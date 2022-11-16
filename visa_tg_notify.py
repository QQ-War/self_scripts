import requests
import pyrogram
import time


session = requests.Session()
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36', 'Cookie': '_ga=GA1.'}
url = 'https://ais.usvisa-info.com/'

api_id = ''
api_hash = ''
bot_token = ''
chats = ['']


def main():
    app = pyrogram.Client('visa_bot', api_id=api_id, api_hash=api_hash, bot_token=bot_token)
    app.start()
    while True:
        response = session.get(url=url, headers=headers)
        if 'There are no available appointments at this time. Please check back in a few days as the Consular Section will open more appointments.' in response.text:
            pass
        elif 'Sign in or Create an Account' in response.text:
            for chat in chats:
                app.send_message(chat, 'need to login again')
        else:
            for chat in chats:
                app.send_message(chat, 'maybe there is a chance')
        print(f'running at {time.asctime( time.localtime(time.time()) )}')
        time.sleep(60)
    app.stop()


if __name__ == '__main__':
    print(f"The __name__ variable of module2 is: {__name__}.")
    main()
