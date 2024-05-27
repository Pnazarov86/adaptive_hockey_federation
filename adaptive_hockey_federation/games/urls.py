from django.urls import include, path
from games import views

app_name = "games"

games_urlpattern = [
    path("", views.GamesListView.as_view(), name="games"),
]

urlpatterns = [
    path("games/", include(games_urlpattern)),
]