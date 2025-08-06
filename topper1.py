#print the name of the topper with out using data structure

name1 = "Alice"
score1 = 85

# Student 2
name2 = "Bob"
score2 = 92

# Student 3
name3 = "Charlie"
score3 = 78

# Find the topper
if score1 >= score2 and score1 >= score3:
    print("Topper is:", name1)
elif score2 >= score1 and score2 >= score3:
    print("Topper is:", name2)
else:
    print("Topper is:", name3)