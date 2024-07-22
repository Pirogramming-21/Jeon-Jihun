from django.shortcuts import render

# Create your views here.

def main(request):
    if request.method == 'GET':
        return render(request, 'users/main.html')
    
def signup(request):
    pass