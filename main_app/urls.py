from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_widget/', views.add_widget,name='add_widget' ),
    path('delete_widget/<int:widget_id>', views.delete_widget, name='delete_widget')
]