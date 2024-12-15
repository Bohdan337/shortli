from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import ShortenedURL
import random
import string
from .forms import URLForm
from django.contrib.auth.decorators import login_required

# @login_required
def redirect_to_original(request, short_code):
    url_entry = get_object_or_404(ShortenedURL, short_code=short_code)
    
    url_entry.click_count += 1
    print(url_entry.click_count)
    url_entry.save()

    return redirect(url_entry.original_url)

# @login_required
def create_short_url(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            original_url = form.cleaned_data['original_url']
            
            short_url = ShortenedURL.objects.create(
                short_code=short_code,
                original_url=original_url,
                author=request.user if request.user.is_authenticated else None
            )
            return render(request, 'url/shortened_url_success.html', {'short_code': short_code})
    else:
        form = URLForm()
    return render(request, 'url/main.html', {'form': form})


def welcome(request):
    return render(request, 'url/welcome.html')