from django.shortcuts import render, get_object_or_404
from .models import Video

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'stream/video_list.html', {'videos': videos})

def video_player(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    return render(request, 'stream/video_player.html', {'video': video})
