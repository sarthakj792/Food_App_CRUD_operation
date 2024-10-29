from django.urls import path
from food import views


urlpatterns = [
    path("",views.welcome,name="welcome"),
    path("create/",views.create, name = "create"),
    path('accept/',views.accept,name="accept"),
    path('edit/<int:item_id>/',views.edit,name="edit"),
    path("edited/<int:item_id>/",views.update,name="update"),
    path('delete/<int:item_id>/', views.delete,name="delete"),
]