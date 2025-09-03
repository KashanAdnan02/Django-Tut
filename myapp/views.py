from django.shortcuts import render
## The App Items will Show When you will connect it to the templates bcs we are 
## using files of HTML Sos connect the templates folder  
def index(req):
    return render(req,"index.html")

def about(req):
    return render(req,"about.html")

def contact(req):
    return render(req,"contact.html")
