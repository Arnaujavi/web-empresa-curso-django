from django.urls import path
from .views import ListViewProfiles, DetailViewProfiles

profilesPatterns = ([
    path('', ListViewProfiles.as_view(), name='listView'),
    path('<username>', DetailViewProfiles.as_view(), name='detailView'),

], "profiles") #Creando esta tupla puedo acceder a la app como nombreApp:vistas `por ejemplo--> profiles:listView`
