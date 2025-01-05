# Dictionary 
people_ages={"Mallik": 18, "Ammu": 17, "Keerthi": 25, "Bharath": 16, "Pavan": 36}


count = 0
for name,age in people_ages.items():
    if age >=18:
        count = count + 1


print(f"Total number of people above the age of 18: {count}")
