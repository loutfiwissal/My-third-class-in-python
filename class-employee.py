class Employee () :
    def __init__( self, name, sales, bonushrs, basesalary):
        self.name=name
        self.sales=sales
        self.bonushrs=bonushrs
        self.basesalary=basesalary
    
    def info(self):
        print("the employee name is {} his sales {}  DH his bonushrs {}  DH and his basesalary {} DH"
              .format(self.name, self.sales, self.bonushrs, self.basesalary))

Em1 = Employee("TAHA", 4000, 50, 2500)

Em1.info()