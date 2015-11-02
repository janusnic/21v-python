import sqlite3
import employee 

class Model(object):
    def __init__(self):
        self.conn = sqlite3.connect('staff.db')
        self.result = []
   
    def add_employee(self,row):
        new_emp = employee.Employee(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
        self.result.append(new_emp)

    def make_list(self):
        c = self.conn.cursor()
        c.execute ("select * from employee")
        for row in c:
            self.add_employee(row)
        return self.result

    def fetchemployee(self):
        c = self.conn.cursor()
        c.execute ("select * from employee")
        for row in c:
            self.add_employee(row)
        return self.result

if __name__ == "__main__":
    resource = Model()
    # accoms = resource.fetchemployee()
    accoms = resource.make_list()


    for accom in accoms:
        print (accom.getname(),accom.show_pay())