from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import DeleteView, UpdateView
from .models import Guest, HouseNo, Member, GuestCategory
from .forms import HouseForm, GuestForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from userdata.models import UserInfo
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import auth
from django.contrib.auth import REDIRECT_FIELD_NAME

class SecretaryView(ListView):
    template_name = 'secretary.html'
    model = Guest


class HouseView(CreateView):
    form_class = HouseForm
    model = HouseNo
    template_name = 'house.html'

    def get_success_url(self):
        return reverse('house')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['house'] = HouseNo.objects.all()
        return context

    def form_valid(self, form):
        form_obj = form.save(commit = False)
        form_obj.user_key = self.request.user
        form_obj.save()
        return HttpResponseRedirect(self.get_success_url())



class AssignMember(CreateView):
    model = Member
    fields = ['user_key']
    template_name = 'assignmember.html'


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['house'] = HouseNo.objects.get(slug = self.kwargs['slug'])
        context['member_obj'] = Member.objects.filter(house_key = context['house'])
        context['user'] = UserInfo.objects.filter(is_member = True)
        return context

    def get_success_url(self):
        return reverse_lazy('assignmember', kwargs={'slug' : self.kwargs['slug']})

    def post(self, *args, **kwargs):
        user = self.request.POST['uname']
        house_no = HouseNo.objects.get(slug = self.kwargs['slug'])
        user_instance = User.objects.get(pk = user)

        if Member.objects.filter(user_key = user_instance):
            print("already there")
        else:
            member_obj = Member()
            member_obj.s_key = self.request.user
            member_obj.house_key = house_no
            member_obj.user_key = user_instance
            member_obj.save()

        return HttpResponseRedirect(self.get_success_url())


def delete(request, slug, id):
    Member.objects.filter(id = id).delete()
    return redirect('assignmember', slug)



class GuestView(LoginRequiredMixin, CreateView):
    model = GuestCategory
    template_name = 'guestc.html'
    form_class = GuestForm
    login_url = '/accounts/Login/'
    redirect_field_name = 'redirect_to'


    def get_success_url(self):
        return reverse_lazy('guest')

    def form_valid(self, form):
        form_obj = form.save(commit=False)
        head_key = Member.objects.get(house_key = form_obj.house_key.id, is_head = True)
        form_obj.user_key = self.request.user
        if form_obj.special_key is None:
            form_obj.special_key = head_key.user_key
            form_obj.save()
        form_obj.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        search_data = self.request.GET.get('search')
        context['house'] = HouseNo.objects.all().order_by('number')
        if search_data:
            context['house'] = HouseNo.objects.filter(number__startswith = search_data).order_by('number')
        return context

class HouseGuestView(LoginRequiredMixin,ListView):
    model = Guest
    template_name = 'allguest.html'
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        qs = super().get_queryset()
        house_no = HouseNo.objects.get(slug = self.kwargs['slug'])
        return qs.filter(house_key = house_no).order_by("-create_at")

    def get_success_url(self):
        return reverse_lazy('houseguest', kwargs={'slug':self.kwargs['slug']})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['slug'] = HouseNo.objects.get(slug = self.kwargs['slug'])
        return context

class HouseGuestEdit(UpdateView):
    model = Guest
    fields = ['total_member','guest_name','mobile_number']
    template_name = 'editguest.html'

    def get_success_url(self):
        return reverse_lazy('houseguest',kwargs={'slug':self.kwargs['slug']})

def logout(request):
    auth.logout(request)
    return redirect('login')

# class DataSerializer(serializer.ModelSerializer):
#     member_obj = Member.object.url.then
#     queryset = SerializerClass
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data( *args, **kwargs)
#         context = User(get_or_404_found).filter(is_head = True)
#         return context
#
#     def set_dispatch(self):
#         Object_Serializer = self.kwargs['slug']
#         return set_dispatch.super(Object_Serializer)
