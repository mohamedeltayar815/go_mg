from django.contrib import admin

# Register your models here.
from accounts.models import Customer, maqal,  vphoto,  visit, massage,Link, frist, scond, third, fourth
from embed_video.admin import AdminVideoMixin
from .models import vItem

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(vItem, MyModelAdmin)
admin.site.register(Customer)
admin.site.register(maqal)
admin.site.register(visit)
admin.site.register(vphoto)
admin.site.register(Link)
admin.site.register(massage)
admin.site.register(frist)
admin.site.register(scond)
admin.site.register(third)
admin.site.register(fourth)
