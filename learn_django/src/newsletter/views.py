
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm, SignUpForm
from .models import SignUp

# Create your views here.

def home(request):
   title="Sign Up Now"
   form=SignUpForm(request.POST or None)
   context={
      "title":title,
      "form":form,
}
  # if request.user.is_authenticated(): 
  #      title="My Title %s" %(request.user)

   print (request)
   if request.method=="POST":
       print (request.POST)
   

   if form.is_valid():
      instance=form.save(commit=False)
      full_name=form.cleaned_data.get("full_name")
      #if not full_name:
      #   full_name="new full name"
      instance.full_name=full_name
      instance.save()
      context={
         "title":"Thank You"
}   

   if request.user.is_authenticated() and request.user.is_staff:
    #print(SignUp.objects.all())
       queryset= SignUp.objects.all().order_by('-timestamp')
       context={
    "queryset":queryset
}
   return render(request,"home.html",context)


def contact(request):
   title="Contact Us"
   title_align_center= False
   form=ContactForm(request.POST or None)
   if form.is_valid():
      #for key, value in iter(form.cleaned_data.items()):
      #   print (key, value)
         #print (form.cleaned_data.get(key))
      form_email=form.cleaned_data.get("email")
      form_message=form.cleaned_data.get("message")
      form_full_name=form.cleaned_data.get("full_name")
      #print (email,message,full_name)
      subject='Site contact form'
      from_email=settings.EMAIL_HOST_USER
      recipient_list=['akhithaskumar@gmail.com']
      message='here is the message'
      #contact_message="%s:%svia%s"%(
      #     form_full_name,
      #     form_message,
      #     form_email) 
      send_mail(subject, 
           contact_message,
           from_email, 
           recipient_list, 
           fail_silently=True)
      
   context={
      "form":form,
      "title":title,
      "title_align_center":title_align_center,
}
   return render(request, "forms.html", context)