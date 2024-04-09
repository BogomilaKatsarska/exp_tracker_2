from django.shortcuts import render, redirect

from exp_tracker_2.web.forms import CreateProfileForm
from exp_tracker_2.web.models import Profile


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    return render(request, 'home-with-profile.html')


def create_expense(request):
    return render(request, 'expense-create.html')


def edit_expense(request, pk):
    return render(request, 'expense-edit.html')


def delete_expense(request, pk):
    return render(request, 'expense-delete.html')


def show_profile(request):
    return render(request, 'profile.html')


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    return render(request, 'profile-edit.html')


def delete_profile(request):
    return render(request, 'profile-delete.html')
