# Functions
def computepay(hours,rate):
    print("In computepay",hours,rate)
    if hours>40:
    #print("overtime")
        reg= hours*rate
        otp= (hours-40.0) * (rate*0.5)
        pay= reg + otp
    else:
        pay= hours*rate
    #print("Returning", pay)
    return pay

sh= input("Enter hours:")
sr= input("Enter rate per hour:")
fh= float(sh)
fr= float(sr)
xp= computepay(fh,fr)
#xp= fh*fr

print("Pay",xp)   

