from .music_object import Rest, Break
from .duration import Duration, CommonDuration
from .bar import Bar


class Line:
    def __init__(self, bars: list):
        self._bars = bars

    def to_lily(self):
        result = ""
        for idx, bar in enumerate(self._bars[:-1]):
            if (idx + 1) % 4 == 0:
                result += bar.to_lily() + Break().to_lily() + '\n'
            else:
                result += bar.to_lily() + '\n'
        result += self._bars[-1].to_lily()
        return result

    def pad(self):
        power = 1
        while power < len(self._bars):
            power *= 2
        to_append = power - len(self._bars)
        for _ in range(to_append):
            self._bars.append(
                Bar([Rest(Duration(CommonDuration.WHOLE))])
            )
