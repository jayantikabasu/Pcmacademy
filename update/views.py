from django.shortcuts import render,HttpResponse, redirect
from .models import *
from django.contrib import messages  

# Create your views here.
def index(request):
    
    try:
        Nav1Obj = Nav1.objects.latest('created_at')
    except Nav1.DoesNotExist:
        Nav1Obj = None
    try:
        SliderObj = HomePage_Slider.objects.latest('created_at')
    except HomePage_Slider.DoesNotExist:
        SliderObj = None
    try:
        HeadCard1Obj = HomePage_HeadCard1.objects.latest('created_at')
    except HomePage_HeadCard1.DoesNotExist:
        HeadCard1Obj = None
    try:
        HeadCard2Obj = HomePage_HeadCard2.objects.latest('created_at')
    except HomePage_HeadCard2.DoesNotExist:
        HeadCard2Obj = None
    try:
        HeadCard3Obj = HomePage_HeadCard3.objects.latest('created_at')
    except HomePage_HeadCard3.DoesNotExist:
        HeadCard3Obj = None
    try:
        HeadCard4Obj = HomePage_HeadCard4.objects.latest('created_at')
    except HomePage_HeadCard4.DoesNotExist:
        HeadCard4Obj = None
    try:
        KeyPointsObj = HomePage_KeyPoints.objects.latest('created_at')
    except HomePage_KeyPoints.DoesNotExist:
        KeyPointsObj = None
    try:
        AboutNITDObj = HomePage_AboutNITD.objects.latest('created_at')
    except HomePage_AboutNITD.DoesNotExist:
        AboutNITDObj = None
    try:
        CourseHomeObj = HomePage_CourseHome.objects.all()
    except HomePage_CourseHome.DoesNotExist:
        CourseHomeObj = None
    try:
        RequestQuoteObj = HomePage_RequestQuote.objects.latest('created_at')
    except HomePage_RequestQuote.DoesNotExist:
        RequestQuoteObj = None
    try:
        ReviewObj = HomePage_Review.objects.all()
    except HomePage_Review.DoesNotExist:
        ReviewObj = None
    try:
        GalleryObj = HomePage_Gallery.objects.latest('created_at')
    except HomePage_Gallery.DoesNotExist:
        GalleryObj = None

    context = { 'Nav1Obj' : Nav1Obj,
                'SliderObj' : SliderObj,
                'HeadCard1Obj' : HeadCard1Obj,
                'HeadCard2Obj' : HeadCard2Obj,
                'HeadCard3Obj' : HeadCard3Obj,
                'HeadCard4Obj' : HeadCard4Obj,
                'KeyPointsObj' : KeyPointsObj,
                'AboutNITDObj' : AboutNITDObj,
                'CourseHomeObj' : CourseHomeObj,
                'RequestQuoteObj' : RequestQuoteObj,
                'ReviewObj' : ReviewObj,
                'GalleryObj' : GalleryObj,
              }
    

    return render(request, 'index.html',context)


def applyform(request):

    try:
        if request.method == "POST":
            name = request.POST.get("name", "")
            phone_number = request.POST.get("phone_number", "")
            course = request.POST.get("course", "")
            message = request.POST.get("message", "")

            if (
                len(name) < 3 
                or len(str(phone_number)) < 10 
                or len(course) < 4 
                or len(message) < 15
            ):
                return redirect("index")
            
            else:
                Apply_FormObj = ApplyForm(
                    name = name,
                    phone_number = phone_number,
                    course = course,
                    message = message

                )
                Apply_FormObj.save()
                return redirect("index")
    
    except Exception:
        return redirect("index")

    

def get_quote(request):

    try: 
        if request.method == "POST":
            name = request.POST.get("name", "")
            email_id = request.POST.get("email_id", "")
            qualification = qualification.POST.get("qualification", "")
            phone = request.POST.get("phone", "")
            message = request.POST.get("message", "")

            if(
                len(name) < 3
                or len(str(phone)) < 10
                or len(qualification) < 4 
                or len(message) < 15
            ):
                messages.error(
                    request, "Invalid input. Please check your details and try again."
                )
            else:
                quoteObj = RequestQuoteFm(
                    name = name,
                    email_id = email_id,
                    qualification = qualification,
                    phone = phone,
                    message = message,
                )
                quoteObj.save()
                messages.success(request, "Your request was sent succesfully. We'll get back to you soon!")

        else:
            messages.error(request, "Invalid request. Please try again.")

    except Exception:
        messages.error(request, "Something went wrong. Please try again.")

    return redirect("index")

def about(request):

    try:
        Nav1Obj = Nav1.objects.latest('created_at')
    except Nav1.DoesNotExist:
        Nav1Obj = None
    try:
        HeadObj = AboutPage_Head.objects.latest('created_at')
    except AboutPage_Head.DoesNotExist:
        HeadObj = None
    try:
        StablishObj = AboutPage_Stablish.objects.latest('created_at')
    except AboutPage_Stablish.DoesNotExist:
        StablishObj = None
    try:
        AboutNITDObj = HomePage_AboutNITD.objects.latest('created_at')
    except HomePage_AboutNITD.DoesNotExist:
        AboutNITDObj = None
    try:
        WhyUsObj = AboutPage_WhychooseUs.objects.latest('created_at')
    except AboutPage_WhychooseUs.DoesNotExist:
        WhyUsObj = None


    context = { 'Nav1Obj' : Nav1Obj,
                'HeadObj' : HeadObj,
               'StablishObj' : StablishObj,
               'AboutNITDObj' : AboutNITDObj,
               'WhyUsObj' : WhyUsObj,
               }

    return render(request, 'about.html',context)

def course(request):

    try:
        Nav1Obj = Nav1.objects.latest('created_at')
    except Nav1.DoesNotExist:
        Nav1Obj = None
    try:
        HeadObj = AboutPage_Head.objects.latest('created_at')
    except AboutPage_Head.DoesNotExist:
        HeadObj = None
    try:
        CourseHomeObj = HomePage_CourseHome.objects.all()
    except HomePage_CourseHome.DoesNotExist:
        CourseHomeObj = None
   

    context = { 'Nav1Obj' : Nav1Obj,
               'HeadObj' : HeadObj,
               'CourseHomeObj' : CourseHomeObj,
    }

    return render(request, 'course.html',context)

def course_details(request, pk):

    try:
        Nav1Obj = Nav1.objects.latest('created_at')
    except Nav1.DoesNotExist:
        Nav1Obj = None
    try:
        HeadObj = AboutPage_Head.objects.latest('created_at')
    except AboutPage_Head.DoesNotExist:
        HeadObj = None
    try:
        CourseHomeObj = HomePage_CourseHome.objects.all()
    except HomePage_CourseHome.DoesNotExist:
        CourseHomeObj = None
    CoursedetailsObj = HomePage_CourseHome.objects.get(pk=pk)


    context = {'Nav1Obj' : Nav1Obj,
               'HeadObj' : HeadObj,
               'CourseHomeObj' : CourseHomeObj,
               'CoursedetailsObj':CoursedetailsObj
               }
    return render(request, 'coursedetail.html',context)

def faculty(request):
    
    try:
        Nav1Obj = Nav1.objects.latest('created_at')
    except Nav1.DoesNotExist:
        Nav1Obj = None
    try:
        HeadObj = AboutPage_Head.objects.latest('created_at')
    except AboutPage_Head.DoesNotExist:
        HeadObj = None
    try:
        corporate_trainerObj = FacultyPage_corporate_trainer.objects.all()
    except FacultyPage_corporate_trainer.DoesNotExist:
        corporate_trainerObj = None

    context = { 'Nav1Obj' : Nav1Obj,
               'HeadObj' : HeadObj,
               'corporate_trainerObj' : corporate_trainerObj,
    }

    return render(request, 'faculty.html',context)


def contact(request):
    
    try:
        Nav1Obj = Nav1.objects.latest('created_at')
    except Nav1.DoesNotExist:
        Nav1Obj = None
    try:
        HeadObj = AboutPage_Head.objects.latest('created_at')
    except AboutPage_Head.DoesNotExist:
        HeadObj = None

    context = { 'Nav1Obj' : Nav1Obj,
               'HeadObj' : HeadObj,
    }

    try:
        if request.method == 'POST':

            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST["phone"]
            course = request.POST['course']
            message = request.POST['message']

            # print(name,email,phone,course)
            if (
                len(name) < 2 
                or len(str(phone)) < 10 
                or len(course) < 5
                or len(email) < 5
                or len(course) < 15
            ):
                messages.error(request, "Invalid request. Please try again.")
                
            
            else:
                contactobj=ContactForm(name=name,email=email,phone=phone,course=course,message=message)
                contactobj.save()
                messages.success(request, "Your request was sent succesfully. ThankYou! ")
        
        
            
    except Exception:
        return redirect("contact")
    


    return render(request, 'contact.html',context)



