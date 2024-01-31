from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.NewListing, name="NewListing"),
    path("display", views.Display,name="Display"),
    path("listing/<int:id>",views.listingInfo,name="Listing"),
]
