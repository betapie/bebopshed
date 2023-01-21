import random

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Line

from music_renderer.music_renderer import MusicRenderer


def main(request):
    return HttpResponse('Welcome to bebopshed API')


@api_view(['GET'])
def generate_line_fallback(request):
    result = {}

    with open("music_renderer/examples/remember1.svg", 'r') as svg_file:
        content = svg_file.read()
        result["line"] = content
        result["artist"] = "Wynton Kelly"
        result["song"] = "Remember"
    return Response(result)


@api_view(['GET'])
def generate_line(request):
    result = {}
    count = Line.objects.count()
    line = Line.objects.all()[random.randint(0, count-1)]

    renderer = MusicRenderer()
    renderer.render(line.line, line.chords)

    with open("tmp/tmp.svg", 'r') as svg_file:
        content = svg_file.read()
        result["line"] = content

    result["artist"] = line.artist.name
    result["song"] = line.song
    result["year"] = line.year

    return Response(result)
