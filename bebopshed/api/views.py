# from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


def main(request):
    return HttpResponse('Welcome to bebopshed API')


@api_view(['GET'])
def generate_line(request):
    result = {}
    with open("music_renderer/examples/remember1.svg", 'r') as svg_file:
        content = svg_file.read()
        result["line"] = content
        result["artist"] = "Wynton Kelly"
        result["song"] = "Remember"
    return Response(result)
