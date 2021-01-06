from django.shortcuts import render
from TestApp.forms import FeedbackForm
from django.core.mail import send_mail 

def feedback_form_view(request):
    form=FeedbackForm()
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            print('Basic Validation Completed and Printing Data')
            print('Name:',form.cleaned_data['name'])
            print("village:",form.cleaned_data['village'])
            print("mandal:",form.cleaned_data['mandal'])
            print("district:",form.cleaned_data['district'])
            print("phonenumber:",form.cleaned_data['phonenumber'])
            print('Email:',form.cleaned_data['email'])
            print('Feedback:',form.cleaned_data['feedback']) 
            send_mail(subject, message, from_email, ['jayanth_balla@srmap.edu.in'])
            sent=True
        else:
            form=FeedbackForm() 
    return render(request,'testapp/feedback.html',{'form':form}) 
def thank_you(request):
    return render(request,'testApp/thanks.html')
def home_page_view(request):
    return render(request,'testApp/home.html')
def experts_advice(request):
    return render(request,'testApp/experts.html')
def natural_farming(request):
    return render(request,'testApp/natural.html')
def interview(request):
    return render(request,'testApp/interviews.html')
def Live(request):
    return render(request,'testApp/live.html')
def Home(request):
    return render(request,'testApp/home.html')
def about(request):
    return render(request,'testApp/about.html')