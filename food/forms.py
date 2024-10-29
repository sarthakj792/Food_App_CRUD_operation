from food.models import Dishlist
from django  import  forms

class Userform(forms.ModelForm):

    class Meta:

        model = Dishlist
        fields = ('name','description' , 'price' , 'propic')

