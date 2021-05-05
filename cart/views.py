from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *

# Create your views here.


class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, req):
        user = req.user
        print(user)
        return Response({'success': 'permission working'})

    def post(self, req):
        data = req.data
        user = req.user
        cart, _ = Cart.objects.get_or_create(user=user, oredered=False)
        product = Course.objects.get(id=data.get('product'))
        quantity = data.get('quantity')

        cart_items = CartItem(user=user, cart=cart,
                              product=product, quantity=quantity)
        cart_items.save()

        return Response({'success': 'Item added to your cart'})

    def update(self, req):
        pass

    def delete(self, req):
        pass
