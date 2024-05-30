from django.shortcuts import redirect, render
from django.urls import reverse
from .form import SignForm,UserForm,ProfileForm
from django.contrib.auth import authenticate,login
from .models import Profile

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = signup(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
            
    else:
        form = SignForm()
        context = {'form':form}

    return render(request,'registration/signup.html',context)

def profile(request):
    p = Profile.objects.get(user = request.user)
    return render(request,'accounts/profile.html',{'pro':p})

def profile_edit(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        u = UserForm(request.POST,request.FILES,instance=request.user)
        p= ProfileForm(request.POST,request.FILES,instance=request.user)
        if u.is_valid() and p.is_valid():
            u.save()
            myprofile = p.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))

    else:
        u = UserForm(instance=request.user)
        p= ProfileForm(instance=profile)


    return render(request,'accounts/profile_edit.html',{'u' : u ,'p' : p})
