from django.db import models
from ckeditor.fields import RichTextField
from PIL import Image
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.utils.text import slugify

# Create your models here.

# Home Page models 

def NITD_Logo_diamension(value):
    img = Image.open(value)
    required_width = 250
    required_height = 80
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
    
def Main_Blog_img_diamension(value):
    img = Image.open(value)
    required_width = 1000
    required_height = 667
    if img.width != required_width and img.height != required_height:
        raise ValidationError(f'The image diamensions must be - Width:{required_width}px, height:{required_height}px')
    
def Blog_internal_img_diamension(value):
    img = Image.open(value)
    required_width = 2000
    required_height = 1335
    if img.width != required_width and img.height != required_height:
        raise ValidationError(f'The image diamensions must be - Width:{required_width}px, height:{required_height}px')
    
def Author_img_diamension(value):
    img = Image.open(value)
    required_width = 800
    required_height = 850
    if img.width != required_width and img.height != required_height:
        raise ValidationError(f'The image diamensions must be - Width:{required_width}px, height:{required_height}px')

class BlogPage_blog(models.Model):

    main_image = models.ImageField(upload_to= 'blog_main_Image', help_text="Blog main image | width= 1000px height= 667px ", 
                                validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg"]), Main_Blog_img_diamension,],)
    post_date = RichTextField()
    post_by = models.CharField(max_length = 30, help_text = "Name of posted by | max_length = 30")
    author_image = models.ImageField(upload_to= 'author_image', help_text=" Author image | width = 800px height = 850px ",
                                   validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg"]), Author_img_diamension,], null = True)
    author_description = models.CharField(max_length = 1000, help_text = "Author's description | max_length = 1000", default="null")
    blog_title = models.CharField(max_length = 100, help_text = "Blog title | max_length = 100")
    blog_internal_img1 = models.ImageField(upload_to= 'blog_internal_Image', help_text="Blog internal image | width= 2000px height= 1335px ", 
                                validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg"]), Blog_internal_img_diamension,],)
    blog_content1 = RichTextField()
    blog_internal_img2 = models.ImageField(upload_to= 'blog_internal_Image', help_text="Blog internal image | width= 2000px height= 1335px ", 
                                validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg"]), Blog_internal_img_diamension,],)
    blog_content2 = RichTextField()
    comment_count = models.IntegerField()
    slug = models.SlugField(unique=True, null = True, blank = True)

    def save(self, *args, **kwargs):
        #generating unique slug if not given
        if not self.slug:
            self.slug = slugify(self.blog_title)
            #ensure slug is unique
            original_slug = self.slug
            count = 1
            while BlogPage_blog.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{count}"
                count += 1
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.blog_title} - {self.post_by}"
    

class BlogComment(models.Model):

    relation = models.ForeignKey(BlogPage_blog, on_delete = models.CASCADE, related_name = 'comments')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    phone = models.IntegerField(null = True, blank = True)
    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self) ->str:
        return f'Comment for {self.relation}'