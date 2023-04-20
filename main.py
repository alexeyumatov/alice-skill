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


got_new_sword, food, dog, extremely_little_food = False, False, False, False


def main(user_input):
    global got_new_sword, food, dog, extremely_little_food
    text, new_button_text_1, new_button_text_2, new_button_text_3, end = \
        '', '', '', 'Мне надо идти, пока!', 'false'
    # ------------------------- #
    if user_input == 'Да!':
        text = 'Тогда слушай, в эпоху Эдо, в Японии, жил один самурай по имени Такэо. ' \
               'Он оставил после себя большую книгу, в которой хранилась одна маленькая история' \
               'из его жизни. Ты всё ещё слушаешь?'
        new_button_text_1 = 'Да, я тут!'
        new_button_text_2 = 'Нет!'
    if user_input == 'Нет!':
        text = 'Тогда пока!'
        new_button_text_1 = 'Пока!'
        new_button_text_2 = 'До встречи!'
        end = 'true'
    # ------------------------- #
    if user_input == 'Да, я тут!':
        text = 'Хорошо, тогда я начинаю читать. 1625 год, месяц сацуки. Выйдя на улицу, я увидел' \
               'толпу людей, который столпились у местного кузнеца Хондзе Масамунэ, по совместительству моего ' \
               'друга. Стоит ли мне подойти к нему?'
        new_button_text_1 = 'Стоит!'
        new_button_text_2 = 'Не надо, зачем, лучше пройдём мимо.'
    # ------------------------- #
    if user_input == 'Стоит!':
        text = 'Кое как пройдя через толпу людей, я увидел довольного друга, который демонстрировал' \
               'новый клинок, который по его словам способен разрубить гору! Я конечно верю в него, ' \
               'но в эту сказку верю с трудом... После того как толпа рассосалась, он, увидев меня, ' \
               'сказал что готов отдать мне этот меч, так как в прошлом я спас его лавку от нападения' \
               'бандитов. Ну, по крайней мере этот клинок куда лучше, чем моя старая и тупая катана.' \
               'И ещё он передал письмо от моего господина, страшно открывать. Как думаешь, что там?'
        new_button_text_1 = 'Какое то поручение?'
        new_button_text_2 = 'Награда за службу?'
        got_new_sword = True
    if user_input == 'Не надо, зачем, лучше пройдём мимо.':
        text = 'Через такую толпу мы вряд ли протиснемся, так что пожалуй пойдём пройдёмся перед походом ' \
               'в горы за травами. Эх, какая же сегодня приятная погода, так хорошо и спокойно... ' \
               'После этих слов, словно с целью нарушить тишину ко мне подбегает мой друг - тот самый' \
               'кузнец и вручает мне письмо от моего господина, страшно открывать. Как думаешь, что там?'
        new_button_text_1 = 'Какое то поручение?'
        new_button_text_2 = 'Награда за службу?'
    # ------------------------- #
    if user_input == 'Какое то поручение?':
        text = 'Да, я был совершенно прав, это было поручение... Необходимо срочно выдвинуться' \
               'в соседнее поселение и собрать парочку человек для того, чтобы сопроводить ' \
               'жену моего господина в безопасное место... Неужели войско врага так далеко продвинулось..' \
               'Ладно, нет времени думать, пора собираться, куда пойти бы сначала?'
        new_button_text_1 = 'Взять еды в дорогу'
        new_button_text_2 = 'Попрощаться с другом'
    if user_input == 'Награда за службу?':
        text = 'Окрылённый этой идеей о награде, я с радостью открываю письмо. Это было поручение..' \
               'Необходимо срочно выдвинуться в соседнее поселение и сопроводить жену моего господина ' \
               'в безопасное место ... Неужели войско врага так далеко продвинулось.. Пора собираться, ' \
               'куда пойти бы сначала?'
        new_button_text_1 = 'Взять еды в дорогу'
        new_button_text_2 = 'Попрощаться с другом'
    # ------------------------- #
    if user_input == 'Взять еды в дорогу':
        text = 'Стоит запастись провиантом в дорогу, не хотелось бы умереть от голода..' \
               'Как раз я вижу рядом повозку где торгуют вяленным мясом.' \
               '- Привет, по чём продаешь? - спрашиваю я' \
               '- Ох, ты же Такэо, верно? Господин всё оплачивает, бери сколько нужно - отвечает торговец.' \
               'А вот такой поворот событый мне нравится, подумал я про себя и набрал провизии на всю дорогу.' \
               'Чтож, дальше думаю пойду домой, собирать вещи в путь или можно пойти подготовить к бою оружие..'
        food = True
        new_button_text_1 = 'Пойти домой'
        new_button_text_2 = 'Подготовить оружие'
    if user_input == 'Попрощаться с другом':
        text = 'Хм, стоит попрощаться с другом перед долгой дорогой, кто знает, всякое может случиться..' \
               'Поговорив с единственным другом - Хондзе Масамунэ, я понял что он что-то скрывает и недоговаривает,' \
               ' но ладно, может настроения нет. Ладно, дальше думаю пойду домой, собирать вещи в путь или можно' \
               ' пойти подготовить к бою оружие..'
        new_button_text_1 = 'Пойти домой'
        new_button_text_2 = 'Подготовить оружие'
    # ------------------------- #
    if user_input == 'Пойти домой':
        text = 'И так, я дома. Развернув перед собой карту нашего поселения, я понял что пройти в соседнее можно ' \
               'через рисовые поля или холодные горы. Как пойдём?'
        new_button_text_1 = 'Пойти через рисовые поля'
        new_button_text_2 = 'Пойти через горы'
    if user_input == 'Подготовить оружие':
        if got_new_sword is True:
            text = 'Хорошо что я заглянул к кузнцу, теперь у меня есть новый клинок, не думаю что его стоит как-то ' \
                   ' подготавливать к бою. Мне стоит выйти как можно раньше, идти ночью довольно не приятно и опасно.' \
                   ' Так, ну вещи я вроде упаковал, можно выходить. Сейчас я могу пойти через рисовые поля или через ' \
                   ' горы, как стоит поступить?'
            new_button_text_1 = 'Пойти через рисовые поля'
            new_button_text_2 = 'Пойти через горы'
        else:
            text = 'Я наточил свой клинок и теперь я точно готов выйти в путь. Уже вечереет и безопаснее будет пойти' \
                   ' через поля. Выйдя из дома, я отправился в сторону рисовых полей и на меня накинулись бандиты' \
                   ' как мне стоит тратить силы?'
            new_button_text_1 = 'Бейся как в последний раз!'
            new_button_text_2 = 'Не напрягайся, они слабые соперники.'
    # ------------------------- #
    if user_input == 'Пойти через рисовые поля':
        text = 'Я спокойно прошёл через поля, но на горизонте увидел бандитов. Хорошо что я ' \
               'вышел раньше. За мной увязалась собака, я могу с ней поделиться мясом и надеюсь что она пойдёт со ' \
               'мной. Стоит ли мне это сделать?'
        new_button_text_1 = 'Да, она будет хорошим напарником!'
        new_button_text_2 = 'Не стоит на неё трать провизию'
    if user_input == 'Пойти через горы':
        text = 'Идти через эти горы будет тяжело, но так я смогу быстрее добраться до поселения. Начинаю своё ' \
               'восхождение на гору. Тут очень холодно, я чувствую что придётся сделать остановку. Стоит ли мне это ' \
               'сделать сейчас?'
        new_button_text_1 = 'Да, остановка сейчас не будет лишней!'
        new_button_text_2 = 'Нет, пройдём и так!'
    # ------------------------- #
    if user_input == 'Бейся как в последний раз!':
        text = 'Я чувствую прилив сил и готов им всем показать как сражается настоящий самурай!!!! ' \
               'Я получаю лёгкое ранение в ногу, ничего страшного, жить буду. Все бандиты были поражены ' \
               'и я хромая продолжил свой путь. Стоит ли мне сделать перевал для перевязки раны или и так пойдёт?'
        new_button_text_1 = 'И так пойдёт!'
        new_button_text_2 = 'Лучше сделать перевал!'
    if user_input == 'Не напрягайся, они слабые соперники.':
        text = 'Забавно, враги испугались моей уверенности и почти сразу убежали роняя свои вещи по пути. Я подобрал' \
               ' кошелёк полный денег и счастливый продолжил свой путь. Уже ночь и я сильно устал, стоит ли делать ' \
               'перевал или поспешим в поселение?'
        new_button_text_1 = 'Сделаем перевал!'
        new_button_text_2 = 'Нет, мы спешим!'
    # ------------------------- #
    if user_input == 'Да, она будет хорошим напарником!':
        if food is True:
            text = 'Я решил поделиться едой с собакой. Ей явно понравилось это мяско. Теперь у меня есть верный ' \
                   'спутник. Думаю как бы её назвать... Она похожа на утренний свет, пусть будет Акирой! В любом ' \
                   'случае, вместе нам будет явно веселее идти. Уже темнеет, не пора ли нам сделать остановку?'
            dog = True
        else:
            text = 'Эх, у меня и так мало еды, но этот пёсик такой дружелюбный, грех не поделиться.' \
                   '- Хороший мальчик, хороший. - приговаривал я гладя собаку. Она же в свою очередь понюхала,' \
                   ' облизала кусок мяса, который я ей дал и фыркнув пошла от меня прочь. Что за неблагодарный пёс!' \
                   'Теперь у меня ещё меньше еды... Уже темнеет, не пора ли нам сделать остановку?'
            extremely_little_food = True
        new_button_text_1 = 'Да, делаем остановку!'
        new_button_text_2 = 'Нет, идём дальше'
    if user_input == 'Не стоит на неё трать провизию':
        text = '- А ну прочь отсюда, у меня для тебя ничего нет! - сказал я громко в сторону это собаки.' \
               'Да, мне немного жаль что у я не стал с ней делиться едой, но меня ждёт долгий путь! Уже темнеет, ' \
               'не пора ли нам сделать остановку?'
        new_button_text_1 = 'Да, делаем остановку!'
        new_button_text_2 = 'Нет, идём дальше'
    # ------------------------- #
    if user_input == 'Да, остановка сейчас не будет лишней!':
        if food is True:
            text = 'Разместив маленький костёр, я смог погреться и поесть еды. Хорошо что у меня её много, я смог ' \
                   'поесть вдовль! Ну чтож, отдохнули и хватит, двигаем дальше! По пути я '
    if user_input == 'Нет, пройдём и так!':
        pass
    # ------------------------- #
    if user_input == 'И так пойдёт!':
        pass
    if user_input == 'Лучше сделать перевал!':
        pass
    # ------------------------- #
    if user_input == 'Сделаем перевал!':
        pass
    if user_input == 'Нет, мы спешим!':
        pass
    # ------------------------- #
    if user_input == 'Да, делаем остановку!':
        pass
    if user_input == 'Нет, идём дальше':
        pass
    # ------------------------- #
    if user_input == 'Мне надо идти, пока!':
        text = 'Тогда пока!'
        end = 'true'

    return [text, new_button_text_1, new_button_text_2, new_button_text_3, end]
