from decimal import Decimal
from rest_framework import serializers
from store.models import Product, Collection, Review

class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    products_count = serializers.IntegerField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'inventory', 'price', 'price_with_tax', 'collection']

    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length= 255)
    # price = serializers.DecimalField(max_digits=6, decimal_places=2)
    price_with_tax = serializers.SerializerMethodField(method_name= 'calculate_tax')
    # collection = serializers.HyperlinkedRelatedField(
    #     queryset=Collection.objects.all(),
    #     view_name='collection-detail'
    # )

    def calculate_tax(self, product):
        return product.price * Decimal(1.1)
    
    
class ReviewSerializer(serializers.ModelSerializer):
      class Meta:
          model = Review
          fields = ['id', 'date', 'name', 'description']

      def create(self, validated_data):
            product_id = self.context['product_id']
            Review.objects.create(product_id=product_id, **validated_data)
