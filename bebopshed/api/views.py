import random

from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Line

from lily_proc.music_rng import KeyRng
from lily_proc.music_renderer import MusicRenderer


def main(request):
    return HttpResponse("Welcome to bebopshed API")


@api_view(["GET"])
def generate_line(request):
    result = {}
    id = request.GET.get("id", None)
    if not id:
        ids = Line.objects.filter(to_review=False).values_list("id")
        if not ids:
            return HttpResponseBadRequest("No line with for query")
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
            rand_key = KeyRng.getMinorKey()
        else:
            rand_key = KeyRng.getMajorKey()
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

    kwargs = {"mode": str(line.progression.mode).lower()}
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
