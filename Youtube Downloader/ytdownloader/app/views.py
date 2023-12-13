from django.views.generic import View
from django.shortcuts import render, redirect
from pytube import *

class home(View):
    def __init__(self, url=None):
        self.url = url

    def get(self, request):
        return render(request, 'app/home.html')

    def post(self, request):
        fetching_video = False
        fetch_button_text = "Fetch Video"

        # for fetching the video
        if request.POST.get('fetch-vid'):
            self.url = request.POST.get('given_url')
            fetching_video = True
            fetch_button_text = "Please wait..."
            try:
                video = YouTube(self.url)
                vidTitle, vidThumbnail = video.title, video.thumbnail_url
                qual, stream = [], []
                for vid in video.streams.filter(progressive=True):
                    qual.append(vid.resolution)
                    stream.append(vid)
                context = {'vidTitle': vidTitle, 'vidThumbnail': vidThumbnail,
                           'qual': qual, 'stream': stream,
                           'url': self.url, 'fetching_video': fetching_video,
                           'fetch_button_text': fetch_button_text}
                return render(request, 'app/home.html', context)
            except Exception as e:
                # Handle fetch failure
                print(f"Fetch failed: {e}")
                fetching_video = False

        # for downloading the video
        elif request.POST.get('download-vid'):
            self.url = request.POST.get('given_url')
            video = YouTube(self.url)
            stream = [x for x in video.streams.filter(progressive=True)]
            video_qual = video.streams[int(request.POST.get('download-vid')) - 1]
            
            try:
                # Attempt to download the video
                video_qual.download(output_path='../../Downloads')
                download_success = True
            except Exception as e:
                # Handle download failure
                print(f"Download failed: {e}")
                download_success = False

            context = {'download_success': download_success}
            return render(request, 'app/home.html', context)

        context = {'fetching_video': fetching_video, 'fetch_button_text': fetch_button_text}
        return render(request, 'app/home.html', context)
