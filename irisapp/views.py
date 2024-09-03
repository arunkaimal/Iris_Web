from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail


def index(request):
    multicam_images = Multi_Cam.objects.all()
    client_logos = Client_Logo.objects.all()
    data = {
        'multicam_image':multicam_images,
        'client_logo':client_logos
    }
    return render(request, "index.html",data)



def about(request):
    if request.method == "POST":
        name = request.POST.get("name")
        from_email = request.POST.get("from_email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        data = {
            "name": name,
            "from_email": from_email,
            "subject": subject,
            "message": message,
        }
        message = """
        Name: {}

        New Message: {}

        From: {}
        """.format(
            data["name"], data["message"], data["from_email"]
        )
        send_mail(data["subject"], message, "", ["irismediaproductionsuae@gmail.com"])
        success_msg = "Your Message Sent Successfully, We Will Contact You Shortly"
        return render(request, "about.html", {"success_msg": success_msg})
    return render(request, "about.html")


def gallery(request):
    image = Images.objects.all()
    return render(request, "gallery.html", {"image": image})


def others(request):
    life_wed_img = Lifestyle_Wedding.objects.all()
    product_img = Products.objects.all()
    sport_img = Sports.objects.all()
    context = {
        "life_wed_img": life_wed_img,
        "product_img": product_img,
        "sport_img": sport_img,
    }

    return render(request, "others.html", context)
