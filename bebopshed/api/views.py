import random

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Line

from lily_proc.music_renderer import MusicRenderer


def main(request):
    return HttpResponse('Welcome to bebopshed API')


@api_view(["GET"])
def generate_line(request):
    result = {}
    id = request.GET.get("id", None)
    if id:
        line = Line.objects.get(id=id)
    else:
        count = Line.objects.count()
        line = Line.objects.all()[random.randint(0, count-1)]

    kwargs = {}
    key = request.GET.get("key", None)
    if key:
        kwargs["transpose_from"] = str(line.key).lower()
        kwargs["transpose_to"] = key.lower()
    else:
        key = str(line.key).lower()

    renderer = MusicRenderer()
    svg = renderer.render(line.line, line.chords, **kwargs)

    result["id"] = line.id
    result["line"] = svg
    result["original_key"] = str(line.key).lower()
    result["key"] = key
    result["prog_name"] = line.progression.common_name
    result["prog_sequence"] = line.progression.sequence

    return Response(result)
