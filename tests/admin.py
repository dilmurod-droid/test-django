from django.contrib import admin

from tests.models import Test, Question, Answer

admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)