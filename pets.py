import csv

class Pet:
  def __init__(self):
    self.name = ''
    self.type = ''
    self.age = ''
  
  def setName(self, nm):
    self.name = nm
  
  def setType(self, tp):
    self.type = tp

  def setAge(self, ag):
    self.age = ag

  def getName(self):
    return self.name
  
  def getType(self):
    return self.type

  def getAge(self):
    return self.age

  def printPet(self):
    print("Pet: ", self.name, self.type, self.age)

petObjects = []

with open('Pets.txt', 'r') as file:
  petList = list(csv.reader(file, delimiter = ' '))
  for row in petList:
    pet = Pet()
    pet.setName(row[0])
    pet.setType(row[1])
    pet.setAge(row[2])
    petObjects.append(pet)

print('Name\t\tType\tAge')
for row in petObjects:
  print('{}\t\t{}\t\t{}'.format(row.getName(),row.getType(),row.getAge()))