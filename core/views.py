from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from core.models import Product, News
from core.forms import ContactForm
from django.urls import reverse
# Create your views here.


def home (request):
      context = {
            "home" : "Django",
            "products": Product.objects.all(),
                       
      }
      return render(request, "index.html" , context)







def shop_cart(request):
      context = {
                       
      }
      return render(request, "shopping-cart.html" , context)








from core.forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('contact')  
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

      
      
      
      
      # context = {
                       
      # }
      # return render(request, "contact.html" , context)




def blog(request):
      context = {
                       
      }
      return render(request, "blog.html" , context)


def about_us(request):
      context = {
                       
      }
      return render(request, "about.html" , context)



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
      context = {
                       
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