from django.core.mail import send_mail

def send_activation_email(email, code):
    activation_url = f'http://localhost:8000/account/activate/?u={code}'
    send_mail(
        'Здравствуйте, активируйте ваш аккаунт!',
        f'Для активации аккаунта нужно перейти по ссылке ниже:'
        f'\n{activation_url}',
        'azkergeshov@gmail.com',
        [email],
        fail_silently=False
    )

def send_password_reset_email(email, reset_code):
    send_mail(
        'Сброс пароля',
        f'Чтобы востанавить пароль, нужно перейти на сайт и ввести код снизу'
        f'\n{reset_code}',
        'akzergeshov@gmail.com',
        [email],
        fail_silently=False
    )