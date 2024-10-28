import os
from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import StoryPointEntry

def is_fibonacci(n):
    """Check if a number is a Fibonacci number."""
    if n < 0:
        return False
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

class MainPageView(View):
    def get(self, request):
        return render(request, 'homepage.html')

class StoryPointsView(View):
    def get(self, request):
        # If you want to render the form for adding story points by default
        return render(request, 'StoryPoints/storypoints.html')

    def get(self, request):
        # If you want to render the form for adding story points by default
        return render(request, 'StoryPoints/addStoryPoints.html')
    
    def post(self, request):
        username = request.POST.get('username')
        story_points_str = request.POST.get('story_points')

        try:
            story_points = int(story_points_str)
        except (ValueError, TypeError):
            return JsonResponse({"error": "Please enter a valid integer for story points."}, status=400)

        if not is_fibonacci(story_points):
            return JsonResponse({"error": "Please enter story points that are a Fibonacci number."}, status=400)

        file_path =  os.path.join(settings.BASE_DIR,'story_points.txt')
                   
        with open(file_path,'a') as f:
            f.write(f"{username},{story_points}\n")
        return JsonResponse({"success": "Story points recorded successfully."})
    
class ViewStoryPoints(View):
    def get(self, request):
        file_path =  os.path.join(settings.BASE_DIR,'story_points.txt')
        # if(request.method== 'POST'):
        #     username = request.POST.get("username")
        #     story_points = request.POST.get("story_points")

        #     with open(file_path,'a') as f:
        #         f.write(f"{username},{story_points}\n")
        #         return redirect('story_points')  # Redirect to display updated entries
        
        entries= []
        if(os.path.exists(file_path)):
            with open(file_path,'r') as f:
                for line in f:
                    username, story_points = line.strip().split(',')
                    entries.append({"username":username , "story_points":story_points})
        # Fetch all story point entries
        return render(request, 'StoryPoints/viewStoryPoints.html',{'entries': entries})
