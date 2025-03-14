from django.shortcuts import render, redirect
from .models import Features
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

# def index(request):
#     features = Features.objects.all()
#     return render(request, 'index.html', {'features': features})


def index(request):
    # Return a simple HTML page with a title and a message
        # features1 = features()
        # features1.id = 1
        # features1.name = 'Feature 1'
        # features1.description = 'This is the first feature'


    features = Features.objects.all()
    return render(request, 'index.html', {'features': features})


    # context = {
    #     'name': 'World',
    #     'message': 'Hello, this is my first Django application!',
    #     'data': 'NameError, please'
    # }
    # return render(request, 'index.html', context)
    
def counter(request):
    message = request.POST['message']
    amount_of_words = len(message.split())
    return render(request, 'counter.html', {'message': message, 'amount': amount_of_words})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmed_password = request.POST['confirmed_password']

        if password == confirmed_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'User registration successful')
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request, pk):
    # feature = Features.objects.get(id=pk)
    return render(request, 'post.html', 
                #   {'feature': feature}
                {'pk': pk}
                  )