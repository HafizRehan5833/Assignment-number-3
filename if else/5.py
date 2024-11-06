#5. Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).

total_num=555
math=int(input("Enter your math result : "))
urdu=int(input("Enter your urdu result :"))
eng=int(input("Enter your english result :"))
phy=int(input("Enter your phy result :"))
comp=int(input("Enter your comp result :"))
Tarjama=int(input("Enter your T.Q result :"))

sum=math+urdu+eng+phy+comp+Tarjama

avg=(sum/total_num)*100



if avg >= 90 :
    print("Your number is ",sum,"Out of ",total_num,"And You average is ",avg,"You got a A+ grade.")
elif avg >= 80 and avg <=90:
   print("Your number is ",sum,"Out of ",total_num,"And You average is ",avg,"You got a A grade.")
elif avg >= 70 and  avg <=80:
    print("Your number is ",sum,"Out of ",total_num,"And You average is ",avg,"You got a B grade.")
elif avg >= 60 and avg <= 70:
     print("Your number is ",sum,"Out of ",total_num,"And You average is ",avg,"You got a C+ grade.")
elif avg >= 50 and avg <= 60:
     print("Your number is ",sum,"Out of ",total_num,"And You average is ",avg,"You got a C grade.")
else:
    print("Your number is ",sum,"Out of ",total_num,"And You average is ",avg,"You Fail in exams.")



