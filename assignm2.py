course=["data analytics","ui&ux","java","php","pyton","data science","ai&ml"]
fees=[5000,25000,18000,4000,7500,2000,1600]

print(type(course))
print(course)
print(fees)
print(type(fees))

course.append("data mining")
print(course)
fees.append(4500)

course.insert(3,"c++")
print(course)
fees.insert(4,1000)
print(fees)

# course.extend(fees)
# print(course)

course.remove("php")
print(course)
fees.remove(5000)

course.pop()
print(course)
course.pop(4)
fees.pop()
print(fees)

course.sort()
print(course)
course.sort(reverse=True)
print(course)

fees.sort()
print(fees)
fees.sort(reverse=True)
print(fees)

print(course.count("java"))

u=tuple(course)
print(u)
v=tuple(fees)
print(v)