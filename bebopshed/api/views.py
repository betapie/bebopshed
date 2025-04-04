import random

from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response

from lily_proc.music_renderer import MusicRenderer
from lily_proc.random import RandomKeyGenerator

from .models import Line, Progression


def main(request):
    return HttpResponse("Welcome to bebopshed API")


@api_view(["GET"])
def generate_line(request):
    result = {}
    id = request.GET.get("id", None)
    if not id:
        progression_id = request.GET.get("progression_id", None)
        filtered_lines = Line.objects.filter(to_review=False)
        if progression_id:
            filtered_lines = filtered_lines.filter(progression_id=progression_id)
        ids = filtered_lines.values_list("id")
        if not ids:
            return HttpResponseBadRequest("No line with queried parameters exists")
        id = random.choice(ids)[0]
    try:
        line = Line.objects.get(id=id)
    except Line.DoesNotExist:
        return HttpResponseBadRequest(f"No line with id {id}")

    kwargs = {}
    key_basepitch = request.GET.get("key_basepitch", None)
    key_accidental = request.GET.get("key_accidental", None)
    if key_basepitch:
        key = key_basepitch
        if key_accidental == "flat":
            key += "es"
        elif key_accidental == "sharp":
            key += "is"
    else:
        if str(line.progression.mode).lower() == "minor":
            rand_key = RandomKeyGenerator.minorKey()
        else:
            rand_key = RandomKeyGenerator.majorKey()
        key = rand_key.to_lily()
        key_basepitch = key[0]
        acc = key[1:]
        if acc in ["s", "es"]:
            key_accidental = "flat"
        elif acc == "is":
            key_accidental = "sharp"
        else:
            key_accidental = "natural"

    kwargs["transpose"] = {
        "orig_key": "c",
        "target_key": key.lower(),
    }

    renderer = MusicRenderer()
    svg = renderer.render(line.line, line.progression.chords, **kwargs)

    result["id"] = line.id
    result["line"] = svg
    result["prog_name"] = line.progression.common_name
    result["prog_sequence"] = line.progression.sequence
    result["key_basepitch"] = key_basepitch
    result["key_accidental"] = key_accidental

    return Response(result)


@api_view(["GET"])
def generate_chops_build(request):
    result = {}
    id = request.GET.get("id", None)
    if not id:
        return HttpResponseBadRequest("Required parameter 'id' missing")
    try:
        line = Line.objects.get(id=id)
    except Line.DoesNotExist:
        return HttpResponseBadRequest(f"No line with id {id}")

    kwargs = {}
    key_basepitch = request.GET.get("key_basepitch", "c")
    key_accidental = request.GET.get("key_accidental", "")
    key = key_basepitch
    if key_accidental == "flat":
        key += "es"
    elif key_accidental == "sharp":
        key += "is"
    delta = request.GET.get("delta_key", "-2")

    chops_builder_params = {
        "orig_key": "c",
        "start_key": key,
        "delta": delta,
        "mode": str(line.progression.mode).lower(),
    }
    kwargs["chops_builder"] = chops_builder_params

    renderer = MusicRenderer()
    svg = renderer.render(line.line, line.progression.chords, **kwargs)

    result["id"] = line.id
    result["line"] = svg
    result["prog_name"] = line.progression.common_name
    result["prog_sequence"] = line.progression.sequence
    result["key_basepitch"] = key_basepitch
    result["key_accidental"] = key_accidental

    return Response(result)


@api_view(["GET"])
def render_line(request):
    result = {}
    lily_line = request.GET.get("lily_line", None)
    if not lily_line:
        return HttpResponseBadRequest("Required parameter 'lily_line' missing")
    lily_chords = request.GET.get("lily_chords", None)
    if not lily_chords:
        return HttpResponseBadRequest("Required parameter 'lily_chords' missing")

    renderer = MusicRenderer()
    svg = renderer.render(lily_line, lily_chords)

    result["lily_line"] = lily_line
    result["lily_chords"] = lily_chords
    result["line"] = svg
    return Response(result)


@api_view(["GET"])
def get_progessions(request):
    result = {}
    progs = []
    for prog in Progression.objects.all().order_by("id"):
        progs.append(
            {
                "id": prog.id,
                "sequence": prog.sequence,
                "common_name": prog.common_name,
            }
        )
    result["progressions"] = progs
    return Response(result)
