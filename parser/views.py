from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .scraper import scrape_aliexpress

@login_required
def index(request):
    products = []
    if request.method == 'POST':
        url = request.POST.get('url')
        if url:
            products = scrape_aliexpress(url)
    return render(request, 'parser/index.html', {'products': products})