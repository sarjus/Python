#Fuction to calculate Gross Pay 
def computepay(Hours,rate) :
    grossPay = 0;
    #Pay the hourly rate for the hours up to 40 and
    #1.5 times the hourly rate for all hours worked above 40 hours.
    if Hours > 40 :
        grossPay = grossPay + 40 * rate
        grossPay = grossPay + ((Hours-40)*(rate*1.5))
    else :
        grossPay = grossPay + 40 * rate
    return grossPay

Hours = input('Enter the Hours:')
Hours = float(Hours)
rate  = input('Enter the Rate:')
rate = float(rate)
grossPay=computepay(Hours,rate)
print("Pay", grossPay)
