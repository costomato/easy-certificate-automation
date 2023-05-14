# The Canva Hack: Automating Certificate Generation for a Cyber Security Seminar

## Phase 1: The challenge

As the technical head of the cyber security club at our college, it was my responsibility to create certificates for all the participants of our recent seminar on data security. With the seminar now over, I sat down to generate certificates for all the attendees.

I first designed the certificate on Canva, but when it came to exporting it in bulk, I hit a roadblock - the bulk export feature was only available with a premium subscription. I was left scratching my head, wondering how I was going to generate certificates for over a hundred attendees.

I tried searching for a solution online, but I couldn't find anything that would help me. So, I thought of using Python to automate the process. I created a login process using `Selenium`. And a roadblock again -  Canva was not allowing me to login using Selenium.

After some brainstorming, I hit upon an idea: what if I could host the certificate design on Canva as a webpage and then manipulate the attendee's name using Python and Selenium? So, I gave it a try, and it worked like a charm!

I made some adjustments to the Canva design, shared it using the website option, and selected the standard format. Then, I used Selenium to change the name in the certificate for each attendee. Finally, I used the Chrome print option to generate a PDF for each certificate and saved them with the attendees' email addresses as their file names.

## Phase 2: Sending the Certificates

Feeling pretty proud of my Canva hack, I moved on to the next task - sending the certificates to the attendees. I had already saved the certificates with the attendees' email addresses as file names, so all I had to do was use Python's `smtplib` library to send each certificate to its respective owner. And just like that, I had automated the entire process of certificate generation and distribution!

Overall, the experience taught me that with a little bit of creativity and hard work, even seemingly impossible tasks can be accomplished.