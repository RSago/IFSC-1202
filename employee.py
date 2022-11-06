class Employee:
    def __init__(self,fname,lname,idn,hworked,wage):
        self.FirstName = fname
        self.LastName = lname
        self.IDNumber = idn
        self.HoursWorked = hworked
        self.Wage = wage
    def WeeklyPay(self):
        if self.HoursWorked <= 40:
            return self.HoursWorked*self.Wage

        
        return (40*self.Wage)+((self.HoursWorked-40)*1.5*self.Wage)

print("   First    Last      ID   Hours  Hourly  Weekly\n    Name    Name  Number  Worked    Wage     Pay""")

file = open("10.06 Payroll.txt", "r")

for line in file.readlines():
    e = line.split(',')
    e = Employee(e[0].strip(),e[1].strip(),int(e[2]),float(e[3]),float(e[4]))

    print("%8s%8s%8d%8.2f%8.2f%8.2f"%(e.FirstName,e.LastName,e.IDNumber,e.HoursWorked,e.Wage,e.WeeklyPay()))

file.close()