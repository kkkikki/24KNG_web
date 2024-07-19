from django.shortcuts import render
from .models import Video

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'stream/video_list.html', {'videos': videos})

def video_player(request, video_id):
    video = Video.objects.get(pk=video_id)
    return render(request, 'stream/video_player.html', {'video': video})
# Create your views here.
