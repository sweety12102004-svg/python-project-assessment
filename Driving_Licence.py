age = 20
learner_license = True
test_score = 75

if age >= 18:
    if learner_license:
        if test_score >= 60:
            print("Eligible for Driving License")
        else:
            print("Driving Test Failed")
    else:
        print("Learner License Required")
else:
    print("Underage")

# OUTPUT
Eligible for Driving License
