from django.shortcuts import render

from home.forms import NewsletterSignupForm

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def newsletter(request):
    form = NewsletterSignupForm(request.POST or None)
    if  request.method == 'POST':
        if form.is_valid():
            form.save()

            return render(request, 'home/thankyou.html')
    return render(request, 'home/signup.html', {'form': form})