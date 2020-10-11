from django.shortcuts import render

# Create your views here.
from user.forms import UserForm


def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'user/registeration/register.html', {'form': form})
