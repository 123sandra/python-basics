w="Swimming"
print(w)
print(type(w))

o="Right now i am swimming in the pool"
#length
print(len(o)) 
print(len(w))
#in or not in
print("now" in o)
print("how" not in o)
print("wow" in o)
print("swimming" not in o)
# upper and lower
print(o.upper())
print(o.lower())
print(w.upper())
print(w.lower())
# finding the range
print(w[3])
print(w[6])
print(w[-2])
print(w[-3])
print(o[3:10])
print(o[20:])
print(o[:20])
print(o[-3:])
print(o[:-7])
print(o[-10:-2])
# concatinating variables
print(w+o)
print(w+" "+o)
# spliting  
r="there are: different types: of fruits"
print(r.split(":"))
#concatinating differet datatypes
item="pizza"
e= f"I would like to order a {item}"
print(e)
# counting no of values
print(o.count("i"))
# replacing 
print(o.replace("swimming", "walking"))

