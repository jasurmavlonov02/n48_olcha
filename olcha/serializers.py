from rest_framework import serializers
from olcha.models import Category, Group, Product, Image


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


class ProductSerializer(serializers.ModelSerializer):
    # images = ImageSerializer(many=True, read_only=True)
    all_images = serializers.SerializerMethodField()

    def get_all_images(self, instance):
        request = self.context.get('request')
        images = [request.build_absolute_uri(image.image.url) for image in instance.images.all()]
        return images

    class Meta:
        model = Product
        fields = '__all__'
