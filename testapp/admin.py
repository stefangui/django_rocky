from django.contrib import admin
import testapp.models as tm

admin.site.register(tm.Article)
admin.site.register(tm.Author)
admin.site.register(tm.Tag)

# Register your models here.
