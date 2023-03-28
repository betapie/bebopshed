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
    key_basepitch = request.GET.get("key_basepitch", None)
    key_accidental = request.GET.get("key_accidental", None)
    if key_basepitch:
        key = key_basepitch
        if key_accidental == "flat":
            key += "es"
        elif key_accidental == "sharp":
            key += "is"

        kwargs["transpose_from"] = str(line.key).lower()
        kwargs["transpose_to"] = key.lower()
    else:
        key = str(line.key).lower()
        key_basepitch = key[0]
        acc = key[1:]
        if acc in ["s", "es"]:
            key_accidental = "flat"
        elif acc == "is":
            key_accidental = "sharp"
        else:
            key_accidental = "natural"

    renderer = MusicRenderer()
    svg = renderer.render(line.line, line.chords, **kwargs)

    result["id"] = line.id
    result["line"] = svg
    result["prog_name"] = line.progression.common_name
    result["prog_sequence"] = line.progression.sequence
    result["key_basepitch"] = key_basepitch
    result["key_accidental"] = key_accidental

    return Response(result)
