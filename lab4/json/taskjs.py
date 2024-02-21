import json 
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

file = open("sample_data.json")
data = json.load(file)
datas = file.read()
for item in data['imdata']:
    print(f"{item['l1PhysIf']['attributes']['dn']}                              {item['l1PhysIf']['attributes']['speed']}   {item['l1PhysIf']['attributes']['mtu']}")
