from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products.html', context)

def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entry_query = utils.get_query(query_string, ['title', 'body',])
        posts = Post.objects.filter(entry_query).order_by('created')
        return render(request, 'search_results.html', { 'query_string': query_string, 'posts': posts })
    else:
        return render(request, 'search_resukts.html', { 'query_string': 'Null', 'found_entries': 'Enter a search term' })


#https://djangopy.org/how-to/how-to-implement-categories-in-django/
#https://learndjango.com/tutorials/django-search-tutorial
#http://www.learningaboutelectronics.com/Articles/How-to-add-search-functionality-to-a-website-in-Django.php