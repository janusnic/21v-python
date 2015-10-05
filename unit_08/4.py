# -*- coding: utf-8 -*-

class Person(object):
    """ A simple class representing a person object.

    """
    #initialize name, ID number, city
    def __init__(self, fname, lname, ID, city):
        self.__ID = ID
        self.__first_name  = fname
        self.__last_name  = lname
        self.__city = city

    def _getName(self):
        s = ' '
        return s.join((self.__first_name, self.__last_name))


    #def __format__(self, formatstr):
    #    return formatstr

    def __format__(self, format_spec):
        if isinstance(format_spec, unicode):
            return unicode(str(self))
        else:
            return str(self)

    #display name
    def show_person(self):
        print 'Name', format(self._getName(),'<9')
        print 'ID:', format(self.__ID,'<9')
        print('City:', self.__city)

    def getfName(self):
        fmt = ':>30'
        return format(self.__first_name, fmt)

# Проверка способа запуска модуля

if __name__ == '__main__':
    # Create an person
    john = Person(
        fname='John', lname='Paw', city="NYC", ID=223344
    )
    mary = Person(
        fname='Mary', lname='Sue', city='LA', ID=113344
    )


    print '__format__ объекта Person: '


    print mary.getfName()
    mary.show_person()
