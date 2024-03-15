from django.shortcuts import render,HttpResponse, redirect
from .models import Product, Category,SignUp
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.contrib.auth.models import User
# from store.customer import isExists
# Create your views here.
# view for index page

def index(request):
    product=Product.objects.all()
    
   #  it will show categories as ascending orders
   #  category=Category.objects.all().order_by('category_name')
    
   #  it will show categories as descending orders
   #  category=Category.objects.all().order_by('-category_name')
    
   #  it will show categories as default order through that it is stored

   # it will show limited categories that we can limit according to our desire. here we shoe on three categories want to show  
   #  category=Category.objects.all().order_by('-category_name')[:3]
   #  it is slicing
   #  category=Category.objects.all().order_by('-category_name')[1:6:2]
   #  a view that fetch all products from Product tabel of sepecific category which was selected based on its category id
   #  def cattegoryy(request,id)
      # product=Product.objects.all()
    
    category=Category.objects.all().order_by('category_name')
   #  just display category id
    print("here is category id is :", request.GET.get("category"))
   #  give us category wise products
    categoryID=request.GET.get('category')
    if categoryID:
       product =Product.objects.filter(category=categoryID)
       print("gvzjxdgcs")
    else:
       print("elssss") 
       product=Product.objects.all()
    data={'product':product,'category':category}
    return render(request,'store/index.html',data)
    
   # views for signup...
def signup(request):
   if request.method == 'POST':
      first_name = request.POST.get('first_name')
      last_name = request.POST.get('last_name')  # Use an empty string as a default if last_name is not provide
      phone_number = request.POST.get('phone_number')
      email = request.POST.get('email')
      password = request.POST.get('password')
   #   form fields validations
      error_message=None
      if (not first_name):
         error_message="First Name is required"
      elif len(first_name)<4:
         error_message="First Name character must be 4 long"
   #   elif (not last_name):
   #      error_message="Last name is required"
   #   elif len(last_name)<4:
   #      error_message="last_name character length should be 4 character"
         
      elif (not phone_number):
         error_message="phone number is required"
      elif len(phone_number)<11:
         error_message="phone must be 11 characters"
      elif (not password):
         error_message="password is  required"
      elif len(password)<5:
         error_message="pasword must be 5 characters"
      #   adding email validation
      #   def isExists(self):
      elif SignUp.objects.filter(email=email):
         error_message = "Email Already Exist"
      #     return True
      #   return False
   #   elif (not .isExists):
   #      error_message="Email is Already Exist"
         
   #   saved object.
      if not error_message:
         # password hashing "to secure our password fom everyone evenif admin"
         password=make_password(password)
         signup_instance = User(username="root1", first_name=first_name, last_name=last_name, email=email, password=password)
         signup_instance.save()
      # To display success message when  signup form is successfully submitted
      # return HttpResponse("Signup successful!")
      # When form is successfully submitted control goes to home or index page we will use that scripts
      # when you want if user sucessfully submitt  form user redirect to the product home page

         return redirect("home")
      # when you want if user sucessfully submitt  form user redirect and show message "Hello,Your For is Submitted"

         # return HttpResponse("Hello,Your For is Submitted")
      else:
         return render(request,'store/signup.html',{'error':error_message})

   return render(request, 'store/signup.html')
    

   #  view for login page

        
        # Check if both email and password are provided
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
      #   print(email,password)
        # Check if both email and password are provided
      #   error_message=None
      #   if not email or not password:
      #       error_message = "Please enter both email and password"
      #       return render(request, 'store/login.html', {'error':error_message})
            
        # Use Django's authenticate function to check credentials
        user = authenticate(request, username=username, password=password)
        print("here is line no 117", user)

        if user is not None:
            # Authentication successful, log in the user
            print("here is line no 121")
            login(request, user)
            return redirect("home")
        else:
            # print(email,password)
            error_message = "Invalid email or password"
            return render(request, 'store/login.html', {'error':error_message})
            

    elif request.method == 'GET':
        error_message="djsadlfasdf"
        print(error_message)
        return render(request, 'store/login.html', {'error':error_message})

    # Handle other HTTP methods if necessary
   #  return render(request, 'store/login.html')
# ----------------------------------------------------
    
# def login(request):
#    if request.method=='GET':
#      return render(request, 'store/login.html')
#    else:
#      emails=request.POST.get('email')
#      passwords=request.POST.get('password')
#      password=SignUp.objects.filter(password)
#      email=SignUp.objects.filter(email)
#      error_message=None
#      if not password:
#          error_message="please Enter Password"
#      else:
#          flag=check_password(passwords, SignUp.password)
#          if flag:
#             return render("home")
#          else:
#             # return redirect("Your password is incorrect")
#             error_message="Your password is incorrect"

#    #   password=password=check_password(password)
#    #   print(email,password)
#    #   customer=customer_email(email)
#    #   if customer:
#    #      pass
#    #   else:
#    #      pass
#    #   print(email,password)
#      return render(request,'store/login.html')
   # QuerySet and QuerySet api ............
def Query_Set(request,course):
   # you can also use ascending or descending based on it's modeli's id
   # categorly=Category.objects.all().order_by('?')
   # categorly=Category.objects.all().order_by('-category_name')
   # categorly=Category.objects.all().order_by('category_name')
   # to get specific values use filter and lookups
   # categorly=Category.objects.filter(id=7)
   # categorly=Category.objects.filter(category_name='mouse')
   # categorly=Category.objects.filter(category_name='mouse')
   # exclude 
   # categorly=Category.objects.exclude(category_name='mouse')
   # print("sql qury:",categorly)
   # SQL SELECT "store_category"."id", "store_category"."category_name" FROM "store_category" WHERE NOT ("store_category"."id" = 7)
   # categorly=Category.objects.exclude(id=7)
   # reverse
   # categorly=Category.objects.all().order_by('id').reverse()[:5]
   # SQL SELECT "store_category"."id", "store_category"."category_name" FROM "store_category" ORDER BY "store_category"."id" DESC LIMIT 5
   # categorly=Category.objects.all().order_by('-id')[:5]
   # SQL SELECT "store_category"."id", "store_category"."category_name" FROM "store_category" ORDER BY "store_category"."id" DESC LIMIT 5
   # values show data in the form of dictionery
   # values scenarios
   # if we want to show all list values inside model in the form of list(dictionery) so below syntax will be us
   # categorly=Category.objects.values()
   # and if we want just show category name inside from list dictionery then below method will be used
   # categorly=Category.objects.values('category_name')
   # values_list() it display data in the form of tup
   # categorly=Category.objects.values_list('category_name',named=True)
   # categorly=Category.objects.values_list(named=True)
   # it return empty queryset
   # categorly=Category.objects.none()
   # doing union on catgory and product model and fetch data based on union and combine both model's record
   # product=Product.objects.values_list('id',named=True)
   # categorly=Category.objects.values_list('id',named=True)
   # categorly=product.union(categorly)
   # print('SQL',categorly.query)
   # in case you want to show all duplicate data then
   # product=Product.objects.values_list('id', named=True)
   # categorly=Category.objects.values_list('id', named=True)
   # categorly=product.union(categorly,all=True)
   # print('SQL',categorly.query)
   # intersection
   # product=Product.objects.values_list('id', named=True)
   # categorly=Category.objects.values_list('id', named=True)
   # categorly=product.intersection(categorly)
   # print('SQL',categorly.query)
   # differnce of two sets
   # product=Product.objects.values_list('id', named=True)
   # categorly=Category.objects.values_list('id', named=True)
   # categorly=categorly.difference(product)
   # Operations that returns Django QuerySet
   # categorly=Category.objects.filter(id=8) & Category.objects.filter(category_name='sheep')
   # categorly=Category.objects.filter(id=8) or Category.objects.filter(category_name='sheep')
   #  we also use this short method to do same
   # categorly=Category.objects.filter(id=7,category_name='sheep') 
   # we are achieve that through Q object
   # categorly=Category.objects.filter(Q(id=7) & Q(category_name="sheep"))
   categorly=Category.objects.filter(Q(id=7) | Q(category_name="sheep"))
   print('SQL',categorly.query)
   return render(request,"store/queryset.html",{'category':categorly})
   
    
   #   #  view for makepassword and checkpassword
   #  p1=make_password('2345324')
   #  print(p1)
   #  p2=check_password('2345324', p1)
   #  print(p2)
# def signup(request):
#    if request.method=='GET':
#       frist_name=request.POST.get("frist_name")
#       last_name=request.POST.get("last_name")
#       phone_number=request.POST.get("phone_number")
#       email=request.POST.get("email")
#       password=request.POST.get("password")
      
#       return render(request,'store/signup.html')
     
      
#    else:
#       signups = SignUp(frist_name=frist_name,last_name=last_name,phone_number=phone_number,email=email,password=password)
#       signups.save()
#       return HttpResponse("Successfully Submitted")

      # validation
      # error_message=""
      # if not frist_name:
      #    print("here is line no 32")
      #    error_message="first name is requied"
      # elif len(frist_name)>4:
      #    print("here is line no 34")
      #    error_message="first name must be 4 character"
      # elif not last_name:
      #    print("here is line no 36")
      #    error_message="last name is required"
      # elif len(last_name)>4:
      #    print("here is line no 38")
      #    error_message="last name must be 4 character"
      # if not error_message:
      #    print("here is line no 40")
      #    signups = SignUp(frist_name=frist_name,last_name=last_name,phone_number=phone_number,email=email,password=password)
      #    signups.save()
      #    return HttpResponse("Form Sucessfully Submitted to Server")
      # else:
      #    print("here is line no 49")
      #    return render(request,'store/signup.html')
   # if request.method=='GET':
   #       return render(request,'store/signup.html')