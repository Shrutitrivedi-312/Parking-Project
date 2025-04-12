from django.shortcuts import render
from .models import ParkingRequest
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from .models import ParkingRequest, Guard
from .models import ParkingSpot  # Assuming you have a ParkingSpot model

def search(request):
    query = request.GET.get('query', '')  # Get the search term from the query string
    results = ParkingSpot.objects.filter(name__icontains=query)  # Search for matching records
    data = list(results.values())  # Convert queryset to a list of dictionaries
    return JsonResponse({'results': data})  # Return results as JSON

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                return redirect('home')  # Replace 'home' with your homepage view
            else:
                return render(request, 'parking_app/login.html', {'error': 'Invalid credentials'})
        except User.DoesNotExist:
            return render(request, 'parking_app/login.html', {'error': 'User does not exist'})
    return render(request, 'parking_app/login.html')

def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = make_password(request.POST['password'])
        email = request.POST['email']

        if not User.objects.filter(username=username).exists():
            User.objects.create(username=username, password=password, email=email)
            return redirect('parking_app/login.html')  # Redirect to login page after successful signup
        else:
            return render(request, 'parking_app/signup.html', {'error': 'Username already exists'})
    return render(request, 'parking_app/signup.html')

def about(request):
    return render(request, 'parking_app/aboutus.html')

def login(request):
    return render(request, 'parking_app/login.html')

def more(request):
    return render(request, 'parking_app/more.html')

def book_parking(request):
    return render(request, 'parking_app/book_parking.html')

def home(request):
    return render(request, 'parking_app/mainpage.html')

def look_park(request):
    return render(request, 'parking_app/look_parking.html')

def look_for_parking(request):
    if request.method == "POST":
        search = request.POST.get("search")

        # Find the guard responsible for the location
        guard = Guard.objects.filter(location__icontains=search).first()

        if guard:
            # Create a new parking request assigned to the guard
            parking_request = ParkingRequest.objects.create(user_query=search, guard=guard)

            # Inform the user that their request is being processed
            message = f"Your request for parking at {search} has been forwarded to {guard.name}. You will receive a reply shortly."
        else:
            message = f"No guard available for {search}. Please try again later."

        return render(request, 'parking_app/look_parking.html', {'message': message})

    return render(request, 'parking_app/look_parking.html')
