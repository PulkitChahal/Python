from django.contrib import admin
from testApp.models import HyderabadJobs, BangloreJobs, PuneJobs, NoidaJobs


# Register your models here.
class HyderabadJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phone_number']


class BangloreJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phone_number']


class PuneJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phone_number']


class NoidaJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phone_number']


admin.site.register(HyderabadJobs, HyderabadJobsAdmin)
admin.site.register(BangloreJobs, BangloreJobsAdmin)
admin.site.register(PuneJobs, PuneJobsAdmin)
admin.site.register(NoidaJobs, NoidaJobsAdmin)
