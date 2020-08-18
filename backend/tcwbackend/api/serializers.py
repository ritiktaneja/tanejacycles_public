from rest_framework import serializers
from .models import Bicycle,Brand, Order, Transaction,SubOrder, Error


class BrandListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Brand
        fields = '__all__'

class BicycleListSerializer(serializers.ModelSerializer):
  
    speed = serializers.CharField(source='get_speed_display')
    wheel_size = serializers.CharField(source='get_wheel_size_display')
    brand = BrandListSerializer(read_only=True)
    images = serializers.SerializerMethodField('get_img_url_list')

    class Meta:
        model = Bicycle
        fields =  '__all__'

          
    def get_img_url_list(self, instance):
        res = []
        if instance.image1 and hasattr(instance.image1,'url'):
            res.append(instance.image1.url)
        if instance.image2 and hasattr(instance.image2,'url'):
            res.append(instance.image2.url)
        if instance.image3 and hasattr(instance.image3,'url'):
            res.append(instance.image3.url)
        return res
       
    def get_field_names(self, declared_fields, info):
        expanded_fields = super(BicycleListSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields


class BicycleDetailSerializer(serializers.ModelSerializer):

  
    speed = serializers.CharField(source='get_speed_display')
    wheel_size = serializers.CharField(source='get_wheel_size_display')
    brand = BrandListSerializer(read_only=True)
    images = serializers.SerializerMethodField('get_img_url_list')

    class Meta:
        model = Bicycle
        fields = '__all__'
        
    def get_img_url_list(self, instance):
        res = []
        if instance.image1 and hasattr(instance.image1,'url'):
            res.append(instance.image1.url)
        if instance.image2 and hasattr(instance.image2,'url'):
            res.append(instance.image2.url)
        if instance.image3 and hasattr(instance.image3,'url'):
            res.append(instance.image3.url)
        return res
       
    def get_field_names(self, declared_fields, info):
        expanded_fields = super(BicycleDetailSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields

class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'

class SubOrderSerializer(serializers.ModelSerializer):
    class Meta : 
        model = SubOrder   
        fields = '__all__'
    
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

