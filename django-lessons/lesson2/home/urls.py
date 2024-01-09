from django.urls import path
from .views import get_age, get_info, GetInfo, GetAge

urlpatterns = [
    path('', get_info),
    path('age/', get_age),
    path('get-info/', GetInfo.as_view(), name='info'),
    path('get-age/', GetAge.as_view(), name='age'),
]


