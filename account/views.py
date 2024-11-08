from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods

from account.forms import AccountDetailsForm, CustomLoginForm, PasswordForm, StudentLogForm
from account.models import StudentLog, User

# Create your views here.

def home(request):
    return redirect('dashboard')

def create_account_step1(request):
    if request.method == 'POST':
        form = AccountDetailsForm(request.POST)
        if form.is_valid():
            # Save the data to the session or context for use in the next step
            request.session['account_data'] = form.cleaned_data
            return redirect('create_account_step2')
    else:
        form = AccountDetailsForm()
    
    return render(request, 'create_account_step1.html', {'form': form})


def create_account_step2(request):
    account_data = request.session.get('account_data')
    print(account_data)

    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']

            # Create the user from session data and set the password
            user = User(
                name=account_data['name'],
                department=account_data['department'],
                mat_no=account_data['mat_no'],
            )
            user.set_password(password)  # Use Django's password hashing
            user.save()

            messages.success(request, 'successfully created account. please log in')
            return redirect('login')

    else:
        form = PasswordForm()

    return render(request, 'create_account_step2.html', {'form': form, 'account_data': account_data})


def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            mat_no = form.cleaned_data.get('mat_no')
            password = form.cleaned_data.get('password')
            user = authenticate(request, mat_no=mat_no, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.name}!')
                return redirect('dashboard')  # Redirect to dashboard
            else:
                messages.error(request, 'Invalid matriculation number or password.')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomLoginForm()

    return render(request, 'login.html', {'form': form})


@login_required(login_url='/account/login')
def dashboard_view(request):
    user_data = request.user
    logs = StudentLog.objects.filter(student=request.user).order_by('-date')
    form = StudentLogForm()
    
    context={
        'log_form': form,
        'user': user_data,
        'logs': logs,
    }
    return render(request, 'dashboard.html', context=context)

@login_required
@require_POST
def add_log(request):
    form = StudentLogForm(request.POST)
    
    if form.is_valid():
        log = form.save(commit=False)
        log.student = request.user
        log.save()

        context = {'log': log}
        return render(request, 'dashboard.html#logitem-partial', context)
    
@login_required
@require_http_methods(['DELETE'])
def delete_log(request, log_id):
    log = get_object_or_404(StudentLog, id=log_id, student=request.user)
    log.delete()

    response = HttpResponse(status=204)
    response['HX-Trigger'] = f'delete-todo'  # Custom trigger name for the specific log ID
    return response
        

@login_required(login_url='/account/login')
def admin_dashboard_view(request):
    user_data = request.user
    logs = StudentLog.objects.order_by('-date')
    
    context={
        'user': user_data,
        'logs': logs,
    }
    return render(request, 'admin_dashboard.html', context=context)