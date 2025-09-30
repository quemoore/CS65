#Quentin Moore
#CS65 Section 1

food_total = float(input("Total bill: "))
num_people_dining = int(input("Number of people: "))
tip_precent = int(input("Percent tip: "))

bill_total = (food_total * (1 + tip_precent/100))/num_people_dining

print("Each person owes: ", round(bill_total, 2))