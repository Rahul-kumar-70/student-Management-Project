from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testapp.models import StudentPG,StudentPhd,StudentEquery
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from testapp.forms import SignUpform
from django.contrib.auth.mixins import LoginRequiredMixin

def homepage(request):
    return render(request,'testapp/home.html')

def aboutpage(request):
    return render(request,'testapp/about.html')

def logoutpage(request):
    logout(request)
    return render(request,'testapp/logout.html')

@login_required
def indexpage(request):
    return render(request,'testapp/index.html')

def signuppage(request):
    form = SignUpform()
    if request.method == 'POST':
        form = SignUpform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  
            user.save()
            return HttpResponseRedirect('/accounts/login')
        else:
            form.add_error(None, "There were errors with your form submission.")
    return render(request, 'testapp/signup.html', {'form': form})


class StudentList(LoginRequiredMixin,ListView):
    model=StudentPG
    ordering=['course']

class StudentDetail(DetailView):
    model=StudentPG

class StudentForm(LoginRequiredMixin,CreateView):
    model=StudentPG
    fields='__all__'
    success_url=('/list')

class StudentUpdate(LoginRequiredMixin,UpdateView):
    model=StudentPG
    fields='__all__'
    success_url='/list'
    
class StudentDelete(LoginRequiredMixin,DeleteView):
    model=StudentPG
    success_url='/list'
    

class StudentPhdList(LoginRequiredMixin,ListView):
    model=StudentPhd
    ordering=['Inrollment_no']

class StudentPhddetail(LoginRequiredMixin,DetailView):
    model=StudentPhd

class StudentPhdform(LoginRequiredMixin,CreateView):
    model=StudentPhd
    fields='__all__'
    success_url=('/listphd')

class StudentPhdUpdate(LoginRequiredMixin,UpdateView):
    model=StudentPhd
    fields='__all__'
    success_url='/listphd'

class StudentPhdDelete(LoginRequiredMixin,DeleteView):
    model=StudentPhd
    success_url='/listphd'

class StudentEnq(CreateView):
    model=StudentEquery
    fields="__all__"
    success_url = ('/thank/')

def thanks(request):
    return render(request,'testapp/thanks.html')
