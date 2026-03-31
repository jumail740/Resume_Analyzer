from django.shortcuts import render
from .forms import ResumeForm
from .models import ResumeAnalysis
from .utils import extract_text
from .gemini import analyze_resume
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.contrib.auth.models import User

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, password=password1)
                login(request, user)
                return redirect('login')

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    if request.method=='POST':
        form=ResumeForm(request.POST,request.FILES)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            
            text = extract_text(instance.resume)
            instance.extracted_text = text
            
            result = analyze_resume(text, instance.job_description)
            instance.result = result
            instance.save()
             
            return render(request, 'result.html', {'result': result})
    else:
        form = ResumeForm()

    return render(request, 'home.html', {'form': form})


@login_required
def dashboard(request):
    analyses = ResumeAnalysis.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'dashboard.html', {'analyses': analyses})

