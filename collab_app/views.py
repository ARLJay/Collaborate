from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """Takes url request, returns Http response."""
    return HttpResponse("Hello, world.")

def about(request):
    """Takes url request, returns about page"""
    pass

def contact_us(request):
    """Takes url request, returns contact-us page"""
    pass

def sign_up(request):
    """Takes url request, returns sing-up page"""
    pass

def login(request):
    """Takes url request, returns login page"""
    pass

def my_account(request):
    """Takes url request, returns my-account page"""
    pass

def general(request):
    """Takes url request, returns general page"""
    pass

def universities(request):
    """Takes url request, returns universities page"""
    pass

def show_university(request):
    """Takes url request, returns a specific university page"""
    pass

def add_university(request):
    """Takes url request, returns the creation page for new universities"""
    pass

def show_category(request):
    """Takes url request, returns a specific category page"""
    pass

def add_category(request):
    """Takes url request, returns the creation page for new categories"""
    pass

def show_page(request):
    """Takes url request, returns a specific page"""
    pass

def add_page(request):
    """Takes url request, returns the creation page for new pages"""
    pass