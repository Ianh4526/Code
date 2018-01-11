# mapa o tabla hash en otros lenguajes
captains = {}
captains["Enterprise"] = "Kirk"
captains["Enterprise D"] = " Picard"
captains["Deep Space Nine"] = "Sisko"
captains["Voyayer"] = "Janeway"

print captains["Voyayer"]

print captains.get("Enterprise")
#get to safetely return an entry
print captains.get("NX-01")

for ship in captains:
    print ship + ": " + captains[ship]
#to get all the data on the dictionary
