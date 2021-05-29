from django.shortcuts import render, redirect
from .forms import BusForm, UserForm, UserUpdateForm, driverForm, driverUpdateForm
from .models import Bus, User, driver
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
import secrets, time
from django.core.mail import send_mail
# For password hashing
from django.contrib.auth.hashers import make_password, check_password

def is_admin(user):
   return user.is_superuser

def is_driver(Bus):
   return Bus.role_id

@login_required
def validate(request):
    if request.user.is_superuser:
        return redirect('welcome_admin')
    # elif request.Bus.:
    #     return redirect('welcome_driver')
    else:
        return redirect('welcome_user')

def driver_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # username = driverForm.cleaned_data['username']
        # request.session['username'] = username
        #import pdb; pdb.set_trace()

        user_account = Bus.objects.filter(username=username)
        if user_account.exists():
            user_account = Bus.objects.filter(username=username)[0]
            if (user_account.username == username and  user_account.password == password):
                # context = {'customer_name': user.username}
                name = user_account.driver_name
                bus_route_no = user_account.bus_route_no
                context = {'username': username, 'name' : name, 'bus_route_no' : bus_route_no}
                return render(request, 'bus/welcome_driver.html', context)
            else:
                context = {'message': "*Wrong username or password"}
                return render(request, 'bus/driver_login.html', context)
        else:
            context = {'message': "*No user found for given username"}
            return render(request, 'bus/driver_login.html', context)
    else:
        return render(request, 'bus/driver_login.html')

def home(request):
    return render(request, 'bus/home.html')

@user_passes_test(is_admin)
def welcome_admin(request):
    username = request.user.username
    return render(request, 'bus/welcome_admin.html', {'username': username})

@user_passes_test(is_admin)
def add_driver(request):
    if request.method == "POST":
        form = BusForm(request.POST)
        password = secrets.token_urlsafe(8)
        username = ((request.POST.get('driver_name')).lower()).split()[0] + str(secrets.randbits(8))
        driver_name = request.POST.get('driver_name')
        post_values = request.POST.copy()
        post_values['username'] = username
        post_values['password'] = make_password(password)
        form = BusForm(post_values)
        if form.is_valid():
            subject = f'{driver_name} was added to ITMVU Bus Tracking as a driver'
            message = ''
            from_email = '2017btechcsenityand@itmvu.in'
            recipient_list = ['nityandesai27091998@gmail.com', 'tripathisamir826@gmail.com']
            fail_silently = False
            auth_user = None
            auth_password = None
            connection = None
            html_message = f'''
            Hi Admin,<br>Please give this credentials to {driver_name}, so he/she can login as a driver.<br><br><strong>Username : </strong>{username}<br><strong>Password : </strong>{password}<br><br>**Please take care that the credetials are only given to the driver only for better user experience.**<br>**DO NOT DELETE this mail, keep it through out the year if in case {driver_name} forgets the password or for changes in driver.**
            '''
            send_mail(subject, message, from_email, recipient_list, fail_silently, auth_user, auth_password, connection, html_message) 
            form.save()
            messages.success(request, 'Well done! You just added a driver.')
    form = BusForm()
    return render(request, 'bus/add_driver.html', {'form': form})

@user_passes_test(is_admin)
def add_student(request):
    if request.method == "POST":
        password = secrets.token_urlsafe(8)
        username = request.POST.get('first_name') + str(secrets.randbits(8))
        name = request.POST.get('first_name') + " " + request.POST.get('parent_name') + " " + request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        roll_no = request.POST.get('roll_no')
        parent_name = request.POST.get('parent_name')
        post_values = request.POST.copy()
        post_values['username'] = username
        post_values['password'] = make_password(password)
        form = UserForm(post_values)
        if form.is_valid(): 
            subject = f'{name} was added to ITMVU Bus Tracking as a student'
            message = ''
            from_email = '2017btechcsenityand@itmvu.in'
            recipient_list = [f'{request.POST.get("email")}', f'{request.POST.get("parent_email")}', 'nityandesai27091998@gmail.com', 'tripathisamir826@gmail.com']
            fail_silently = False
            auth_user = None
            auth_password = None
            connection = None
            html_message = f'''Hi there,<br>This mail contains credentials of ITMVU Bus Tracking.<br><br><strong>Roll no of the student: </strong>{roll_no}<br><strong>Username : </strong>{username}<br><strong>Password : </strong>{password}<br><br>**If you're student, Please share this credetials with your parents only,so they can track bus in emergancy conditions.**<br>**DO NOT DELETE this mail, keep it through out the year if in case student forgets the password.**
            '''
            send_mail(subject, message, from_email, recipient_list, fail_silently, auth_user, auth_password, connection, html_message)
            form.save()
            messages.success(request, 'Well done! You just added a student.')
    form = UserForm()
    return render(request, 'bus/add_student.html', {'form': form})

@user_passes_test(is_admin)
def emergency(request):
    if request.method == "POST":
        reason = request.POST.get('reason')
        bus_route_no = request.POST.get('bus_route_no')
        mailList = User.objects.filter(bus_route_no=bus_route_no).values_list('parent_email')
        # form = UserForm()
        # if form.is_valid():
        for mail in mailList.iterator():
            print(mail[0])
            subject = f'ITMVU Bus Tracking - About a delay or an emergancy situation'
            message = ''
            from_email = '2017btechcsenityand@itmvu.in'
            recipient_list = [f'{mail[0]}']
            fail_silently = False
            auth_user = None
            auth_password = None
            connection = None
            html_message = f'''Hi there,<br>Please don't panic but this is to inform you the bus of your child: <strong>Route no. {bus_route_no}</strong> will be having some delay due to <strong>{reason}</strong>.<br>Regards,<br>ITMVU Transport Department.<br>**You can get more info about it by calling to <a href="itmvubustracking.pythonanywhere.com/contact_us">ITMVU Admin department</a> or <a href="itmvubustracking.pythonanywhere.com/your_bus_details">your bus driver</a>.**
            '''
            send_mail(subject, message, from_email, recipient_list, fail_silently, auth_user, auth_password, connection, html_message)
        messages.success(request, 'Emergancy notification mail has been sent.')
    form = UserForm()
    return render(request, 'bus/emergency.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            name = user.first_name + user.parent_name + user.last_name
            roll_no = user.roll_no
            password = f'{request.POST.get("new_password1")}'
            post_values = request.POST.copy()
            post_values['password'] = make_password(password)
            subject = 'The password was changed'
            message = ''
            from_email = '2017btechcsenityand@itmvu.in'
            recipient_list = [f'{user.email}', f'{user.parent_email}', 'nityandesai27091998@gmail.com', 'tripathisamir826@gmail.com']
            fail_silently = False
            auth_user = None
            auth_password = None
            connection = None
            html_message = f'''Hi there,<br>A student's password was changed on ITMVU Bus Tracking.<br><br><strong>Roll no : </strong>{roll_no}<br><strong>New Password : </strong>{password}<br><br>**Please share this credetials with your parents only, so they can track bus in emergancy conditions.**<br>**DO NOT DELETE this mail, keep it through out the year if in case of 'forgot password'.**<br>**If you're the student & you didn't change the password please login with new password and change your password.**
            '''
            send_mail(subject, message, from_email, recipient_list, fail_silently, auth_user, auth_password, connection, html_message)
            update_session_auth_hash(request, user)
            messages.success(request, 'Well done! Your password was successfully updated!')
            return redirect('change_password')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'bus/change_password.html', {'form': form})

def change_pass(request, username):
    driver = Bus.objects.get(username=username)
    form = PasswordChangeForm(request.POST or None)
    if request.method == 'POST':
        if (f'{request.POST.get("old_password")}' == driver.password):
            # bus = form.save()
            name = driver.driver_name
            bus_route_no = driver.bus_route_no
            password = f'{request.POST.get("new_password1")}'
            subject = 'The password has been changed successfully.'
            message = ''
            from_email = '2017btechcsenityand@itmvu.in'
            recipient_list = ['nityandesai27091998@gmail.com', 'tripathisamir826@gmail.com']
            fail_silently = False
            auth_user = None
            auth_password = None
            connection = None
            html_message = f'''Hi there Admin,<br>Driver {name}'s password was changed on ITMVU Bus Tracking.<br><br><strong>Bus Route no : </strong>{bus_route_no}<br><strong>New Password : </strong>{password}<br><br>**Please inform the driver not to share username or password with anyone.**<br>**DO NOT DELETE this mail, keep it for the case of 'forgot password'.**<br>**If the driver & asks he couldn't login, then please give him/her new password to login with & change the password later.**
            '''
            send_mail(subject, message, from_email, recipient_list, fail_silently, auth_user, auth_password, connection, html_message)
            Bus.objects.filter(username = username).update(password = password)
            messages.success(request, 'Well done! Your password was successfully updated!')
        else:
            messages.error(request, 'Try Again! Your old password was wrong!')
    else:
        form = PasswordChangeForm(request.POST or None)
    return render(request, 'bus/change_pass.html', {'form': form})



@user_passes_test(is_admin)
def edit_bus_details(request, pk):
    bus = Bus.objects.get(pk=pk)
    form = BusForm(request.POST or None, instance=bus)
    if request.method == 'POST':
        driver_name = request.POST.get('driver_name')
        driver_mobile_no = request.POST.get('driver_mobile_no')
        # if form.is_valid():
        Bus.objects.filter(pk=pk).update(driver_name = driver_name, driver_mobile_no = driver_mobile_no)
        messages.success(request, 'Well done! Driver details were successfully updated!')
        return redirect('view_bus_details')
    return render(request, 'bus/edit_bus_details.html', {'form': form, 'pk':pk})


@user_passes_test(is_admin)
def edit_student_details(request, pk):
    student = User.objects.get(pk=pk)
    form = UserUpdateForm(request.POST or None, instance=student)
    if request.method == "POST":
        # username = student.username
        # password = student.password
        # first_name = request.POST.get('first_name')
        # last_name = request.POST.get('last_name')
        # email = request.POST.get('email')
        # roll_no = request.POST.get('roll_no')
        # bus_route_no = request.POST.get('bus_route_no')
        # parent_name = request.POST.get('parent_name')
        # parent_email = request.POST.get('parent_email')
        # parent_mobile_no = request.POST.get('parent_mobile_no')
        # User.objects.filter(pk=pk).update(username = username, password = password, first_name = first_name, last_name = last_name, email = email, roll_no = roll_no, bus_route_no = bus_route_no, parent_name = parent_name, parent_mobile_no = parent_mobile_no, parent_email = parent_email)
        if form.is_valid():
            form.save()
            messages.success(request, 'Well done! Student details were successfully updated!')
            return redirect('view_student_details')
            # print(request, 'Well done! Student details were successfully updated!')
    return render(request, 'bus/edit_student_details.html', {'form': form, 'pk':pk})

@user_passes_test(is_admin)
def delete_bus_details(request, pk):
    bus = Bus.objects.get(pk=pk)
    bus.delete()
    # form = BusForm(request.POST or None, instance=bus)
    # if form.is_valid():
    #     form.save()
    messages.success(request, 'Well done! Driver was successfully deleted!')
    return redirect('view_bus_details')

@user_passes_test(is_admin)
def delete_student_details(request, pk):
    student = User.objects.get(pk=pk)
    student.delete()
    # form = BusForm(request.POST or None, instance=bus)
    # if form.is_valid():
    #     form.save()
    messages.success(request, 'Well done! Student was successfully deleted!')
    return redirect('view_student_details')

@user_passes_test(is_admin)
def view_bus_details(request):
    buses = Bus.objects.all()
    return render(request, 'bus/view_bus_details.html', {'buses': buses})

@user_passes_test(is_admin)
def view_student_details(request):
    students = User.objects.exclude(roll_no = 0)
    return render(request, 'bus/view_student_details.html', {'students': students})

#student/parent Login
@login_required
def welcome_user(request):
    user = request.user.bus_route_no
    name = request.user.first_name
    return render(request, 'bus/welcome_user.html', {'name': name})


@login_required
def your_bus_details(request):
    bus = request.user.bus_route_no
    return render(request, 'bus/your_bus_details.html',{'bus':bus})

@login_required
def schedule(request):
    return render(request, 'bus/schedule.html')

def about(request):
    return render(request, 'bus/about.html')

def contact_us(request):
    return render(request, 'bus/contact_us.html')

@login_required
def track_bus(request):
    bus_route_no = int(str(request.user.bus_route_no))
    bus = Bus.objects.filter(bus_route_no=bus_route_no).values_list('lat', 'lon')
    if (bus[0][0] != None) & (bus[0][0] != None):
        lati = bus[0][0]
        longi = bus[0][1]
    else:
        lati = 22.33991955946263
        longi = 73.3614583053149
    return render(request, 'bus/track_bus.html', {'lati':lati, 'longi':longi})

#Driver Login
def welcome_driver(request):
    # driv = str(request.bus.bus_route_no)
    # name = request.bus.driver_name
    # # bus = Bus.objects.all()
    # username = request.bus.username
    # return render(request, 'bus/welcome_driver.html', {'name': name}, {'username' : username}, {'driv' : driv})
    if request.method == 'POST':
        lat = request.POST.get('lat')
        lon = request.POST.get('long')
        pk = request.POST.get('pk')
        username = request.POST.get('username')
        name = request.POST.get('name')
        Bus.objects.filter(pk=pk).update(lat=lat, lon=lon)
        messages.success(request, 'Well done! Your location is shared with the students!')
    return render(request, 'bus/welcome_driver.html', {'bus_route_no': pk, 'username': username, 'name': name})

#Driver Login
def reset(request, pk):
    lat = 22.33991955946263
    lon = 73.3614583053149
    Bus.objects.filter(pk=pk).update(lat=lat, lon=lon)
    messages.success(request, 'Attention! Your location has been reset!')
    return redirect('driver_login')