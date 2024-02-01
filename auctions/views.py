from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse

from .models import User, Listings, Category
from .forms import ListingForm


def index(request):
    ActiveListings = Listings.objects.filter(IsActive=True)
    CategoryList = Category.objects.all()
    return render(request, "auctions/index.html",{"Listings":ActiveListings,"Category":CategoryList})


# Listing Creation Function

def NewListing(request):
    username = request.user

    if request.method == "POST":
        form = ListingForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(user=username)
            return redirect("/")
        else:
            return HttpResponse(form.errors.as_json())
    else:
        form = ListingForm()

        return render(request,"auctions/create.html",{"form":form,"username":username})

def Display(request):
    if request.method == "POST":
        Selection = request.POST['category']
        CategorySelected = Category.objects.get(CatName= Selection)
        SelectedListings = Listings.objects.filter(IsActive=True, Item_Category=CategorySelected)
        CategoryList = Category.objects.all()
        return render(request, "auctions/index.html",{
            "Listings":SelectedListings,"Category":CategoryList,"Selection":Selection
            })


def listingInfo(request, id):
    Info = Listings.objects.get(pk=id)
    #We Ensure that the Actual User is already on the Auction Watchlist
    OnWatchList= request.user in Info.Watchlist.all()
    return render(request,"auctions/listing.html",{
        "Info":Info,
        "OnWatchList":OnWatchList
        })



def Watchlist_Remove(request,id):
    Info = Listings.objects.get(pk=id)
    CurrentUser = request.user
    Info.Watchlist.remove(CurrentUser)
    return HttpResponseRedirect(reverse(listingInfo, args=(id, )))



def Watchlist_Add(request,id):
    Info = Listings.objects.get(pk=id)
    CurrentUser = request.user
    Info.Watchlist.add(CurrentUser)
    return HttpResponseRedirect(reverse(listingInfo, args=(id, )))


def DisplayWatchlist(request):
    CurrentUser = request.user
    UserWatchList = CurrentUser.watchlist.all()
    return render(request,"auctions/watchlist.html",{"Listings":UserWatchList})


# D E F A U L T   V I E W S #

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
