import requests
from flask import current_app

from .models import TelegramAdmin


# function for sending data in telegram bot
def send_msg_bot(**kwargs):
    BOT_TOKEN = current_app.config['BOT_TOKEN']
    dict_text = {**kwargs}
    msg_type = dict_text.get('type_of_message', "")
    text_array = [
        f'{key}: {value}'
        for key, value in dict_text.items() if key != 'type_of_message'
    ]
    text = '\n'.join(text_array)

    tg_admins = TelegramAdmin.query.all()  # TODO: check for admin permissions
    for admin in tg_admins:
        chat_id = admin.chat_id
        if msg_type:
            title_text = "New comment:" if msg_type == "comment" else "New contact:"
            primary_message = f'''
                https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={title_text} 
            '''
            requests.get(primary_message)

        main_message = f'''
            https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={text}
        '''
        requests.get(main_message)
