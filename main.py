import io
import qrcode
import datetime

from auth import users
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader


print("Covid-19 Certificate Application\n -------------------------------")
menu = "1. Insert the Customer's Data\n\n2. Quit"

flag = True

while flag:
    print(menu)
    choose = input("\nChoose Your Option (1 or 2)\n>>> ")
    if choose == "1":
        # users login
        tries = 3

        while tries > 0:
            user_input = input("What is Your Username?\n>>> ").lower()

            if user_input in users:
                tries = 0
            else:
                tries -= 1
                if tries == 0:
                    print("You have no more attempts. Goodbye!")
                elif tries == 1:
                    print(f"Wrong Username! You only have {tries} more attempt.")
                else:
                    print(f"Wrong Username! You only have {tries} more attempts.")
        if user_input not in users:
            break

        tries = 3

        while tries > 0:
            user_pass = input("What is Your Password?\n>>> ")

            if user_pass == users[user_input][0]:
                tries = 0
                print(f"Welcome {users[user_input][1]}!")
            else:
                tries -= 1
                if tries == 0:
                    print("You have no more attempts. Goodbye!")
                elif tries == 1:
                    print(f"Wrong Password! You only have {tries} more attempt.")
                else:
                    print(f"Wrong Password! You only have {tries} more attempts.")
        if user_pass != users[user_input][0]:
            break

        print("-----------------------------")

        # insert clients data
        flag = True

        while flag:
            first_name = input("Insert the Customer's First Name: \n>>> ").title()

            if first_name.isalpha() or " " in first_name:
                flag = False
            else:
                print("You cannot use numbers or special characters.")
                flag = True

        flag = True

        while flag:
            last_name = input("Insert the Customer's Last Name: \n>>> ").upper()

            if last_name.isalpha() or " " in last_name:
                flag = False
            else:
                print("You cannot use numbers or special characters.")
                flag = True

        flag = True

        while flag:
            result = input("Insert Covid-19 Result (NEGATIVE or POSITIVE): \n >>> ").upper()
            if result == "NEGATIVE" or result == "POSITIVE":
                print("----------------------------------")
                flag = False
            else:
                print("The result can only be POSITIVE or NEGATIVE.")

        # create pdf body
        global did
        did = ""
        if result == "POSITIVE":
            did = "did"
        else:
            did = "did not"

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        report = canvas.Canvas("covid_test.pdf")
        report.drawString(75, 800, "Current date and time:")
        report.drawString(75, 775, f"{now}")
        report.drawString(225, 625, "Result Report / Certificate")
        report.drawString(75, 550, f"Dear {first_name} {last_name}, ")
        report.drawString(75, 525, f"Your coronavirus(COVID-19) test result is {result},")
        report.drawString(75, 500, f"meaning you {did} have the virus when the test was done.")
        report.drawString(75, 450, "Please continue to follow your local government guidelines.")
        report.drawString(75, 425, "Contact 112 if you need medical help. For medical emergency, dial 999.")
        report.drawString(75, 375, "For more advice go to https://www.gov.uk/coronavirus")
        report.drawString(75, 325, "Type of Test: Sample collection for the RT-PCR test in the form of swab.")
        report.drawString(75, 200, f"{users[user_input][1]}")
        report.drawString(75, 185, "Mobile Laboratory Manager")
        report.drawString(75, 170, "Random Clinical Laboratory Services")
        report.drawString(75, 155, "Tel: +44 (0)28 9552 3645")
        report.drawString(300, 200, "Testing Location")
        report.drawString(300, 185, "Random Drive Through Testing center")
        report.drawString(300, 170, "London/United Kingdom")
        report.drawString(300, 155, "Postcode: RM11 1ER")
        report.drawString(224, 50, "- End of Report -")

        report.save()


        # generate the QR code
        img = qrcode.make(f"{first_name} {last_name}: Covid-19 {result}")
        img.save("code.jpg")

        # add the QR code on PDF
        now = datetime.datetime.now().strftime("%H_%M_%S")
        in_pdf_file = 'covid_test.pdf'
        out_pdf_file = str(now) + ".pdf"
        img_file = "..\covid_test\code.jpg"

        packet = io.BytesIO()
        can = canvas.Canvas(packet)
        x_start = 380
        y_start = 550
        can.drawImage(img_file, x_start, y_start, width=150, preserveAspectRatio=True, mask='auto')
        can.save()

        new_pdf = PdfFileReader(packet)

        existing_pdf = PdfFileReader(open(in_pdf_file, "rb"))
        output = PdfFileWriter()

        for i in range(len(existing_pdf.pages)):
            page = existing_pdf.getPage(i)
            page.mergePage(new_pdf.getPage(i))
            output.addPage(page)

        outputStream = open(out_pdf_file, "wb")
        output.write(outputStream)
        outputStream.close()

        flag = True
    elif choose == "2":
        print("Have a Good Day!")
        break
    else:
        print("You can choose only between 1 or 2.")
        print("-----------------------------------")


