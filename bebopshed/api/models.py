from django.db import models


class Instrument(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=64)
    instrument = models.ForeignKey(
        Instrument, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Progression(models.Model):
    sequence = models.CharField(max_length=32)
    common_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.sequence} ({self.common_name})"


class Album(models.Model):
    artist = models.ForeignKey(Artist, models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.artist} - {self.name}"


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
    artist = models.ForeignKey(Artist, models.SET_NULL, blank=True, null=True)
    song = models.CharField(max_length=50, blank=True, null=True)
    album = models.ForeignKey(Album, models.SET_NULL, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.artist} - {self.progression} on {self.song}"
