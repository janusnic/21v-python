# -*- coding: utf-8 -*-

class Private:
    def __init__(self, names):
        self.__names = names
        self.__data = {}
    def __getattr__(self, name):
        if name in self.__names:
            return self.__data[name]
        raise AttributeError(name)
    def __setattr__(self, name, value):
        if name.startswith("_Private"):
            self.__dict__[name] = value
            return
        if name in self.__names:
            self.__data[name] = value
            return
        raise TypeError("cannot set the attribute %r" % (name,))

class Person(Private):
    """ Класс person.

    """
    def __init__(self, parent = None):
        Private.__init__(self, ["first_name", "last_name", 'id', "age", 'city', "addr", "parent"])
        self.parent = parent

    def __str__(self):
        return ''.join((self.first_name.lower().title(),' ', self.last_name.lower().title()))
    
    def new_child(self):
        return Person(self)

