from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from student_results.models import User
from django.contrib.auth import get_user_model



User = get_user_model()


class MyUserAdmin(UserAdmin):

    list_display = ('email','username','date_joined', 'last_login', 'is_admin','is_staff')
    search_fields = ('email','username',)
    readonly_fields=('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, UserAdmin)
admin.site.site_header = "Teletex Administration Page"
admin.site.site_title = "Teletex"
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Staff)
admin.site.register(Friend)
admin.site.register(Profile)

admin.site.register(Std1)
admin.site.register(Std2)
admin.site.register(Std3)
admin.site.register(Std4)
admin.site.register(Std5)
admin.site.register(Std6)
admin.site.register(Std7)

admin.site.register(FormOne)
admin.site.register(FormTwo)
admin.site.register(FormThree)
admin.site.register(FormFour)

admin.site.register(FormOneTech)
admin.site.register(FormTwoTech)
admin.site.register(FormThreeTech)
admin.site.register(FormFourTech)

admin.site.register(EGM5)
admin.site.register(PCB5)
admin.site.register(PCM5)
admin.site.register(CBG5)
admin.site.register(PGM5)
admin.site.register(ECA5)
admin.site.register(HGE5)
admin.site.register(HGK5)
admin.site.register(HGL5)
admin.site.register(HKL5)

admin.site.register(EGM6)
admin.site.register(PCB6)
admin.site.register(PCM6)
admin.site.register(CBG6)
admin.site.register(PGM6)
admin.site.register(ECA6)
admin.site.register(HGE6)
admin.site.register(HGK6)
admin.site.register(HGL6)
admin.site.register(HKL6)