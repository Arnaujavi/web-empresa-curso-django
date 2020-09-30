from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCReationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required = True, help_text ="Requerido, 254 caracteres como maximo y debe ser valido")

    class Meta:
        model = User
        fields = ('username', "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email = email).exists(): #El filter nunca da error ya que devuelve una lista vacia si no hay nada
            raise forms.ValidationError("El email ya está registrado. Prueba con otro.")#Aqui mandamos un mensaje de error si ya existe un usuario
        
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}), #Este widget nos permite limpiar la imagen en el formulario
            'bio': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder': 'Biografia'}),
            'link': forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder': 'Enlace'})
        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required = True, help_text ="Requerido, 254 caracteres como maximo y debe ser valido")
    
    class Meta:
        model = User
        fields = ['email']


    def clean_email(self):
        email = self.cleaned_data.get("email")
        
        if 'email' in self.changed_data: #Aqui estan todos los campos que se han modificado en el formulario
            if User.objects.filter(email = email).exists(): #El filter nunca da error ya que devuelve una lista vacia si no hay nada
                raise forms.ValidationError("El email ya está registrado. Prueba con otro.")#Aqui mandamos un mensaje de error si ya existe un usuario
        return email