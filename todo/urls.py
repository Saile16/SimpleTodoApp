from django.urls import path
from .views import (
    todo_list,
    todo_detail,
    todo_create,
    todo_update,
    todo_delete
)
# esto de poner app_name es raro aun no sabemos porque pero esta usando
# namespace en urltotal
app_name = 'todos'
urlpatterns = [
    path('', todo_list),
    path('create/', todo_create),
    path('<id>/', todo_detail),
    path('<id>/update/', todo_update),
    path('<id>/delete/', todo_delete),

]
