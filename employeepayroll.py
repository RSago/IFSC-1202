class Employee:
    def_init_(self, firstName, lastName, idNumber, hours, wage)
    self.firstName = firstName
    self.IDnumber = idNumber
    self.HoursWorked = hours
    self.Wage = wage
def weeklyPay(self):
    if self.HoursWorked > 40:
        return (40 * self.Wage) + (self.HoursWorked - 40) * 1.5 * self.Wage
    else:
        return self.HoursWorked * self.Wage
def find_employee(employees, empID):
    for i in range(len(employees)):
        if employees[i].idNumber == empID:
            return i
    return -1
employeesFile = open("Employees.txt")
hoursFile = open("Hours.txt")
employees = []
for i in range(3):
    x = employeesFile.readline()
    x2 = hoursFile.readline()
    y = x.strip().split(",")
    emp = Employee(y[0], y[1], int(y2[1]), float(y[3]))
    employees.append(emp)
employeesFile.close()
print("{:>12s}{:>12s}{:>12s}{:>12s}{:>12s}{:>12s}". format("First", "Last","ID", "Hours", "Hourly", "Weekly")) 
print("{:>12s}{:>12s}{:>12s}{:>12s}{:>12s}{:>12s}". format("Name", "Name", "Number", "Worked", "Wage", "Pay")) 
for emp in employees:   
    print("{:>12s}{:>12s}{:>12d}{:>12.2f}{:>12.2f}{:>12.2f}". 
        format(emp.FirstName, emp.LastName, emp.IDNumber, emp.HoursWorked, emp.Wage,round(emp.weeklyPay(),2))) 
print("Index:",find_employee(employees,39119))

