from django.shortcuts import render
from django.http import  Http404
from .forms import  Country_form,NewCasesForm
# Create your views here.
from .models import  Country,NewCases
def homeview(request):
    template_name='main/index.html'
    return render(request,template_name)


def is_superuser(call):
    def function_wraper(request, **args):
        print('hello fuc wraper')
        if request.user.is_superuser :
            return call(request, **args)
        raise Http404
    return function_wraper


@is_superuser
def load_all_country(request):

    qs=Country.objects.all()
    if request.GET.get('c',None):
        qs=qs.filter(country_name__icontains=request.GET.get('c'))

    ctx={
    "objects":qs
    }
    return render(request,'main/loadData.html',ctx)

@is_superuser
def updateCountry(request,id):

    obj=Country.objects.get(id=id)
    if request.method=='POST':
        form=Country_form(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.save()
    else:
        form=Country_form(
        initial={
        'country_name':obj.country_name,
        'total_cases':obj.total_cases,
        'total_death':obj.total_death,
        'total_recover':obj.total_recover,
        'active_cases':obj.active_cases,
        'total_case_per_minion_pop':obj.total_case_per_minion_pop,
        'total_death_per_minion_pop':obj.total_death_per_minion_pop,
        }
        )

    ctx={
    'form':form,
    'new_cases':obj.new_cases.all(),
    }
    return render(request,'main/updates.html',ctx)


@is_superuser
def updateNewCase(request,id):
    obj=NewCases.objects.get(id=id)
    if request.method=='POST':
        form=NewCasesForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.save()
    else:
        form=NewCasesForm(initial={
        'new_cases':obj.new_cases,
        'new_death':obj.new_death,
        })
    ctx={
    'form':form,
    'date':obj.date
    }
    return render(request,'main/updateCases.html',ctx);
