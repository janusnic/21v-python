# Employee
class Employee(object):
    def __init__(self,emp_id,sex,city_id,dep_id,first_name,last_name,address,id,base_pay,shift,hours,title,updatedon):
        self.info = {}
        self.info["emp_id"] = emp_id
        self.info["city_id"] = city_id
        self.info["dep_id"] = dep_id
        self.info["first_name"] = first_name
        self.info["last_name"] = last_name
        self.info["address"] = address
        self.info["id"] = id
        self.info["base_pay"] = base_pay
        self.info["shift"] = shift
        self.info["hours"] = hours
        self.info["updatedon"] = updatedon
        self.info["title"] = title
        self.info["sex"] = sex

        self.SHIFT_2 = 0.05
        self.SHIFT_3 = 0.10
    
    
    def getname(self):
        return self.info["first_name"]+' '+self.info["last_name"]
    
    def show_pay(self):
        if self.info["shift"] == 1:
            return (self.info["base_pay"]*self.info["hours"])
        elif self.info["shift"] == 2:
            return  (self.info["base_pay"] * self.SHIFT_2 + self.info["base_pay"])*self.info["hours"]
        elif self.info["shift"] == 3:
            return (self.info["base_pay"] * self.SHIFT_3 + self.info["base_pay"])*self.info["hours"]


if __name__ == "__main__":
        
    manor = Employee(2,2,1,"Manor","Well","Chesterton Road",80.00,5.,1,8)
    antonia = Employee(1,2,1,"Antonia", "Hourse","Shaw Country Road",45.00,2.,1,12)
    shaw = Employee(1,2,1,"Shaw", "Carry","Antonia Road",44.00,22.,3,6)

    emps = (manor, antonia, shaw)
    for emp in emps:
        print emp.getname(), emp.show_pay()
