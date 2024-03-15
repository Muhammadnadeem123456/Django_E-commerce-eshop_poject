from django.db import models

# Create your models here.
# Category model
class Category(models.Model):
   category_name=models.CharField(max_length=50)
   def __str__(self):
       return self.category_name
   class Meta:
       verbose_name_plural='Category'


class Size(models.Model):
    sizes=models.CharField(max_length=20)
    def __str__(self):
       return self.sizes
   
# Product model
class Product(models.Model):
    product_name=models.CharField(max_length=70)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_price=models.IntegerField(default=0)
    product_detail=models.CharField(max_length=150)
    product_image=models.ImageField(upload_to='Product_images/')
    available_sizes = models.ManyToManyField(Size, blank=True, related_name="size")
    class Meta:
     verbose_name_plural='Product'
    def __str__(self):
        return self.product_name
    
# size quantity..
    
    
# creating model for our signup form
class SignUp(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=512)

    class Meta: 
        verbose_name_plural = 'Sign_Up'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
#    def isExists(self, email):
#        if SignUp.objects.filter(email=email):
#         return True
#        return False
#    @staticmethod
#    def customer_email(email):
#        return SignUp.objects.get(email=email)
   
#    for matching new entered email with existing email we we will write that function and add it to the form  validation of that email validation
#    let us fetch compate email from SingUp table
   
