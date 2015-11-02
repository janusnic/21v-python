import models

class Accomlist(object):
    def __init__(self):
        resource = models.Model()
        self.accoms = resource.fetchemployee()

    def __str__(self):
        result = ""
        for emp in self.accoms:
            called = emp.getname()
            result += "\n" + called
        return result