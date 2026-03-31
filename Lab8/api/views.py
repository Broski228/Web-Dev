import json
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Product, Category


def product_to_dict(product):
    return {
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'count': product.count,
        'is_active': product.is_active,
        'category_id': product.category_id,
    }


def category_to_dict(category):
    return {
        'id': category.id,
        'name': category.name,
    }


@require_GET
def products_list(request):
    products = Product.objects.all()
    data = [product_to_dict(p) for p in products]
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


@require_GET
def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
        return JsonResponse(product_to_dict(product), json_dumps_params={'ensure_ascii': False})
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404, json_dumps_params={'ensure_ascii': False})


@require_GET
def categories_list(request):
    categories = Category.objects.all()
    data = [category_to_dict(c) for c in categories]
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


@require_GET
def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
        return JsonResponse(category_to_dict(category), json_dumps_params={'ensure_ascii': False})
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404, json_dumps_params={'ensure_ascii': False})


@require_GET
def products_by_category(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404, json_dumps_params={'ensure_ascii': False})

    products = Product.objects.filter(category=category)
    data = [product_to_dict(p) for p in products]
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

@require_GET
def products_byprice(request):
    cheap = Product.objects.filter(price__lt=100).order_by('price')
    expensive = Product.objects.filter(price__gte = 100).order_by('price')
    data = {
        'under_100': [product_to_dict(p) for p in cheap],
        'above_100': [product_to_dict(p) for p in expensive]
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii':False})