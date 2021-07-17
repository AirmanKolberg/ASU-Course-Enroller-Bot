from twilio.rest import Client
from secrets import sid, token, trial_number, my_number


client = Client(sid, token)


def call_me():
    client.calls.create(url='http://demo.twilio.com/docs/voice.xml',
                        to=my_number,
                        from_=trial_number)

    print('Called you!')


def text_me(text_message):
    client.messages.create(body=text_message,
                           from_=trial_number,
                           to=my_number)

    print('Sent you a text message!')


if __name__ == '__main__':
    
    pass
