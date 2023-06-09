from django.urls import path
# Импортируем созданное нами представление
from .views import PostMany, CategoryMany, PostAlone


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   # path('<int:pk>', PostOne.as_view()),
   path('', PostMany.as_view()),
   path('', CategoryMany.as_view()),
   path('<int:pk>', PostAlone.as_view())

]
