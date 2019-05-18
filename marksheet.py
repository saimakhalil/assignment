biology = int(input("enter Biology marks"))
chemistry = int(input("enter Chemistry marks"))
sindhi = int(input("enter Sindhi marks"))
pak_Studies = int(input("enter Pakitan Studies marks"))
english = int(input("enter English marks"))
sum = biology+chemistry+sindhi+pak_Studies+english
percentage= (sum*100)/500
if biology <==32 and chemistry <==32 and sindhi <==32 and pak_Studies <==32 and english <==32:
    print (" your garde is F")
elif percentage >=80 :
    print ("Your Grade  is A+\nPercentage", percentage)
elif percentage >=70 :
    print ("Your Grade is A\nPercentage", percentage)
elif percentage >=60 :
    print ("Your Grade is B\nPercentage", percentage)
elif percentage >=50 :
    print ("Your Grade is C\nPercentage", percentage)
elif percentage >=40 :
    print ("Your Grade is D\nPercentage", percentage)
elif percentage >=40 :
    print ("Your Grade is F\nPercentage", percentage)
# elif biology <=32 : 
#     print (" Fail in Biology")
# elif chemistry <=32 : 
#     print (" Fail in Chemistry")
# elif sindhi <=32 :
#     print (" Fail in Sindhi")
# elif pak_Studies <=32 :
#     print (" Fail in Pakistan Studies")
# elif english <=32 :
#     print (" Fail in English")
else:
    print ("Try again there is error")
    print ("Good Luck")