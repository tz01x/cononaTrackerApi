from django.shortcuts import render,redirect
from django.http import  Http404
from main.models import  Country
from django.views import generic
from .forms import ContactForm
from django.utils import  safestring
# Create your views here.
def display(request):
    ctx={}
    try:

        qs=Country.objects.get(country_name__icontains='World')
        ctx={
        'total_cases':qs.total_cases,
        'total_death':qs.total_death,
        }
    except:
        pass
    return render(request,'frontend/home.html',ctx)
def details(request,name):
    try:
        qs=Country.objects.get(country_name=name)
        print(qs)
    except Country.DoesNotExist:
        raise  Http404("No MyModel matches the given query")
    return render(request,'frontend/details.html',{'qs':qs})

def About(request):
    context={
    'objects':[{
    'title':'About',
    'body':' Covid-Tracker and Covid-Api is run by an only one  developer with the goal of making  statistics report of Corona Virus  available in a thought-provoking and time relevant format to a wide audience around the world. It is published by a small and independent only one developer in Bangladesh. We have no political, governmental, or corporate affiliation.'
    },{
    'title':'How it works',
    'body':'''
        For the COVID-19 data, we collect data from official reports,
        and Data was Scrap form International website  like <a href="https://www.worldometers.info/">Worldometer</a> and other .

    '''}]
    }
    template_name='frontend/about.html'
    return render(request,template_name,context)
def source(request):
    context={
    'objects':[
    {
    'title':'Sources',
    'body':'''
        <ol>
        <li><a href="https://www.iedcr.gov.bd/">IEDCR-BD</a>-Institute of Epidemiology, Disease Control and Research</li>
        <li><a href="https://www.worldometers.info/coronavirus/">worldometers</a>-  real time world statistics</li>
        <li id="ref-1"><a href="https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports/">Novel Coronavirus (2019-nCoV) situation reports</a> -
        <a href="https://www.who.int/">World Health Organization</a> (WHO) </li>
        <li id="ref-2"><a href="https://www.cdc.gov/coronavirus/2019-ncov/cases-in-us.html">2019 Novel Coronavirus (2019-nCoV) in the U.S.</a> -. <a href="https://www.cdc.gov/">U.S. Centers for Disease Control and Prevention</a> (CDC) </li>
        <li id="ref-3"><a href="http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml">Outbreak Notification</a> - National Health Commission (NHC) of the People’s Republic of China</li>
        <li id="ref-4"><a href="https://www.health.gov.au/health-topics/novel-coronavirus-2019-ncov">Novel coronavirus (2019-nCoV)</a> - Australian Government Department of Health</li>
        <li id="ref-5"><a href="https://www.medrxiv.org/content/10.1101/2020.01.23.20018549v2">Novel coronavirus 2019-nCoV: early estimation of epidemiological parameters and epidemic prediction</a> - Jonathan M. Read et al, Jan. 23,2020.</li>
        <li id="ref-7"><a href="https://www.imperial.ac.uk/mrc-global-infectious-disease-analysis/news--wuhan-coronavirus/">Report 3: Transmissibility of 2019-nCoV</a> - 25 January 2020 - Imperial College London‌</li>
        <li id="ref-8"><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3809029/">Case fatality risk of influenza A(H1N1pdm09): a systematic review</a> - Epidemiology. Nov. 24, 2013</li>
        <li id="ref-9"><a href="https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(20)30185-9/fulltext#tbl1">A novel coronavirus outbreak of global health concern</a> - Chen Want et al. The Lancet. January 24, 2020 </li>
        <li id="ref-10"><a href="https://www.cdc.gov/coronavirus/2019-ncov/about/symptoms.html">Symptoms of Novel Coronavirus (2019-nCoV)</a> - CDC</li>
        </ol>
    '''
    },
    ]
    }
    template_name='frontend/about.html'

    return render(request,template_name,context)


def Contact(request):
    form=ContactForm()
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('frontend:contact')
    context={
    'objects':
        [
            {
                'title':'Contact me',

            }
        ],
    'form':form
    }
    return render(request,'frontend/about.html',context)
