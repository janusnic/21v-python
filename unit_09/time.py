# -*- coding: utf-8 -*-

class TimeNumber:
    def __init__(self, hours, minutes, seconds):
        assert minutes < 60 and seconds < 60
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def __str__(self):
        return "%d:%02d:%02d" % (self.hours, self.minutes, self.seconds)
    def __add__(self, other):
        seconds = self.seconds + other.seconds
        minutes = self.minutes + other.minutes
        hours = self.hours + other.hours
        if seconds >= 60:
            seconds %= 60
            minutes += 1
        if minutes >= 60:
            minutes %= 60
            hours += 1
        return TimeNumber(hours, minutes, seconds)

    def __sub__(self, other):
        raise NotImplementedError

    def __mul__(self, other):
        raise NotImplementedError

    def __div__(self, other):
        raise NotImplementedError

t1 = TimeNumber(0, 58, 59)
sec = TimeNumber(0, 0, 1)
min = TimeNumber(0, 1, 0)
print t1 + sec + min + min
# 1:01:00
