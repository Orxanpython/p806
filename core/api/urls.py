from core.api.views import *
from django.urls import path


urlpatterns = [
    path('news/', GetNewsAPIView.as_view(), name="get_news"),
    path('create-news/', CreateNewsAPIView.as_view(), name='create-news'),
    path("update-news/<int:id>/", UpdateNewsAPIView.as_view(), name="update_news"),
    path('category/', GetCategoryAPIView.as_view(), name="get_category"),
    path('create-category/', CreateCategoryAPIView.as_view(), name="create-category"),
    path('update-category/<int:id>', UpdateCategoryAPIView.as_view(), name="update_category"),
    path('setting/', GetSettingAPIView.as_view(), name="get_setting"),
    path('create-setting/', CreateSettingAPIView.as_view(), name="create_setting"),
    path("update-setting/<int:id>/", UpdateSettingAPIView.as_view(), name="update_setting"),
    path('product/', GetProductAPIView.as_view(), name="get_product"),
    path('create-product/', CreateProductAPIView.as_view(), name="create_product"),
    path("update-product/<int:id>/", UpdateProductAPIView.as_view(), name="update_product"),
    path('contact/', GetContactAPIView.as_view(), name="get_contact"),
    path('create-contact/', CreateContactAPIView.as_view(), name="create_contact"),
    path("update-contact/<int:id>/", UpdateContactAPIView.as_view(), name="update_contact"),


]   
