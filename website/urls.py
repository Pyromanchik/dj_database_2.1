from django.contrib import admin
from django.urls import path, include
from school.views import students_list  # ← добавлено: импорт представления
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', students_list, name='students_list'),
    path('__debug__/', include(debug_toolbar.urls)),
]