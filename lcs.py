grades = ["AA", "BB", "CC", "AB", "BC", "CD", "AA", "BC", "CC", "DD", "BB", "BC", "CD", "DD", "FF", "AA", "AB", "CD", "CC", "AA"]
lcs = []
ptr1 = 0
ptr2 = 1
while ptr2 < len(grades):
    while ptr2 < len(grades) and (grades[ptr2] is not grades[ptr1]):
        ptr2 += 1
    if(ptr2 < len(grades) and grades[ptr2] is grades[ptr1]):
        lcs.append(grades[ptr1])
    ptr2 += 1
    while ptr2 < len(grades) and (grades[ptr1] is not grades[ptr2]):
        ptr1 += 1
    if(ptr2 < len(grades) and grades[ptr1] is grades[ptr2]):
        lcs.append(grades[ptr1])
    ptr1 += 1
print(lcs)