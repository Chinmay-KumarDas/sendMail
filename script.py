import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os

sender_email = os.getenv('SENDER_EMAIL')
sender_password = os.getenv('SENDER_PASSWORD')
# import time

# Email configuration

# HTML email content (same as before)
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to the TCS Future Associates Discord Community</title>
</head>
<body style="font-family: Arial, sans-serif; color: #333; background-color: #f4f4f4; margin: 0; padding: 0;">
    <table width="100%" style="background-color: #004080; padding: 20px;">
        <tr>
            <td align="center">
                <h1 style="color: #fff; font-size: 28px;">Welcome to the TCS Future Associates Community! 🎉</h1>
            </td>
        </tr>
    </table>
    <table width="100%" cellpadding="0" cellspacing="0" style="padding: 20px;">
        <tr>
            <td>
                <p style="font-size: 18px; color: #004080; font-weight: bold;">Hello fellow TCSer!</p>
                <p>We’re excited to invite you to our <strong>TCS Future Associates Discord Community</strong>! This server is an <strong>initiative by a fellow TCSer</strong> and is here to help people just like you, <strong>waiting for their TCS joining</strong>, to connect, learn, and support each other.</p>
                <p><strong>Please note:</strong> This is <u>not an official TCS channel</u>—just a friendly community run by TCSers to make the journey easier for all of us. Here’s what you’ll find:</p>
                <ul style="list-style-type: none; padding: 0;">
                    <li>💬 <strong>Casual Discussions</strong> - Chat freely and connect with other future TCSers</li>
                    <li>📚 <strong>Learning Resources</strong> - Access shared study resources, guides, and tips</li>
                    <li>🤝 <strong>Project Ideas</strong> - Collaborate on projects and grow your skills</li>
                    <li>🛠️ <strong>Doubts & Guidance</strong> - Get help with technical and HR questions</li>
                </ul>
                <p>Our community is here to help each other prepare for TCS, but it’s also a place to <strong>relax, make friends, and have fun!</strong> There’s no management or senior staff on the server, so feel free to discuss openly. 🚀</p>
                <p style="text-align: center; margin-top: 20px;">
                    <a href="https://discord.gg/Bx8K9h77JH" style="background-color: #004080; color: #fff; padding: 15px 25px; text-decoration: none; font-size: 9px; border-radius: 5px; margin: 5px;">Join the TCS Discord Community</a>
                </p>
                <p>Looking forward to seeing you there and building this community together!</p>
                <p style="font-size: 16px; color: #555;">Best regards,<br>A fellow TCSer</p>
            </td>
        </tr>
    </table>
</body>
</html>
"""

# Set up the server
server = smtplib.SMTP('smtp.gmail.com', 587)  # Use your email provider's SMTP settings
server.starttls()
server.login(sender_email, sender_password)

# Read emails from a text file and send them
def send_emails_from_file(file_number):
    with open(f'batch_{file_number}.txt', 'r') as f:
        email_addresses = f.readlines()

    for email in email_addresses:
        email = email.strip()  # Remove any whitespace/newline characters
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = 'Welcome to the TCS Future Associates Community!'
        msg.attach(MIMEText(html_content, 'html'))
        server.send_message(msg)
        print(f'Email sent to {email}')

# Specify the file number for today's batch (e.g., batch_1, batch_2, etc.)
file_number = 26  # Change this number each day ------- done till Batch 26

# Send emails from the specified batch file
send_emails_from_file(file_number)

server.quit()
