from django.shortcuts import render
from .model import popularity_based

# Create your views here.
def homepage(request):
    popular = popularity_based(5)
    restaurants = popular.to_dict(orient='records')

    if request.method == 'POST':
        selected_number = int(request.POST.get('number'))
        popular = popularity_based(selected_number).sort_values('rate', ascending=False)
        restaurants = popular.to_dict(orient='records')

    return render(request, 'home.html', {'restaurants': restaurants})