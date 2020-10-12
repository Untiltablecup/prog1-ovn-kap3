poang = float(input("Hur många poang fick eleven?")) # Frågar hur många poäng som eleven fick och ger sedan varibeln poang det numret

if poang < 25:         # Om elevens poäng är mindre än 25 får dom F
    print ("Betyg: F")
elif poang <30>=25:    # Om elevens poäng är 25 eller mellan 25 och 30 får eleven E
    print ("Betyg: E")
elif poang <35>=30:    # Om elevens poäng är 30 eller mellan 30 och 35 får eleven D
    print ("Betyg: D")
elif poang <40>=35:    # Om elevens poäng är 35 eller mellan 35 och 40 får eleven C
    print ("Betyg: c")
elif poang <45>=40:    # Om elevens poäng är 40 eller mellan 40 och 45 får eleven B
    print ("Betyg: B")
elif poang >=45:       # Om elevens poäng är 45 eller mer så får eleven A
    print ("Betyg: A")
