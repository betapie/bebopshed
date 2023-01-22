import random

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Line

from lily_proc.music_renderer import MusicRenderer


def main(request):
    return HttpResponse('Welcome to bebopshed API')


@api_view(['GET'])
def generate_line(request):
    result = {}
    count = Line.objects.count()
    line = Line.objects.all()[random.randint(0, count-1)]

    renderer = MusicRenderer()
    svg = renderer.render(line.line, line.chords)

    result["line"] = svg
    result["artist"] = line.artist.name
    result["song"] = line.song
    result["year"] = line.year

    return Response(result)
