from django.db import models
from ckeditor.fields import RichTextField
from PIL import Image
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

# Create your models here.

# Home Page models 

def NITD_Logo_diamension(value):
    img = Image.open(value)
    required_width = 247
    required_height = 259
    if img.width != required_width and img.height != required_height:
        raise ValidationError(f'The image diamensions must be - Width:{required_width}px, height:{required_height}px')

class Nav1(models.Model):

    logo = models.ImageField(upload_to='Nav_logo', help_text="NITD Logo | width= 250px height= 80px ", 
                             validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"]), NITD_Logo_diamension,],)
    email = models.EmailField(max_length=120, help_text ="Enter Email of Company | max_length = 120")
    call_number = models.CharField(max_length=20, help_text ="Enter phone_number of Company")

    created_at = models.DateTimeField(auto_now_add = True)

    def _str_(self):
        return f"Navbar Details"
    
def Home_Slider_diamension(value):
    img = Image.open(value)
    required_width =1600
    required_height = 1066
    if img.width != required_width and img.height != required_height:
        raise ValidationError(f'The image diamensions must be - Width:{required_width}px, height:{required_height}px')

class HomePage_Slider(models.Model):

    title1 = models.CharField(max_length=150, help_text ="max_length = 150")
    description1 = models.CharField(max_length=150, help_text ="max_length = 150")
    bg_img1 = models.ImageField(upload_to = 'Home_Slider', help_text="Home Slider | width= 2000px height= 1335px ", 
                                validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg"]), Home_Slider_diamension,],)
    title2 = models.CharField(max_length=150, help_text ="max_length = 150")
    description2 = models.CharField(max_length=150, help_text ="max_length = 150")
    bg_img2 = models.ImageField(upload_to = 'Home_Slider', help_text="Home Slider | width= 2000px height= 1335px ", 
                                validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg"]), Home_Slider_diamension,],)

    created_at = models.DateTimeField(auto_now_add = True)

    def _str_(self):
        return f"HomePage Slider"

class HomePage_HeadCard1(models.Model):

    title = models.CharField(max_length=20, help_text ="Home_head card1 title | max_length = 20")
    content = RichTextField()

    created_at = models.DateTimeField(auto_now_add = True)

    def _str_(self):
        return f"{self.title}"

class HomePage_HeadCard2(models.Model):

    title = models.CharField(max_length=20, help_text ="Home_head card2 title | max_length = 20")
    content = RichTextField()

    created_at = models.DateTimeField(auto_now_add = True)

    def _str_(self):
        return f"{self.title}"

class HomePage_HeadCard3(models.Model):

    title = models.CharField(max_length=30, help_text ="Home_head card3 title | max_length = 30")
    content = RichTextField()

    created_at = models.DateTimeField(auto_now_add = True)

    def _str_(self):
        return f"{self.title}"

class HomePage_HeadCard4(models.Model):

    title = models.CharField(max_length=20, help_text ="Home_head card4 title | max_length = 20")
    content = RichTextField()

    created_at = models.DateTimeField(auto_now_add = True)

    def _str_(self):
        return f"{self.title}"


def KeyPoints_diamension(value):
    img = Image.open(value)
    required_width = 408
    required_height = 612
    if img.width != required_width and img.height != required_height:
        raise ValidationError(f'The image diamensions must be - Width:{required_width}px, height:{required_height}px')

class HomePage_KeyPoints(models.Model):

    title = models.CharField(max_length=20, help_text ="KeyPoints title | max_length = 20")
    description = models.CharField(max_length=500)

    sub_title1 = models.CharField(max_length=50, help_text ="KeyPoints subtitle1 | max_length = 50")
    content1 = RichTextField()

    sub_title2 = models.CharField(max_length=50, help_text ="KeyPoints subtitle2 | max_length = 50")
    content2 = RichTextField()

    sub_title3 = models.CharField(max_length=50, help_text ="KeyPoints subtitle3 | max_length = 50")
    content3 = RichTextField()

    sub_title4 = models.CharField(max_length=50, help_text ="KeyPoints subtitle4 | max_length = 50")
    content4 = RichTextField()

    sub_title5 = models.CharField(max_length=50, help_text ="KeyPoints subtitle5 | max_length = 50")
    content5 = RichTextField()

    sub_title6 = models.CharField(max_length=50, help_text ="KeyPoints subtitle6 | max_length = 50")
    content6 = RichTextField()

    img = models.ImageField(upload_to= 'KeyPoints', help_text="KeyPoints side image | width= 408px height= 612px ", 
                                validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg"]), KeyPoints_diamension,],)

    created_at = models.DateTimeField(auto_now_add = True)

    def _str_(self):
        return f"{self.title}"


def About_bg_diamension(value):
    img = Image.open(value)
    required_width = 2000
    required_height = 1335
    if img.width != required_width and img.height != required_height:
        raise ValidationError(f'The image diamensions must be - Width:{required_width}px, height:{required_height}px')

def About_main_diamension(value):
    img = Image.open(value)
    required_width = 1000
    required_height = 563


class HomePage_AboutNITD(models.Model):

    bg_img = models.ImageField(upload_to= 'home_about', help_text="About on home bg | width= 2000px height= 1333px ", 
                                validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg"]), About_bg_diamension,],)
    img = models.ImageField(upload_to= 'home_about', help_text="About on home image | width= 1000px height= 563px ", 
                                validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg"]), About_main_diamension,],)
    video_url = models.URLField(help_text = "Youtube video URL for About on HomePage")
    title = models.CharField(max_length=20, help_text ="About on HomePage title | max_length = 20")
    content = RichTextField()
    trainer_count = models.IntegerField(help_text = "Enter the number of Trainers")
    students_count = models.IntegerField(help_text = "Enter the number of Studentss")

    created_at = models.DateTimeField(auto_now_add = True)

    def _str_(self):
        return f"{self.title}"


def Course_Home_diamension(value):
    img = Image.open(value)
    required_width = 1000
    required_height = 750

class HomePage_CourseHome(models.Model):

    img = models.ImageField(upload_to= 'courseHome', help_text="Course Field Image ", 
                                validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg"]), Course_Home_diamension,],)
    courseTitle = models.CharField(max_length = 50, help_text = "Course title here | max_length = 50 ")
    content = RichTextField()

    created_at = models.DateTimeField(auto_now_add = True)

    def _str_(self):
        return f"Course Section HomePage"

class HomePage_RequestQuote(models.Model):

    title = models.CharField(max_length = 20, help_text = "Request a Quote title | max_length = 20")
    content = RichTextField()

    created_at = models.DateTimeField(auto_now_add = True)

    def _str_(self):
        return f"{self.title}"
    

def Client_Review_diamension(value):
    img = Image.open(value)
    required_width = 800
    required_height = 850
    if img.width != required_width and img.height != required_height:
        raise ValidationError(f'The image diamensions must be - Width:{required_width}px, height:{required_height}px')

class HomePage_Review(models.Model):

    img = models.ImageField(upload_to= 'Client_review', help_text="Client Image | width= 800px height= 850px ", 
                                validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg"]), Client_Review_diamension,],)
    comment = RichTextField()
    name = models.CharField(max_length = 20, help_text = "Client Name | max_length = 20")
    position = models.CharField(max_length = 20, help_text = "Client Position | max_length = 20")

    created_at = models.DateTimeField(auto_now_add = True)

    def _str_(self):
        return f"Client Reviews"


def Gallery_Home_diamension(value):
    img = Image.open(value)
    required_width = 1000
    required_height = 750


class HomePage_Gallery(models.Model):

    img1 = models.ImageField(upload_to= 'gallery_home', help_text="Gallery on home | width= 1000px height= 750px ", 
                                validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg"]), Gallery_Home_diamension,],)
    img2 = models.ImageField(upload_to= 'gallery_home', help_text="Gallery on home | width= 1000px height= 750px ", 
                                validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg"]), Gallery_Home_diamension,],)
    img3 = models.ImageField(upload_to= 'gallery_home', help_text="Gallery on home | width= 1000px height= 750px ", 
                                validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg"]), Gallery_Home_diamension,],)

    created_at = models.DateTimeField(auto_now_add = True)

    def _str_(self):
        return f"Gallery HomePage"


# 
# 
# About Page models 
# 
# 

def Head_About_diamension(value):
    img = Image.open(value)
    required_width = 640
    required_height = 360
    if img.width != required_width and img.height != required_height:
        raise ValidationError(f'The image diamensions must be - Width:{required_width}px, height:{required_height}px')

class AboutPage_Head(models.Model):

    bg_img = models.ImageField(upload_to= 'aboutpagehead', help_text="About head bg | width= 848.8px height= 600px ", 
                                validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg"]), Head_About_diamension,],)

    created_at = models.DateTimeField(auto_now_add = True)

    def _str_(self):
        return f"AboutPage Head bg_img"


def Stablish_About_diamension(value):
    img = Image.open(value)
    required_width = 479
    required_height = 612


class AboutPage_Stablish(models.Model):

    img = models.ImageField(upload_to= 'stablishedsection', help_text="Stablished side image | width= 479px height= 612px ", 
                                validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg"]), Stablish_About_diamension,],)
    title = models.CharField(max_length = 100, help_text = "Stablish detail title | max_length = 100")
    content = RichTextField()

    created_at = models.DateTimeField(auto_now_add = True)

    def _str_(self):
        return f"{self.title}"

# class journey(models.Model):     


def MV_bg_About_diamension(value):
    img = Image.open(value)
    required_width = 2000
    required_height = 1333
    if img.width != required_width and img.height != required_height:
        raise ValidationError(f'The image diamensions must be - Width:{required_width}px, height:{required_height}px')
    
def MV_About_diamension(value):
    img = Image.open(value)
    required_width = 600
    required_height = 400
    if img.width != required_width and img.height != required_height:
        raise ValidationError(f'The image diamensions must be - Width:{required_width}px, height:{required_height}px')
    
class AboutPage_MissionVision(models.Model):

    img1 = models.ImageField(upload_to= 'MissionVision', help_text="Mission image | width= 600px height= 400px ", 
                                validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg"]), MV_About_diamension,],)
    title1 = models.CharField(max_length= 20, help_text = "Mission title")                   
    content1 = RichTextField()
    img2 = models.ImageField(upload_to= 'MissionVision', help_text="Vision image | width= 600px height= 400px ", 
                                validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg"]), MV_About_diamension,],)
    title2 = models.CharField(max_length= 20, help_text = "Vision title")                 
    content2 = RichTextField()

    created_at = models.DateTimeField(auto_now_add = True)

    def _str_(self):
        return f"Mission Vision"

    
def dedicated_team_diamension(value):
    img = Image.open(value)
    required_width = 512
    required_height = 512
    if img.width != required_width and img.height != required_height:
        raise ValidationError(f'The image diamensions must be - Width:{required_width}px, height:{required_height}px')

class AboutPage_dedicated_team(models.Model):

    img = models.ImageField(upload_to= 'dedicated_team', help_text="dedicated_team | width= 512px height= 512px ", 
                                validators=[FileExtensionValidator(allowed_extensions=["png"]), dedicated_team_diamension,],)
    trainer_name = models.CharField(max_length = 20, help_text = 'Trainer name | length max = 20')
    trainer_designation = models.CharField(max_length = 50, help_text = 'Trainer designation | length max = 50')
    twitter_link = models.URLField(null=True, blank=True, help_text = 'Trainer twitter/company link')
    linkedin_link = models.URLField(null=True, blank=True, help_text = 'Trainer linkedin/company link')
    google_plus_link = models.URLField(null=True, blank=True, help_text = 'Trainer google_plus/company link')
    instagram_link = models.URLField(null=True, blank=True, help_text = 'Trainer instagram/company link')

    def _str_(self):
        return f"{self.trainer_name}"
    
def corporate_trainer_diamension(value):
    img = Image.open(value)
    required_width = 700
    required_height = 700

    
class FacultyPage_corporate_trainer(models.Model):

    img = models.ImageField(upload_to= 'corporate_trainer', help_text="corporate_trainer | width= 800px height= 850px ", 
                                validators=[FileExtensionValidator(allowed_extensions=["jpg","jpeg"]), corporate_trainer_diamension,],)
    trainer_name = models.CharField(max_length = 50, help_text = 'Trainer name | length max = 20')
    content = RichTextField()
    trainer_designation = models.CharField(max_length = 100, help_text = 'Trainer designation | length max = 50')


    def _str_(self):
        return f"{self.trainer_name}"
    
def WhyUs_bg_diamension(value):
    img = Image.open(value)
    required_width = 612
    required_height = 408
    if img.width != required_width and img.height != required_height:
        raise ValidationError(f'The image diamensions must be - Width:{required_width}px, height:{required_height}px')

class AboutPage_WhychooseUs(models.Model):

    bg_img = models.ImageField(upload_to= 'aboutpagehead', help_text="About WhyUs bg | width= 612px height= 408px ", 
                                validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg"]), WhyUs_bg_diamension,],)
    
    Column_title1 = models.CharField(max_length = 50, help_text = "Column Title | max_length = 50")
    subtitle1 = models.CharField(max_length = 50, help_text = "Column Title | max_length = 50")
    content1 = models.TextField()
    subtitle2 = models.CharField(max_length = 50, help_text = "Column Title | max_length = 50")
    content2 = models.TextField()
    subtitle3 = models.CharField(max_length = 50, help_text = "Column Title | max_length = 50")
    content3 = models.TextField()
    Column_title2 = models.CharField(max_length = 50, help_text = "Column Title | max_length = 50")
    subtitle4 = models.CharField(max_length = 50, help_text = "Column Title | max_length = 50")
    content4 = models.TextField()
    subtitle5 = models.CharField(max_length = 50, help_text = "Column Title | max_length = 50")
    content5 = models.TextField()
    subtitle6 = models.CharField(max_length = 50, help_text = "Column Title | max_length = 50")
    content6 = models.TextField()

    created_at = models.DateTimeField(auto_now_add = True)

    def _str_(self):
        return f"WhyUs"
    

class ContactForm(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=50)
    message = models.TextField()


    created_at = models.DateTimeField(auto_now_add = True)

class ApplyForm(models.Model):

    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    course = models.CharField(max_length=50)
    message = models.TextField()


    created_at = models.DateTimeField(auto_now_add = True)

class RequestQuoteFm(models.Model):

    name = models.CharField(max_length=30)
    email_id = models.CharField(max_length=100)
    qualification = models.CharField(max_length=500,null=True, default=None)
    phone = models.IntegerField()
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add = True)

