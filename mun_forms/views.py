from django.shortcuts import render, HttpResponse
from mun_forms import forms
from mun_forms.models import ApplicationFormData


def application_form(request):
    if request.method == 'POST':
        form = forms.ApplicationForm(request.POST)
        if form.is_valid():
            obj = ApplicationFormData(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                dob=form.cleaned_data['dob'],
                institution=form.cleaned_data['institution'],
                mun_exp=form.cleaned_data['mun_exp'],
                council_p1=form.cleaned_data['council_p1'],
                council_p2=form.cleaned_data['council_p2'],
                imp_p1=form.cleaned_data['imp_p1'],
                q1=form.cleaned_data['q1'],
                q2=form.cleaned_data['q2'],
                accommodation=form.cleaned_data['accommodation']
            )
            obj.save()
            name = form.cleaned_data['name']
            return HttpResponse('Success:' + name)
        return HttpResponse('Invalid')
    else:
        form = forms.ApplicationForm()
        context = {'form': form}
        return render(request, 'application_form.html', context)
