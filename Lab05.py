# Quentin Moore
# CS65 Mon 1100
# 09-22-2025

those_days = int(input("Please enter the number of days: "))
counting_stars = 0
mony_mony = 0

while counting_stars < those_days:
    counting_stars += 1
     
    if counting_stars % 5 == 0 and counting_stars <= 100:
        mony_mony += (2* counting_stars)/100
        
    elif counting_stars <= 100:
        mony_mony += counting_stars/100
    
    elif counting_stars % 5 == 0 and counting_stars < 100:
        mony_mony += (6* counting_stars)/100
    
    else:
        mony_mony += (3* counting_stars)/100
        
print(f"After {those_days} days, you would have ${mony_mony:.2f}")
