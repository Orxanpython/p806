from core.api.serializers import *
from core.models import *
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView


class GetNewsAPIView(ListAPIView):
      serializer_class = GetNewsSerializer
      queryset = News.objects.all()
    
class CreateNewsAPIView(CreateAPIView):
      serializer_class = CreateNewsSerializer
      queryset = News.objects.all()
   
    
class UpdateNewsAPIView(RetrieveUpdateDestroyAPIView):
      serializer_class = CreateNewsSerializer
      queryset = News.objects.all()
      lookup_field = "id"
      # lookup_url_kwarg = 'news_id'
      
      
      
      

class GetCategoryAPIView(ListAPIView):
      serializer_class = GetCategorySerializer
      queryset = Category.objects.all()
      
class CreateCategoryAPIView(CreateAPIView):
      serializer_class = CreateCategorySerializer
      queryset = Category.objects.all()
      

class UpdateCategoryAPIView(RetrieveUpdateDestroyAPIView):
      serializer_class = CreateCategorySerializer
      queryset = Category.objects.all()
      lookup_field = "id"
      # lookup_url_kwarg = 'news_id'
    
    
    



class GetSettingAPIView(ListAPIView):
      serializer_class = GetSettingSerializer
      queryset = Setting.objects.all()
      
class CreateSettingAPIView(CreateAPIView):
      serializer_class = CreateSettingSerializer
      queryset = Setting.objects.all()
      

class UpdateSettingAPIView(RetrieveUpdateDestroyAPIView):
      serializer_class = CreateSettingSerializer
      queryset = Setting.objects.all()
      lookup_field = "id"
      # lookup_url_kwarg = 'news_id'
    
    
    
    
class GetProductAPIView(ListAPIView):
      serializer_class = GetProductSerializer
      queryset = Product.objects.all()
      
class CreateProductAPIView(CreateAPIView):
      serializer_class = CreateProductSerializer
      queryset = Product.objects.all()
      

class UpdateProductAPIView(RetrieveUpdateDestroyAPIView):
      serializer_class = CreateProductSerializer
      queryset = Product.objects.all()
      lookup_field = "id"
      # lookup_url_kwarg = 'news_id'



 
class GetContactAPIView(ListAPIView):
      serializer_class = GetContactSerializer
      queryset = Contact.objects.all()
      
class CreateContactAPIView(CreateAPIView):
      serializer_class = CreateContactSerializer
      queryset = Contact.objects.all()
      

class UpdateContactAPIView(RetrieveUpdateDestroyAPIView):
      serializer_class = CreateContactSerializer
      queryset = Contact.objects.all()
      lookup_field = "id"
      # lookup_url_kwarg = 'news_id'
