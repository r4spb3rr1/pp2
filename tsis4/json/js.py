import json
print("Interface Status")
print("================================================================================")
print("DN                                  x.                Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

with open("sample_data.json", "r") as file:
    json_data = file.read()
data = json.loads(json_data)
interfaces = data.get('imdata', [])
for i in interfaces:
    l1physif = i.get('l1PhysIf', {})
    att = l1physif.get('attributes', {})
    
    dn = att.get('dn', '')
    descr = att.get('descr', '')
    speed = att.get('speed', 'inherit')
    mtu = att.get('mtu', '')
    
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, descr, speed, mtu))