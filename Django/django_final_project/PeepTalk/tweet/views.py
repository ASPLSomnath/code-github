from django.shortcuts import render

# Create your views here.

## add
def index(request):
    return render(request=request , template_name='index.html')
