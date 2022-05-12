# Conditional Execution
sh= input("Enter hours:")
sr= input("Enter rate per hour:")
fh= float(sh)
fr= float(fh)
#xp=fh*fr
if fh>40: 
  #print(overtime)
  reg= fh*fr
  otp= (fh-40) * (fr*0.5)
  xp= reg + otp
else:
  #print(regular)
  xp= fh*fr
print("Pay:",xp)  



#code2
ss=input("Enter score:")
fs=float(ss)
if fs >= 0.9:
    print("A")
elif fs >= 0.8:
    print("B")
elif fs >= 0.7:
    print("C")
elif fs >= 0.6:
    print("D")
elif fs <= 0.5:
    print("F")
elif fs >= 1:
    print("Out of range")