from core.models import *
from rest_framework import serializers

class GetNewsSerializer(serializers.ModelSerializer):
      class Meta:
            model = News
            fields = ('title','content', 'image','like', 'dislike', 'views','category')
            
            
class CreateNewsSerializer(serializers.ModelSerializer):
      class Meta:
            model = News
            fields = ('title','content', 'image','category')
            




class GetCategorySerializer(serializers.ModelSerializer):
      class Meta:
        model = Category
        fields =  ('title',)


class CreateCategorySerializer(serializers.ModelSerializer):
      class Meta:
            model = News
            fields =  ('title',)
      






class GetSettingSerializer(serializers.ModelSerializer):
      class Meta:
        model = Setting
        fields = ('logo', 'phone', 'email', 'facebook', 'twitter', 'instagram', 'linkedin', 'bgimg', 'title', 'description')


class CreateSettingSerializer(serializers.ModelSerializer):
      class Meta:
            model = Setting
            fields = ('logo', 'phone', 'email', 'facebook', 'twitter', 'instagram', 'linkedin', 'bgimg', 'title', 'description')





class GetProductSerializer(serializers.ModelSerializer):
      class Meta:
        model = Product
        fields = ('title', 'content', 'category', 'slug', 'image', 'price')


class CreateProductSerializer(serializers.ModelSerializer):
      class Meta:
            model = Product
            fields = ('title', 'content', 'category', 'slug', 'image', 'price')






class GetContactSerializer(serializers.ModelSerializer):
      class Meta:
        model = Contact
        fields = ('name', 'email', 'message', 'timestamp',)


class CreateContactSerializer(serializers.ModelSerializer):
      class Meta:
            model = Contact
            fields = ('name', 'email', 'message', 'timestamp',)

