# -*- coding: utf-8 -*-

import re
_places_re = re.compile(r"\.(\d+)")

default_places = 0

class FixNum:
    def __init__(self, value, places = None):
        self.value = value
        if places is None:
            # get from the value
            m = _places_re.search(str(value))
            if m:
                places = int(m.group(1))
            else:
                places = default_places
        self.places = places

    def __add__(self, other):
        return FixNum(self.value + other.value,
                      max(self.places, other.places))

    def __mul__(self, other):
        return FixNum(self.value * other.value,
                      max(self.places, other.places))

    def __div__(self, other):
        # Force to use floating point, since 2/3 in Python is 0
        # Don't use float() since that will convert strings
        return FixNum((self.value+0.0) / other.value,
                      max(self.places, other.places))

    def __str__(self):
        return "STR%s: %.*f" % (self.__class__.__name__,
                                self.places, self.value)
    def __int__(self):
        return int(self.value)

    def __float__(self):
        return self.value

def demo():
    x = FixNum(40)
    y = FixNum(12, 0)

    print "sum of", x, "and", y, "is", x+y
    print "product of", x, "and", y, "is", x*y

    z = x/y
    print "%s has %d places" % (z, z.places)
    if not z.places:
        z.places = 2

    print "div of", x, "by", y, "is", z
    print "square of that is ", z*z

if __name__ == "__main__":
    demo()
