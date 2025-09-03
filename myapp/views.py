from django.shortcuts import render
from myapp.models import Register
## The App Items will Show When you will connect it to the templates bcs we are 
## using files of HTML Sos connect the templates folder  
def index(req):
    return render(req,"index.html")

def about(req):
    return render(req,"about.html")

def contact(req):
    return render(req,"contact.html")

def register(req):    
    if req.method == "POST":
        name = req.POST.get("name")
        email = req.POST.get("email")
        phone = req.POST.get("phone")
        password = req.POST.get("password")
        register = Register(name = name, email = email, phone=phone, password=password)
        register.save()
    return render(req,"register.html")