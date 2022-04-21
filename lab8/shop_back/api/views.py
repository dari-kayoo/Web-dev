from django.http.response import HttpResponse, JsonResponse
from api.models import Product, Category

#a
def products_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=0)

#b
def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message': str(e)})
    return JsonResponse(product.to_json())

#c
def categories_list(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=0)

#d
def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'message': str(e)})
    return JsonResponse(category.to_json())
