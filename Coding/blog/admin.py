from django.contrib import admin
from blog.models import Blog, Contact

# Register your models here.

# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'phone', 'desc')

#     def delete_model(self, request, obj):
#         # Call the superclass method to delete the object
#         super().delete_model(request, obj)
#         # Redirect to the contact list view with a message
#         from django.contrib import messages
#         remaining = Contact.objects.count()
#         messages.success(request, f'Successfully deleted. Remaining contacts: {remaining}')



class BlogAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all" : ('css/main.cs',)
        
        }
        js = ('js/blog.js',)
        
admin.site.register(Blog , BlogAdmin)
admin.site.register(Contact )

# admin.site.register(ContactAdmin)