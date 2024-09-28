from django.db.models import Avg
from rest_framework import serializers
from olcha.models import Category, Group, Product, Image, Comment, ProductAttribute


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    full_image_url = serializers.SerializerMethodField()
    count = serializers.SerializerMethodField(method_name='groups_count')

    def groups_count(self, obj):
        count = obj.groups.count()
        return count

    def get_full_image_url(self, instance):

        if instance.image:
            image_url = instance.image.url
            request = self.context.get('request')
            return request.build_absolute_uri(image_url)
        else:
            return None

    class Meta:
        model = Category
        fields = ['id', 'title', 'full_image_url', 'slug', 'count', 'groups']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttribute
        exclude = ('id','product','attr_key','attr_value')

    def to_representation(self, instance):
        context = super(ProductAttributeSerializer, self).to_representation(instance)
        context['key_id'] = instance.attr_key.id
        context['key_name'] = instance.attr_key.key_name

        context['value_id'] = instance.attr_value.id
        context['value_name'] = instance.attr_value.value_name
        return context
        # return {instance.attr_key.key_name: instance.attr_value.value_name}


class ProductSerializer(serializers.ModelSerializer):
    attributes = ProductAttributeSerializer(many=True,read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    # images = ImageSerializer(many=True, read_only=True)
    all_images = serializers.SerializerMethodField()
    users_like = serializers.SerializerMethodField()
    category_name = serializers.CharField(source='group.category.title')
    avg_rating = serializers.SerializerMethodField()

    def get_avg_rating(self, instance):
        instance = instance.comments.all().aggregate(avg_rating=Avg('rating', default=0))
        return round(instance['avg_rating'])

    def get_users_like(self, product):
        user = self.context.get('request').user
        if not user.is_authenticated:
            return False
        if user in product.users_like.all():
            return True

        return False

    def get_all_images(self, instance):
        request = self.context.get('request')
        images = [request.build_absolute_uri(image.image.url) for image in instance.images.all()]
        return images

    def to_representation(self, product):
        context = super(ProductSerializer, self).to_representation(product)
        context['comments_count'] = product.comments.count()
        return context

    class Meta:
        model = Product
        fields = '__all__'












'''
BASIC authenticatin
SESSION 
Token
Django JWT => Json Web TOken
'''
