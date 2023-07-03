


from django.views import View
from django.http import JsonResponse
from .data import products
from .serializers import ProductSerializer
class ProductList(View):
    def get(self,request):
        serialized_products=ProductSerializer(products,many=True).data
        return JsonResponse(products,safe=False)

class ProductListById(View):
    def get(self,request,id):
        product = next((product for product in products if product['id'] == id), None)
        return JsonResponse(product,safe=False)
