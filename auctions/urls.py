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
    path("remove/<int:id>",views.Watchlist_Remove,name="watchlist_remove"),
    path("add/<int:id>",views.Watchlist_Add,name="watchlist_add"),
    path("watchlist",views.DisplayWatchlist,name="display_watchlist"),

]
