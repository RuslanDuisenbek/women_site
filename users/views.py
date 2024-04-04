from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from djangoProject import settings
from .forms import LoginUserForm, RegisterUserForm, ProfileForm, UserPasswordChangeForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Authorization'}

    # def get_success_url(self):
    #     return reverse_lazy('home')


class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect('home')

    def post(self, request):
        return self.get(request)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': 'Registration'}
    success_url = reverse_lazy('users:login')


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileForm
    template_name = 'users/profile.html'
    extra_context = {
        'title': 'Profile of user',
        'default_image': settings.DEFAULT_USER_IMAGE
    }

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChangeView(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('users:password_change_done')
    template_name = 'users/password_change_form.html'
