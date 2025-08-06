students = {
    "Alice": 89,
    "Bob": 95,
    "Charlie": 78,
    "Diana": 92
}

topper = max(students, key=students.get)
print("Topper (with data structure):", topper)