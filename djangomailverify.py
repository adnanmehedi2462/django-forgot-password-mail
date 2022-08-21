# Setting......................

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL= 'OTF team <adnanmehedi54@gmail.com>'

# url.py/////////////////////////////////
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
    path('reset/password/',PasswordResetView.as_view(template_name="reset_password.html"), name='password_reset'),
    
    path('reset/password/done/',PasswordResetDoneView.as_view(template_name="reset_password_done.html"), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/',PasswordResetCompleteView.as_view(template_name="password_reset_complate.html"), name='password_reset_complete'),

    # view.py////////////////////////////////////////////////////////////

def register(request):
    
    
    if request.user.is_authenticated:
        return redirect("/") 
    else:
        

        form=createform()
        
        if request.method=='POST': 
   
            form=createform(request.POST)
                  
            if form.is_valid():

                user=form.save()
                # for mail
                current_site=get_current_site(request)
            
                mail_subject="An account created"
                message=render_to_string('Account.html',{
                    'user':user,
                    'domain':current_site.domain,
                })
                send_mail=form.cleaned_data.get('email')
                email=EmailMessage(mail_subject,message,to=[send_mail])
                email.send()
                # End mail
           
                
                return redirect("userlogin")
                                    
            else:
                messages.success(request,'something Wrong !!')

                
        context={
            "form":form
        }
        return render(request,"register.html",context)
        
    

# account.html///////////////////////////////////


{% autoescape off %}
    Hi {{user.username}},
    You have created an account on 
    http://{{domain}},
    
{% endautoescape %}
