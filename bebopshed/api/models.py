from django.db import models


class Progression(models.Model):
    sequence = models.CharField(max_length=32)
    common_name = models.CharField(max_length=64)

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
    line = models.TextField()
    chords = models.TextField()
    progression = models.ForeignKey(
        Progression, models.SET_NULL, blank=True, null=True)
    key = models.CharField(max_length=3, choices=Key.choices)

    def __str__(self):
        return f"#{self.id}: {self.progression.sequence} in {self.key}"
