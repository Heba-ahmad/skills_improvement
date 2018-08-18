import datetime

print("Hi, My name is Heba!")
print("I learnd how to code in Python!")

print("I love programming ")

print("and I love horses too")
      
print("Here\'s a picture of horse")

print("        ,--,")
print("  _ ___/ /\|")
print(" ;( )__, )")
print("; //   '--;")
print("  \     |")
print("   ^    ^")
your_age= str(raw_input("would you like me to tell you your age? yes or no: "))
if your_age in "Yes Y yes yeah yea y":
    print "Great!"
    y1 = int(input("what year were you born? "))
    m1 = int(input("what month you were born? from 1 to 12: "))
    d1 = int(input("and what day you were born? from 1 to 31: "))
    now = datetime.datetime.now()
    y2 = now.year
    m2 = now.month
    d2 = now.day
    age= 2030 - y1
    agenow= y2 - y1
    daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def isLeapYear(year):
        ##
        # Your code here. Return True or False
        # Pseudo code for this algorithm is found at
        # http://en.wikipedia.org/wiki/Leap_year#Algorithm
        ##
        if year % 4 == 0:
            return True
        if year % 100 ==0:
            return False
        if year % 400 == 0: 
            return True
        else:
            return False
    def Count_Days(year1, month1, day1):
        if month1 ==2:
            if isLeapYear(year1):
                if day1 < daysOfMonths[month1-1]+1:# daysofmonth for feb(2) = dayOfMonths[2-1]= 29 if leap year
                    return year1, month1, day1+1
                else:
                    if month1 ==12:
                        return year1+1,1,1
                    else:
                        return year1, month1 +1 , 1
            else:#if notleap year 
                if day1 < daysOfMonths[month1-1]:#daysofmonth for feb(2) = dayOfMonths[2-1]= 28 
                    return year1, month1, day1+1
                else:
                    if month1 ==12:
                        return year1+1,1,1
                    else:
                        return year1, month1 +1 , 1
        else:# if month1 is not 2  
            if day1 < daysOfMonths[month1-1]:# if month1= 6 the daysofmonth for june(6) = dayOfMonths[6-1]= 30
                 return year1, month1, day1+1
            else:
                if month1 ==12:
                    return year1+1,1,1
                else:
                        return year1, month1 +1 , 1
    def daysBetweenDates(y1, m1, d1, y2, m2, d2):
        if y1 > y2:
            m1,m2 = m2,m1
            y1,y2 = y2,y1
            d1,d2 = d2,d1
        days=0
        while(not(m1==m2 and y1==y2 and d1==d2)):
            y1,m1,d1 = Count_Days(y1,m1,d1)
            days+=1
        return days

    thank_you= """

    Thank you :)

    All the best

    bey

    """
    print "You are", agenow, "years old"
    print "There are", daysBetweenDates(y1, m1, d1, y2, m2, d2) ,"between your birthday and today!"
    print "In the year 2030 you\'ll be", age, "years old!"
    print thank_you

else:
    smile = """

      .ssSSSSss.
    .ER'      `AM.
  .ST'          `CS.
 .E'  .S.    .S.  `S.
.L'   SSS    SSS   `S.
S'    `S'    `S'    `S
S                    S
S                    S
S.  s.          .s   S
`S. `"s.      .s"'  S'
 `S.  `"ss..ss"'  .S'
  `SS.    ~~    .SS'
    `SS.      .SS'
      `SSssssSS'

"""
    print "OK .. All the best", smile
