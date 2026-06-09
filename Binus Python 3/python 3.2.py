Age = int(input("Enter any age: "))
if(Age <= 1):
    print("Baby")
elif((Age >= 2) and (Age < 4)):
    print("Toddler")
elif((Age >= 5) and (Age < 7)):
    print("preschooler")
elif((Age >= 6) and (Age < 13)):
    print("child")
elif((Age >= 13) and (Age < 18)):
    print("teenager")
elif((Age >= 18) and (Age < 22)):
    print("young adult")
elif((Age >= 22) and (Age < 31)):
    print("pre-adult")
elif((Age >= 31) and (Age < 51)):
    print("adult")
elif((Age >= 51) and (Age < 71)):
    print("pre-elderly")
elif((Age >= 71)):
    print("elderly")