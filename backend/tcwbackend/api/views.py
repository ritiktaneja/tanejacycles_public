from django.shortcuts import render,redirect

from .models import Bicycle, Order , Transaction, SubOrder , Error
from .serializers import BicycleListSerializer,BicycleDetailSerializer,OrderSerializer,TransactionSerializer, SubOrderSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics

from django_filters import rest_framework as filters
from .filters import BicycleFilter

from . import Checksum
from django.conf import settings

from .constants import OrderStatus

from django.core.mail import send_mail

# Create your views here.

class BicycleListView(generics.ListAPIView):
   
        queryset = Bicycle.objects.all().order_by('-in_stock')
        serializer_class = BicycleListSerializer
        filter_backends = (filters.DjangoFilterBackend,)
        #filterset_fields = ('name','category')
        filter_class = BicycleFilter



class BicycleDetailView(APIView):
    def get(self,request,**kwargs):
        bicycle = Bicycle.objects.get(id=kwargs['bicycle_id'])
        serializer = BicycleDetailSerializer(bicycle)
        return Response(serializer.data)


class OrderCreateView(APIView):
    # def get(self,request,**kwargs):
    #     order =   OrderSerializer(data=Order.objects.all(),many=True)
    #     res = []

    #     if order.is_valid():
    #         order = order.data
    #         for o in order:
    #             perorder_dict = dict()
    #             perorder_dict = o
    #             suborder_data = SubOrder.objects.filter(ORDERID = o['id'])
    #             suborder_serializer = SubOrderSerializer(data=suborder_data,many=True)
    #             if suborder_serializer.is_valid():
    #                 perorder_dict['products'] = suborder_serializer.data
    #                 res.append(perorder_dict)
    #             else:
    #                 print('here',suborder_serializer.error)
    #     else:
    #         print('hereeee',order.errors)        
              
            

   
        # return Response(res)
  
    def post(self,request, format=None):
        print('here in /api/orders')
        amount = 0
        bicycles = request.data['bicycle']
        #print('bicycle_id = ',bicycles)
        
        for pkey in bicycles:
            bicycle = Bicycle.objects.get(pk=pkey['id'])
            amount = amount + bicycle.price
            print('Pkey = ',pkey,'Amount = ',bicycle.price)

        print("Amount = ",amount)
        print('Request data = ',request.data)
        serializer = OrderSerializer(data=request.data)
        if amount:
            request.data['amount'] = amount
          
            if serializer.is_valid():
                serializer.save()

                suborder_data = dict()

                for b in bicycles:
                    bicycle = Bicycle.objects.get(pk=b['id'])
                    
                    suborder_data['bicycle'] = b['id']
                    suborder_data['amount'] = bicycle.price
                    suborder_data['color'] = b['color'][0]
                    suborder_data['ORDERID'] = serializer.data['id']
                    suborder_data['qty'] = 1   #v2 changes
                    print(serializer.data['id'],'#$#$')

                    suborder_serializer = SubOrderSerializer(data = suborder_data)

                    if suborder_serializer.is_valid():
                        suborder_serializer.save()
                        print('Suborder Saved')
                    else:
                        print(suborder_serializer.errors,'ERROR SUBORDER')
        
                
                
                MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
                MERCHANT_ID = settings.PAYTM_MERCHANT_ID    
                
                
            
            
                data_dict = {
                    'MID' : MERCHANT_ID,
                    'ORDER_ID' : str(serializer.data['id']),
                    'TXN_AMOUNT' : str(amount),
                    'CUST_ID':serializer.data['phone'],
                    'INDUSTRY_TYPE_ID' : 'ECommerce',
                    'WEBSITE' : 'DEFAULT',
                    'CHANNEL_ID' : 'WEB',
                    'CALLBACK_URL' : 'https://tanejacycles.com/api/transaction/'
                }
                
                paytmchecksum = Checksum.generateSignature(data_dict,MERCHANT_KEY)
                verifychecksum = Checksum.verifySignature(data_dict,MERCHANT_KEY,paytmchecksum)

                param_dict = data_dict

                param_dict['CHECKSUMHASH'] = paytmchecksum

                print("generateSignature Returns:" + str(paytmchecksum))
                print("verifySignature Returns:" + str(verifychecksum))

                return Response(param_dict,status=status.HTTP_201_CREATED)
            
            
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_200_OK)

class TransactionCreateView(APIView):
    
    def post(self,request):
        serializer = TransactionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
            MERCHANT_ID = settings.PAYTM_MERCHANT_ID
            print('DATA : ',request.data.dict())
            data_dict = {}
           
            
            paytmParams = dict()
            paytmParams = request.data.dict()
            paytmChecksum = paytmParams['CHECKSUMHASH']
            paytmParams.pop('CHECKSUMHASH', None)

            # Verify checksum
            # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys 
            isVerifySignature = Checksum.verifySignature(paytmParams, MERCHANT_KEY,paytmChecksum)
            if isVerifySignature:
                print("Checksum Matched")
                print(serializer.data['STATUS'])
                if serializer.data['STATUS'] == 'TXN_SUCCESS' : 
                    order = Order.objects.get(pk=serializer.data['ORDERID'])
                    order.orderStatus = OrderStatus.confirmed.value
                    order.paymentStatus = "Confirmed"
                    order.save()

                    subject = 'Your Order Has Been Placed! - Taneja Cycles'
                    message = 'Thank you for placing your order. Your Order ID is '+str(order.id)
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [order.email,'tanejacycleworks@gmail.com']
                    send_mail( subject, message, email_from, recipient_list )
                    
                    return redirect('https://tanejacycles.com/track/success/'+str(order.id))
                elif serializer.data['STATUS'] == 'TXN_PENDING':
                    order = Order.objects.get(pk=serializer.data['ORDERID'])
                    order.orderStatus = OrderStatus.confirmed.value
                    order.paymentStatus = "Pending"
                    order.save()
                    subject = 'Your Order Has Been Placed! - Taneja Cycles'
                    message = 'Thank you for placing your order. Your payment status is pending. We are contacting the bank and will get back to you shortly! Your Order Id is '+str(order.id)
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [order.email,'tanejacycleworks@gmail.com']
                    send_mail( subject, message, email_from, recipient_list )

                    return redirect('https://tanejacycles.com/track/pending/'+str(order.id))
                else :
                    order = Order.objects.get(pk=serializer.data['ORDERID'])
                    order.paymentStatus = "Failed"
                    subject = 'Transaction Failed - Taneja Cycles'
                    message = 'Thank you for showing your interest in Taneja Cycles. However your order couldn\'t be processed as the transaction failed at the gateway.We\'ll be contacting you shortly. Your Order Id is '+str(order.id)
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [order.email,'tanejacycleworks@gmail.com']
                    send_mail( subject, message, email_from, recipient_list )
                    order.save()
                    return redirect('https://tanejacycles.com/track/failure/')
                
                ##reminder Function here


            else:
                print("Checksum Mismatched")
                return Response(status=404)

class OrderStatusView(APIView):
    def get(self,request):
        uid = request.GET.get('id',None)
        phone = request.GET.get('phone',None)

        if uid is not None and phone is not None:
            try:
                order = Order.objects.get(phone=phone,id=uid)
                serialized_data = OrderSerializer(order)
                return Response(serialized_data.data,status=status.HTTP_200_OK)

            except Order.DoesNotExist:
                return Response({'exists':False},status=status.HTTP_200_OK)
           

class ErrorCreateView(APIView):
    def post(self,request):
        error = Error(error=str(request.data))
        error.save()
        return Response(status=status.HTTP_200_OK)        
               
           
            


       
        
