from django.urls import path
from dinofacts import views
from dinofacts.views import show_dino
urlpatterns = [
    path('', views.dinofacts, name='show_dino'),
    path("show_dino/<str:name>/", show_dino),
    

]
