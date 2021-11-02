# Covid-19 Certificate with QR
Working in progress...

** Version 1.0.0.**

This is an app to create Covid-19 Certificates with QR.

This application can be used by the staff of a testing laboratory.

When we run this app it will be displayed a MENU with 2 options:
1. Insert the Customer's Data
2. Quit

After that you will have to choose between 1 and 2.
If you choose 1 the app will run.
if you choose 2 the app will quit.
If you have a different choice the app will display "You can choose only between 1 or 2." and the loop will run again.

If you choose 1 you will receive login informations. First, "What is Your Username?" and the second time "What is You Password?".

The Username is not case-sensitive.
You have only 3 attempts.
If the username is wrong you will receive "Wrong Username! You only have 2 more attempts."
If the username is wrong you will receive "Wrong Username! You only have 1 more attempts."
If the username is wrong you will receive "You have no more attempts. Goodbye!". The loop will stop.

When you insert the correct user_name the app will display "What is Your Password?"
You have only 3 attempts.
If the username is wrong you will receive "Wrong Username! You only have 2 more attempts."
If the username is wrong you will receive "Wrong Username! You only have 1 more attempts."
If the username is wrong you will receive "You have no more attempts. Goodbye!". The loop will stop.

After that you have to insert the customer's first name.
The Customer's First Name is not case-sensitive.
If you use numbers or special characters in first name you will receive this message: "You cannot use numbers or special characters."
After that, the loop will continue to ask you to insert the customer's name.
The First Name is not case-sensitive.

After you enter a correct First Name, you have to enter the Last Name.
If you use numbers or special characters in last name you will receive this message: "You cannot use numbers or special cha
The Last Name is not case-sensitive.

First Name and Last Name can be composed of several words.

Finally, you have to introduce the Covid-19 result.
You have to choose between NEGATIVE and POSITIVE.
The input is not case-sensitive.
If you introduce a wrong data, you will receive the message: "The result can only be POSITIVE or NEGATIVE." and the loop will restart.

After the correct data entry, the application will generate a pdf report with qr.
On the report you will find:
1. Current Date and Time.
2. The QR. When you scan the qr code, the customer's first and last name will be displayed, together with the negative or positive result.
3. The Body. In the body the client will find his name and the test result.
4. Footer. In the footer the client will find the name of the user who generated the report, a test location and a phone number.



