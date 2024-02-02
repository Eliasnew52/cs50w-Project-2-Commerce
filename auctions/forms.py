from django import forms
from .models import Listings, Category, Comments, Bid

class ListingForm(forms.ModelForm):
    
    #List Retrieved From Category Model
    Item_Category = forms.ModelChoiceField(Category.objects.all(),label='Choose Category')
    Price = forms.FloatField()

    class Meta:
        model = Listings
        fields = ['Title','Description','Image','Price','Item_Category']
        widgets = {
            'Title':forms.TextInput(attrs={'class':'form-control w-100','placeholder':'Product Name'}),
            'Description':forms.TextInput(attrs={'class':'form-control w-100','placeholder':'Product Desc'}),
            'Image':forms.FileInput(attrs={'class':'form-control w-100'}),
            
        }
  

    #Own Save Method to Retrieve Owner and Save the Relation between classes
    def save(self, commit=True,user=None):
        Listing = super().save(commit=False)
        Listing.Owner = user
        Listing.save()
        return Listing

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['Author','Listing','Comment']
        widgets = {
            'Comment':forms.TextInput(attrs={'class':'form-control w-100','placeholder':'Add Comment'}),     
        }

    #Own Save Method to Retrieve Owner and Listing to Save Comment
    def save(self, commit=True, user=None, listing=None):
        comment = super().save(commit=False)
        comment.Author = user
        comment.Listing = listing
        if commit:
            comment.save()
        return comment


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['BidCreator','BidListing','BidAmount']


    #Own Save Method to Retrieve Owner and Listing to Save Comment
    def save(self, commit=True, user=None, listing=None):
        bid = super().save(commit=False)
        bid.BidCreator = user
        bid.BidListing = listing
        if commit:
           bid.save()
        return bid
