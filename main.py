def handler(event, context):
    text = 'Привет! Хочешь я расскажу тебе историю про самурая?'
    if 'request' in event and 'original_utterance' in event['request'] and \
            len(event['request']['original_utterance']) > 0:
        user_input = event['request']['original_utterance']
        output = main(user_input)
        text = output[0]
        new_button_text_1 = output[1]
        new_button_text_2 = output[2]
        new_button_text_3 = output[3]
        end = output[4]
        return {
            'version': event['version'],
            'session': event['session'],
            'response': {
                'text': text,
                'tts': text,
                "buttons": [
                    {
                        "title": new_button_text_1,
                        "hide": True
                    },
                    {
                        "title": new_button_text_2,
                        "hide": True
                    },
                    {
                        "title": new_button_text_3,
                        "hide": True
                    },

                ],
                'end_session': end,
            },
        }

    return {
        'version': event['version'],
        'session': event['session'],
        'response': {
            'text': text,
            'tts': text,
            "buttons": [
                {
                    "title": "Да!",
                    "hide": True
                },
                {
                    "title": "Нет!",
                    "hide": True
                }
            ],
            'end_session': 'false',
        },
    }


def main(user_input):
    pass
