d1 = {"ashu":"burger" , "mummy":"roti_sabji" , "papa":"chicken",
      "Prashant":{"morning":"momos" , "afternoon":"fried rice","evening":"chowmin"}}
d1["amit"] = "Poha"
d1["ansshul"] ="jalebi"
d1["bhavik"]="Phapda"
d1[420] = " aam janta ki kamai"
del d1[420]
del d1["bhavik"]

d2 = d1.copy()
del d2["ashu"]
print(d1)
print(d2)