from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from company.models import Company, Job, JobLocation, CRPDate, Attachment, Branch, month_list
from consent.models import PersonalDetail, EducationDetail, CGPA

from datetime import date
import itertools as it


def index(request):
	#return render(request, 'base.html')
    return HttpResponse("Aakash says hello world!")

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if (email):
        	username = User.objects.get(email=email).username
        else:
        	username = None

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/consent/home')
            else:
                return HttpResponse("Your TnP account is disabled.")
        else:
            #print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'consent/login_user.html', {})


def grouper(n, iterable):
    """
    >>> list(grouper(3, 'ABCDEFG'))
    [['A', 'B', 'C'], ['D', 'E', 'F'], ['G']]
    """
    iterable = iter(iterable)
    return iter(lambda: list(it.islice(iterable, n)), [])


def home(request):
    branch = EducationDetail.objects.get(user=request.user).branch
    jobs = Job.objects.filter(eligible_branches=branch).order_by('-updated_at')

    print (jobs)
    companies_list = []
    for job in jobs:
        job_dict = {}
        job_dict["company"] = job.company.name
        job_dict["designation"] = job.designation
        job_dict["ctc"] = str(job.ctc)
        job_dict["url"] = "/company/"+job.slug
        if(job.updated_at >= request.user.last_login):
            job_dict["new_badge"] = 1
        else:
            job_dict["new_badge"] = 0
        
        crp = job.crpdate
        
        if (crp.datatype == 'DAT'):
            crpdate_str = str(crp.date)
        elif (crp.datatype == 'MON'):
            crpdate_str = month_list[crp.month]
        elif (crp.datatype == 'WOM'):
            crpdate_str = crp + ' week of ' + crp.month
        else:
            crpdate_str = 'Not Available'

        job_dict["date"] = crpdate_str
        companies_list.append(job_dict)

    companies_list = list(grouper(3,companies_list))
    print (companies_list) 
    return render(request, 'consent/home.html', {'companies_list': companies_list})
 

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')