from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product, Review, Category
from product.serializers import ProductSerializer, CategorySerializer, ReviewSerializer, \
    ProductReviewSerializer, CategoryValidateSerializer, ProductValidateSerializer, ReviewValidateSerializer
from rest_framework import status


@api_view(["GET"])
def product_review_list(request):
    products_reviews = Product.objects.all()
    serializer = ProductReviewSerializer(products_reviews, many=True)
    return Response(data=serializer.data)


@api_view(["GET", "POST"])
def review_list_api_view(request):
    if request.method == "GET":
        """ list of reviews"""
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(data=serializer.data)
    elif request.method == "POST":
        """ created of reviews """
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
        text = serializer.validated_data.get("text")
        stars = serializer.validated_data.get("stars")
        product = serializer.validated_data.get('product')
        reviews = Review.objects.create(text=text, stars=stars, product_id=product)
        return Response(data=ReviewSerializer(reviews).data)


@api_view(["GET", "PUT", "DELETE"])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': "Review not found!"},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        """ retrieve product """
        serializer = ReviewSerializer(review)
        return Response(data=serializer.data)
    elif request.method == "DELETE":
        """ delete review """
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        """ update reviews """
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
        review.text = serializer.validated_data.get('text')
        review.product_id = serializer.validated_data.get('product')
        review.stars = serializer.validated_data.get('stars')
        review.save()
        return Response(data=ReviewSerializer(review).data)


""" alright"""


@api_view(["GET", "POST"])
def category_list_api_view(request):
    if request.method == "GET":
        """ list of category """
        category = Category.objects.all()
        serializer = CategorySerializer(instance=category, many=True)
        return Response(data=serializer.data)
    elif request.method == "POST":
        """ created of category """
        serializer = CategoryValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
        name = serializer.validated_data.get('name')
        category = Category.objects.create(name=name)
        return Response(data=CategorySerializer(category).data)


""" alright """


@api_view(['GET', "PUT", "DELETE"])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': "Category not found!"},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        """ retrieve product """
        serializer = CategorySerializer(category)
        return Response(data=serializer.data)
    if request.method == "DELETE":
        """ delete product """
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == "PUT":
        """ update product """
        serializer = CategoryValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
        category.name = serializer.validated_data.get("name")
        category.save()
        return Response(data=CategorySerializer(category).data)


""" alright """


@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == "GET":
        """ list of product """
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(data=serializer.data)
    elif request.method == "POST":
        """ created of product """
        serializer = ProductValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
        title = serializer.validated_data.get('title')
        descriptions = serializer.validated_data.get('descriptions')
        price = serializer.validated_data.get('price')
        category = serializer.validated_data.get('category')
        product = Product.objects.create(title=title, descriptions=descriptions, price=price, category_id=category)
        return Response(data=ProductSerializer(product).data)


""" alright """


@api_view(["GET", "PUT", "DELETE"])
def product_derail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': "Product not found!"},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        """ retrieve product """
        serializer = ProductSerializer(product)
        return Response(data=serializer.data)
    elif request.method == "DELETE":
        """ delete movie """
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        """ update movie """
        serializer = ProductValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
        product.title = serializer.validated_data.get('title')
        product.descriptions = serializer.validated_data.get("descriptions")
        product.price = serializer.validated_data.get("price")
        product.category_id = serializer.validated_data.get("category")
        product.save()
        return Response(data=ProductSerializer(product).data)



