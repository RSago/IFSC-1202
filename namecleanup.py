def middleName(middleName_str): 
    return properCase(middleName_str[middleName_str.find(' '):middleName_str.rfind(' ')]) 
def lastName(lastName_str): 
    return properCase(lastName_str[lastName_str.rfind(' '):]) 
def firstName(firstName_str): 
    return properCase(firstName_str[:firstName_str.find(' ')]) 
def trim(trim_str): 
    return trim_str.strip() 
def removeCR(removeCR_str): 
    return removeCR_str.replace("\n", "") 
def properCase(str): 
    str = trim(str) 
    str = removeCR(str) 
    str_len = len(str) 
    return str[0].upper() + str[1:str_len] 
if __name__ == '__main__': 
    filepath = 'names.txt' 
    with open(filepath) as fp: 
        allNames = [] 
        for line in fp: 
            allNames.append(line) 
        print("Lines :", allNames) 
        for full_name in allNames: 
            print("\nRaw full name : ", full_name) 
            full_name = trim(full_name) 
            full_name = removeCR(full_name) 
            first_name = firstName(full_name) 
            print("First Name :", first_name) 
            middle_name = middleName(full_name) 
            print("Middle Name :", middle_name) 
            last_name = lastName(full_name) 
            print("Last Name :", last_name) 