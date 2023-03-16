from fractions import Fraction


class Duration:
    def __init__(self, base_duration: Fraction, dots=0):
        self.base_duration = base_duration
        self.dots = dots
