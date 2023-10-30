

from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from core.models import *
from core.forms import ContactForm
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    sliders = Slider.objects.all()
    tags = Tag.objects.all()

    products = Product.objects.all()
    if 'tags' in request.GET:
        tags_param = request.GET.getlist('tags')
        products = products.filter(tags__title__in=tags_param).distinct()

    context = {
        "sliders": sliders,
        "home": "Django",
        "products": products,
        'mehsul': products,
        'tags': tags,
        'blog_posts': BlogPost.objects.all(),
    }
    return render(request, "index.html", context)







def shop_cart(request):
      context = {
                       
      }
      return render(request, "shopping-cart.html" , context)








from core.forms import ContactForm

def contact_view(request):
    contact_info = ContactInfo.objects.all()
  
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('contact')  
    else:
        form = ContactForm()

        return render(request, 'contact.html', {'form': form, 'contact_info': contact_info})

      
      
      
      
      # context = {
                       
      # }
      # return render(request, "contact.html" , context)



def blog(request):
    blog_posts = BlogPost.objects.all()
    return render(request, "blog.html", {'blog_posts': blog_posts})


def about_us(request):
    about_items = AboutItem.objects.all()  

    context = {
        'about_items': about_items,
    }
    return render(request, 'about.html', context)



def shop_details(request):
      context = {
                       
      }
      return render(request, "shop-details.html" , context)


def check(request):
      context = {
                       
      }
      return render(request, "checkout.html" , context)


def blog_details(request):
      context = {
                       
      }
      return render(request, "blog-details.html" , context)



def shop(request):
      mehsullar = Product.objects.all()
      brands = Brands.objects.all()
      size = Size.objects.all()
      tags = Tag.objects.all()
      color = Color.objects.all()
      
      paginator = Paginator(mehsullar, 6)
      page= request.GET.get('page')
      mehsullar = paginator.get_page(page)
      
      if "brands" in request.GET.keys():        
            mehsullar = Product.objects.filter(
                  brands_id__title=request.GET["brands"])
         
      if "size" in request.GET.keys():        
            mehsullar = Product.objects.filter(
                  size_id__title=request.GET["size"])
            

      if "tags" in request.GET.keys():
             mehsullar = Product.objects.filter(
                    tags__title=request.GET["tags"])

      if "min_price" in request.GET.keys():
       
            mehsullar = Product.objects.filter(
              price__gte=request.GET["min_price"], price__lte=request.GET["max_price"])
      
      if "color" in request.GET.keys():        
            mehsullar = Product.objects.filter(
                  color_id__title=request.GET["color"])
      
      
      product_count = len(mehsullar)  # Count the number of products
      context = {
               "mehsul" : mehsullar,
               'page_obj': page,  
               'brands': brands,
               'size': size, 
               'tags':tags,  
               'color': color,
               'product_count': product_count,  
               
      }
      return render(request, "shop.html" , context)

      
      
      

def male_fashion(request):
      context = {
                       
      }
      return render(request, "index.html" , context)


def shop_detail(request, slug):
      context = {
            "product":  Product.objects.get(slug=slug),
                       
      }
      return render(request, "shop-details.html" , context)





def search(request):
    
    query = request.GET.get('query')

    if query:
        products = Product.objects.filter(title__icontains=query)
        # course = Course.objects.filter(title__icontains=query)
        context = {
            'title': 'Search',
            'query': query,
            'products': products,
            # 'course': course,
        }
        return render(request, 'search.html', context)
    else:
        return HttpResponseRedirect(reverse('home'))
  
  


def shop_product_view(request):    
    products = Product.objects.all()   
    context = {'products': products}
    return render(request, 'shop.html', context)






# from django.shortcuts import render
# from .models import Product

# def filter_products_by_price(request, min_price, max_price):
#     # Convert the price values from string to integers
#     min_price = int(min_price)
#     max_price = int(max_price)
    
#     # Query the products within the specified price range
#     filtered_products = Product.objects.filter(price__gte=min_price, price__lte=max_price)

#     context = {
#         'filtered_products': filtered_products,
#         'min_price': min_price,
#         'max_price': max_price,
#     }

#     return render(request, 'shop.html', context)




from django.shortcuts import render, redirect
from .forms import CheckoutForm
from .models import Order

from django.shortcuts import render, redirect
from .forms import CheckoutForm

def checkout_view(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            form.save()  # Form verilerini veritabanına kaydet
            # Başka bir işlem yapmak veya başarılı sayfaya yönlendirmek için
            return redirect('checkout_view')  # 'success_page'yi başarılı sayfanızın URL'siyle değiştirin
    else:
        form = CheckoutForm()
        
        
    return render(request, 'checkout.html', {'form': form})



def blog_details(request, blog_id):
    blog_post = BlogPost.objects.get(pk=blog_id)
    return render(request, 'blog-details.html', {'blog_post': blog_post})


# def contact_us(request):
#     contact_info = ContactInfo.objects.all()
#     return render(request, 'contact.html', {'contact_info': contact_info})
