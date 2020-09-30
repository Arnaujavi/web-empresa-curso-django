from .forms import UserCReationFormWithEmail, ProfileForm, EmailForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCReationFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        #Modificaremos en tiempo real el formulario recogido
        form.fields['username'].widget= forms.TextInput(attrs={'class':'form-control mb2', 'placeholder': 'Nombre de Usuario'})
        form.fields['email'].widget= forms.EmailInput(attrs={'class':'form-control mb2', 'placeholder': 'Email'})
        form.fields['password1'].widget= forms.PasswordInput(attrs={'class':'form-control mb2', 'placeholder': 'Contraseña'})
        form.fields['password2'].widget= forms.PasswordInput(attrs={'class':'form-control mb2', 'placeholder': 'Repite la contraseña'})
        return form

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        #El profile es una variable y created es una variable que devuelve true o false si se ha creado o no
        profile, created = Profile.objects.get_or_create(user = self.request.user)
        return profile

@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'
    def get_object(self):
        return self.request.user


    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        form.fields['email'].widget= forms.EmailInput(attrs={'class':'form-control mb2', 'placeholder': 'Email'})
        return form
