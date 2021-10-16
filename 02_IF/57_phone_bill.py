
TARIF = 15
INCLUDED_MIN_IN_STD_PLAN = 50
INCLUDED_SMS_IN_STD_PLAN = 50
TARIF_1_MIN_ADDITIONAL_IN_STD_PLAN = 0.25
TARIF_1_SMS_ADDITIONAL_IN_STD_PLAN = 0.15
TOTAL_FEE_PECENT = 5
FEE_CALL_CENTER = 0.44

count_of_minutes_per_month = int(input("Enter the count of minutes: "))
count_of_sms_per_month = int(input("Enter the count of sms: "))

if count_of_minutes_per_month <= INCLUDED_MIN_IN_STD_PLAN and count_of_sms_per_month <= INCLUDED_SMS_IN_STD_PLAN :
    total_bill = 15
    print("Total sum is $%0.2f" % total_bill)
elif count_of_minutes_per_month > INCLUDED_MIN_IN_STD_PLAN or count_of_sms_per_month >INCLUDED_SMS_IN_STD_PLAN :
    bill_min = (count_of_minutes_per_month - INCLUDED_MIN_IN_STD_PLAN)*0.25 
    bill_sms = (count_of_sms_per_month - INCLUDED_SMS_IN_STD_PLAN)*0.15
    call_center = (bill_min+bill_sms)+0.44
    tax = round(((bill_min+bill_sms)+0.44)*0.05,2)
    total_bill = round((15+((bill_min+bill_sms)+0.44)*1.05),2)
    print("The count of additional", count_of_minutes_per_month - INCLUDED_MIN_IN_STD_PLAN, " payment for minutes is ", bill_min)
    print("The count of additional sms", count_of_sms_per_month - INCLUDED_SMS_IN_STD_PLAN, " payment for sms is ", bill_sms)
    print("The tax is: %0.2f " % tax)
    print("The total bill is %0.2f" % total_bill)



