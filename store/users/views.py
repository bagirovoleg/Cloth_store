from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy

from products.models import Basket, Product, ProductCategory
from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from common.views import TitleMixin


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index:index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'You have been successfully registered'
    title = 'Store - Registration'

    def get_context_data(self, **kwargs):
        context = super(UserRegistrationView, self).get_context_data(**kwargs)
        # context['title'] = 'Store - Registration'
        return context


class UserProfileView(TitleMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_message = 'You have been successfully change your date'
    title = 'Store - Profile'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id), )

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        # context['title'] = 'Store - Profile'
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index:index'))

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Your personal data has been changed')
#             return HttpResponseRedirect(reverse('users:profile'))
#         else:
#             print(form.errors)
#     else:
#         form = UserProfileForm(instance=request.user)
#
#     baskets = Basket.objects.filter(user=request.user)
#     total_sum = 0
#     total_quantity = 0
#     for basket in baskets:
#         total_sum += basket.sum()
#         total_quantity += basket.quantity
#
#     context = {
#         'title': 'Store - Profile',
#         'form': form,
#         'baskets': Basket.objects.all(),
#         'total_sum': total_sum,
#         'total_quantity': total_quantity,
#     }
#     return render(request, 'users/profile.html', context)
