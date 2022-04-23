from django.contrib import messages
from django.shortcuts import redirect, render

from app.filter import HospitalFilter
from app.forms import hospitalform
from app.models import hospital


def add_hospital(request):
    form = hospitalform()
    if request.method == 'POST':
        form = hospitalform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'successfully added')
            return redirect('admin_home')
    return render(request, 'admin_temp/add_hospital.html', {'form': form})

def view_hospital(request):
    v = hospital.objects.all()
    hospitalfilter = HospitalFilter(request.GET, queryset=v)
    v = hospitalfilter.qs
    context = {
        'hospital': v,
        'hospitalfilter': hospitalfilter,
    }
    return render(request, 'admin_temp/ViewHospital.html', context)
