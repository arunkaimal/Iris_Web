from django.db import models


class Images(models.Model):
    image = models.ImageField(upload_to="images/")


class Lifestyle_Wedding(models.Model):
    life_wed_image = models.ImageField(upload_to="life_wed_images/")


class Products(models.Model):
    product_image = models.ImageField(upload_to="product_images/")


class Sports(models.Model):
    sport_image = models.ImageField(upload_to="sport_images/")


class Multi_Cam(models.Model):
    multicam_image = models.ImageField(upload_to="multicam_image")


class Client_Logo(models.Model):
    client_logo = models.ImageField(upload_to="client_logos")
