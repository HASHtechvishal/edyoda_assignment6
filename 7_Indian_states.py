'''Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.'''
import json

states = {"Haryana":"Chandigarh","Himachal Pradesh":"Shimla",
           "Jharkhand":"Ranchi","Karnataka":"Bangalore","Kerala":"Thiruvananthapuram","Madhya Pradesh":"Bhopal",
           "Maharashtra":"Mumbai"}

write = open("states.json","w")
json.dump(states,write,indent=4)

print("file wirte...")
write.close()