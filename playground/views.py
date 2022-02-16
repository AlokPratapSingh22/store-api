from django.shortcuts import render
# from django.core.mail import EmailMessage, BadHeaderError
# from templated_mail.mail import BaseEmailMessage
# from .tasks import notify_customers


def say_hello(request):
    # notify_customers.delay('Hello')
    return render(request, 'hello.html', {'name': 'Alok'})
    # try:

    #     # message = BaseEmailMessage(
    #     #     template_name='email/hello.html',
    #     #     context={'name': 'Alok'}
    #     # )
    #     # message.send(['john@alok.com'])

    #     # message = EmailMessage('subject', 'message',
    #     #                        'from@alok.com', ['tojo@alok.com'])
    #     # message.attach_file('playground/static/images/ss.png')
    #     # message.send()

    #     # send_mail('subject', 'message', 'info@alok.com', ['bob@alok.com'])
    #     # mail_admins('subject', 'message', html_message='<em>message</em>')
    # except BadHeaderError:
    #     pass
