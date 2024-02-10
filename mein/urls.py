from django.urls import path
from .views import *
urlpatterns = [
    path('get-banner/', get_banner),
    path('get-proper/', get_proper),
    path('get-about/', get_about),
    path('get-agent1/', get_agent1),
    path('get-agent/', get_agent),
    path('get-agent2/', get_agent2),
    path('get-services/', get_services),
    path('get-testimonial/', get_testimonial),
    path('get-contact/', get_contact),
    path('get-news/', get_news),
]
