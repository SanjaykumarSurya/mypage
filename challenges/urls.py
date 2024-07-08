          # Author     : Sanjaykumar.M
            # Date       : 04-06-2024
            # Description: Django basic views and urls some example


from django.urls import path

from . import views

urlpatterns = [
    # path("january", views.index),
    # path("february", views.month),
    path("", views.index, name="index"),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.month_challenge, name="month_challenge")
]
