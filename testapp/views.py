from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import signupform,UserProfileForm,signupupdateform,UserProfileUpdateForm
from django.http import HttpResponseRedirect
from testapp.models import UserProfile
from django.contrib.auth.models import User

# Create your views here.

@login_required
def home_page_view(request):
    return render(request,'testapp/home.html')

@login_required
def main_page_view(request):
    user_list =  User.objects.all()
    user_list2 = UserProfile.objects.all()
    return render(request,'testapp/mainpage.html',{'user_list':user_list,'user_list2':user_list2})

@login_required
def plan_page_view(request):
    return render(request,'testapp/plans.html')

def abtus_page_view(request):
    return render(request,'testapp/abtus.html')

def logout_view(request):
    return render(request,'testapp/logout.html')


def sign_up_view(request):
    form = signupform(request.POST or None)
    profile_form = UserProfileForm(request.POST or None)
    if request.method=='POST':
        form = signupform(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            user.set_password(user.password)
            user.save()
            profile.save()
            return HttpResponseRedirect('/accounts/login')
        else:
            form = signupform(request.POST)
            profile_form = UserProfileForm(request.POST)
    return render(request,'testapp/signup.html',{'form':form , 'profile_form': profile_form})

@login_required
def updateform(request):
    u_form = signupupdateform(request.POST or None, instance=request.user)
    p_form = UserProfileUpdateForm(request.POST or None , instance=request.user.userprofile)
    if request.method == 'POST':
        u_form = signupupdateform(request.POST, instance=request.user)
        p_form = UserProfileUpdateForm(request.POST, instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            profile = p_form.save()
            user.save()
            profile.save()
            return HttpResponseRedirect('/')
    return render(request, 'testapp/update.html', {'u_form': u_form, 'p_form': p_form})