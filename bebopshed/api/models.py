from django.db import models


class Progression(models.Model):
    class Mode(models.TextChoices):
        MAJOR = "Major"
        MINOR = "Minor"

    sequence = models.CharField(max_length=32)
    common_name = models.CharField(max_length=64)
    chords = models.TextField()
    mode = models.CharField(max_length=16, choices=Mode.choices)

    def __str__(self):
        return f"{self.sequence} ({self.common_name})"


class Line(models.Model):
    # using lilypond nomenclature
    class Key(models.TextChoices):
        C = "C", "c"
        C_sharp = "CIS", "cis"
        D_flat = "DES", "des"
        D = "D", "d"
        D_sharp = "DIS", "dis"
        E_flat = "ES", "es"
        E = "E", "e"
        F = "F", "f"
        F_sharp = "FIS", "fis"
        G_flat = "GES", "ges"
        G = "G", "g"
        G_sharp = "GIS", "gis"
        A_flat = "AS", "as"
        A = "A", "a"
        B_flat = "BES", "bes"
        B = "B", "b"

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    original_line = models.TextField()
    line = models.TextField()
    progression = models.ForeignKey(
        Progression, models.SET_NULL, blank=True, null=True
    )
    original_key = models.CharField(max_length=3, choices=Key.choices)
    to_review = models.BooleanField(default=True)

    def __str__(self):
        return (
            f"#{self.id}: {self.progression.sequence} in {self.original_key}"
        )
