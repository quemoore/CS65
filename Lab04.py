# Quentin Moore
# Lab04
# 09/17/2025

limit = int(input("What is the limit? "))
increment = int(input("What is the increment? "))

'''
count = 0
while count <= limit:
    print(count)
    count += increment
'''

for x in range(0, limit +1, increment):
    print(x)