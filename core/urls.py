from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_tournament/", views.add_tournament, name="add_tournament"),
    path("configure_tournament/<int:tournament_id>/", views.configure_tournament, name="configure_tournament"),
    path("add_team/", views.add_team, name="add_team"),
    path("start_tournament/<int:tournament_id>/", views.start_tournament, name="start_tournament"),
    path("delete_team/", views.delete_team, name="delete_team"),
]