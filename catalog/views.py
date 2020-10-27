from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product, Category, ProductReview
from django.db.models import Q # new
from django.contrib import messages
from django.core.paginator import Paginator


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
            print(f"Category: {products}")
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


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    #review = ProductReview.objects.get_queryset().order_by('id')
    review = product.reviews.all()

    paginator = Paginator(review, 2)

    page = request.GET.get('page')
    reviews = paginator.get_page(page)

    context = {
        'product': product,
        'reviews': reviews
    }

    return render(request, 'product_detail.html', context)
    

def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    print(f"product: {product}")
    if request.method == 'POST' and request.user.is_authenticated:
        print(f"star in the request: {request.POST['stars']}")
        stars = request.POST.get('stars', 4)
        content = request.POST.get('content', '')

        review = ProductReview.objects.create(product=product, user=request.user, stars=stars, content=content)
        review.save()

        return redirect(reverse('product_detail', args=[product_id]))





#https://djangopy.org/how-to/how-to-implement-categories-in-django/
#https://learndjango.com/tutorials/django-search-tutorial
#http://www.learningaboutelectronics.com/Articles/How-to-add-search-functionality-to-a-website-in-Django.php