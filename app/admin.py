from django.contrib import admin
from .models import About,Faq,Teacher,Course,Event, Opinion

admin.site.register([About,Faq,Teacher,Course,Event, Opinion])