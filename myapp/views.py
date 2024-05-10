from django.shortcuts import render

# Create your views here.
def index(request):
  # No data needed for this view, so we can pass an empty dictionary
  context = {}
  return render(request, 'index.html', context)