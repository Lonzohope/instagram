from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_welcome_email(name,receiver):
   #creating message subject and sender
   subject = 'Welcome to InstaBae'
   sender = 'hopemutheu@gmail.com'

   #passing in the context variables
   text_content = render_to_string('email/gramemail.txt',{"name": name})
   html_content = render_to_string('email/gramemail.html',{"name": name})

   msg = EmailMultiAlternatives(subject,text_content,sender[receiver])
   msg.attach_alternative(html_content,'text.html')
   msg.send()