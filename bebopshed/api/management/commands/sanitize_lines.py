from django.core.management.base import BaseCommand

from api.models import Line
from lily_proc.line_parser import LineParser


class Command(BaseCommand):
    help = "TODO"

    def handle(self, *args, **kwargs):
        parser = LineParser()
        for line in Line.objects.all():
            print(f"Sanitized {line}")
            line.line = parser.sanitize(line.line)
            line.save()
