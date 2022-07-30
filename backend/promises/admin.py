from django.contrib import admin

from .models import Promise, Document

admin.site.register(Promise)
admin.site.register(Document)