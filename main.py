from bill import Bill, Flatmate
from report import PDFReport

bill_amount = float(input("Enter the Bill amount: "))
period = input("Enter the period of bill for example: 'September 2024': ")

flatmate_1 = input("Enter the flatmate 1's name: ")
flatmate_2 = input("Enter the flatmate 2's name: ")

flatmate_1_Days_in_House = int(input("Enter the flatmate 1's number of days in house: "))
flatmate_2_Days_in_House = int(input("Enter the flatmate 2's number of days in house: "))

the_bill = Bill(bill_amount, period)
flatmate1 = Flatmate(flatmate_1, flatmate_1_Days_in_House)
flatmate2 = Flatmate(flatmate_2, flatmate_2_Days_in_House)
pdf = PDFReport('Billing_Summary.pdf')
pdf.generate(flatmate1, flatmate2, the_bill)

