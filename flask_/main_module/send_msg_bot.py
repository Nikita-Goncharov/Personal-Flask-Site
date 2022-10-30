import requests
from flask import current_app

# function for sending data in telegram bot
def send_msg_bot(**kwargs):
    CHAT_ID = current_app.config['CHAT_ID']
    BOT_TOKEN = current_app.config['BOT_TOKEN']
    dict_text = {**kwargs}
    text_array = [
        f'{key}: {value}'
        for key, value in dict_text.items() if key != 'type_of_message'
    ]
    text = '\n'.join(text_array)

    if (dict_text['type_of_message'] == 'comment'):
        primary_message = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text=' + 'New comment: '
    elif (dict_text['type_of_message'] == 'contact'):
        primary_message = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text=' + 'New contact: '
    
    main_message = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={text}'
    
    if (primary_message):
        requests.get(primary_message)    
    requests.get(main_message)
