from django.core.management.base import BaseCommand
from api.models import Line
from lily_proc.line_parser import LineParser
from lily_proc.transpose import KeyTransposer
from lily_proc.pitch import Key, BasePitch, Accidental


class Command(BaseCommand):
    help = (
        "Creates the line lily string in the key of C"
        "from the original line in the original key"
    )

    def handle(self, *args, **kwargs):
        target_key = Key(BasePitch.C, Accidental.NATURAL)
        parser = LineParser()
        for line in Line.objects.all():
            # sanitized = parser.sanitize(line.original_line)
            print(f"id: {line.id}")
            line_obj = parser.parse(line.line)
            orig_key = Key.from_lily(str(line.original_key).lower())
            transposer = KeyTransposer(orig_key, target_key)
            transposed_line = transposer.transpose(line_obj)
            line.original_line = line.line
            line.line = transposed_line.to_lily()
            line.save()
