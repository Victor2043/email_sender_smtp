import smtplib, ssl

def send_email(email):
    try:
        port = 465  
        password = "Alterar123"
        ssl._create_default_https_context = ssl._create_unverified_context
        context = ssl.create_default_context()
        
        receiver_email = email
        sender_email = "python3.email.smtp@gmail.com"
        message  = """Subject: Python
                    Hello from python """

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        
        return 'email enviado'

    except Exception as e:
        return str(e)

    
