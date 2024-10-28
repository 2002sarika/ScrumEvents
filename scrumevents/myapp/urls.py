# scrumevents/urls.py
from django.urls import path
from .views import MainPageView,StoryPointsView,ViewStoryPoints# Import your view

urlpatterns = [
    path('', MainPageView.as_view(), name='home'),  # Define the home view for the root URL
    path('story-points/', StoryPointsView.as_view(), name='story_points'),
    path('add-story-points/',StoryPointsView.as_view(),name="add-story-points"),
    path('view-story-points/',ViewStoryPoints.as_view(),name="view-story-points"),
]
