
import json

employees = {
  "employee_1" : {
    "name" : "vishal arora",
    "DOB":"10/08/1994",
    "Height":6,
    "City":"delhi", 
    "State":"delhi"
  },
  "employee_2" : {
    "Name":"saisha", 
    "DOB":"25/05/1996", 
    "Height":5.5, 
    "City":"jalandhar", 
    "State":"punjab"
  },
  "employee_3" : {
    "Name":"Anil",
    "DOB":"25/5/1992",
    "Height":5.4, 
    "City":"delhi",
    "State":"delhi"
  },
  "employee_4" : {
    "Name":"Jay", 
    "DOB":"11/12/1994", 
    "Height":5.5, 
    "City":"delhi", 
    "State":"delhi"
  },
  "employee_5" : {
    "Name":"Ayaan", 
    "DOB":"7/3/1991", 
    "Height":5.7, 
    "City":"delhi", 
    "State":"delhi"
  }
}

write = open("employee.json","w")
json.dump(employees,write,indent=4)

print("file wirte...")
write.close()

'''Finally print the list of the Employee objects.'''

with open("employee.json","r") as write:
    read = json.load(write)
    print(read)
