from django import forms
from .models import Listings, Category

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

