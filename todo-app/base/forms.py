from django.forms import ModelForm
from .models import Task
 
 
class UpdateOrder(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'