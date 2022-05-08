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