from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import ShortenedURL
import random
import string
from .forms import URLForm


def redirect_to_original(request, short_code):
    url_entry = get_object_or_404(ShortenedURL, short_code=short_code)
    
    url_entry.click_count += 1
    print(url_entry.click_count)
    url_entry.save()

    return redirect(url_entry.original_url)

def create_short_url(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            original_url = form.cleaned_data['original_url']
            
            short_url = ShortenedURL.objects.create(
                short_code=short_code,
                original_url=original_url
            )
            return render(request, 'shortened_url_success.html', {'short_code': short_code})
    else:
        form = URLForm()
    return render(request, 'main.html', {'form': form})