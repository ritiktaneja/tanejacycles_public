from django.urls import path

from .views import BicycleListView,BicycleDetailView,OrderCreateView,TransactionCreateView,OrderStatusView, ErrorCreateView

urlpatterns = [
    path('bicycles/',BicycleListView.as_view()),   #Card View
    path(r'bicycles/<int:bicycle_id>/',BicycleDetailView.as_view()), #Detail View
    path('orders/',OrderCreateView.as_view()),
    path('transaction/',TransactionCreateView.as_view()),
    path('order-status/',OrderStatusView.as_view()),
    path('error/',ErrorCreateView.as_view())

]