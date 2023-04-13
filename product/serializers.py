from rest_framework import serializers
from product.models import Product, Review, Category


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text product stars'.split()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name product_count'.split()


class ProductReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "id title descriptions price category avg_rating".split()


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField()


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    descriptions = serializers.CharField()
    price = serializers.IntegerField()
    category = serializers.IntegerField()


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    product = serializers.IntegerField()
    stars = serializers.IntegerField()