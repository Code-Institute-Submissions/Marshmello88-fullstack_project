from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q # new
from django.contrib import messages


# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None #new
    categories = None #new

    print(f"REQUEST: {request.GET}")

    if request.GET: #new
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            print(f"Category: {categories}")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name=categories)

        if 'q' in request.GET: #new
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query, #new
        'current_categories': categories, #new
    }

    return render(request, 'products.html', context)


#https://djangopy.org/how-to/how-to-implement-categories-in-django/
#https://learndjango.com/tutorials/django-search-tutorial
#http://www.learningaboutelectronics.com/Articles/How-to-add-search-functionality-to-a-website-in-Django.php