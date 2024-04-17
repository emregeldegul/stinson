from django.contrib import admin

from merchant.models import Application, Channel


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('token', 'first_name', 'last_name', 'created_at', 'updated_at')
    
    
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('application', 'website_url')
    
    @admin.display(empty_value="???")
    def application(self, obj):
        return obj.application.token
    
    
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Channel, ChannelAdmin)