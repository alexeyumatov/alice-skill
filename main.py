def handler(event, context):
    text = 'Привет! Хочешь я расскажу тебе историю про самурая?'
    if 'request' in event and 'original_utterance' in event['request'] and \
            len(event['request']['original_utterance']) > 0:
        user_input = event['request']['original_utterance']

        got_new_sword = event['state']['session']['sword']
        food = event['state']['session']['start_food']
        extremely_little_food = event['state']['session']['food_state']
        dog = event['state']['session']['dog']
        injury = event['state']['session']['injury']
        energy = event['state']['session']['energy']
        money = event['state']['session']['money']
        warriors = event['state']['session']['warriors']

        output = main(user_input, got_new_sword, food, dog,
                      extremely_little_food, injury, energy,
                      money, warriors)

        text = output[0]
        new_button_text_1 = output[1]
        new_button_text_2 = output[2]
        new_button_text_3 = output[3]
        end = output[4]

        got_new_sword = output[5]
        food = output[6]
        extremely_little_food = output[7]
        dog = output[8]
        injury = output[9]
        energy = output[10]
        money = output[11]
        warriors = output[12]

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
            'session_state': {
                "sword": got_new_sword,
                "start_food": food,
                "food_state": extremely_little_food,
                "dog": dog,
                "injury": injury,
                "energy": energy,
                "money": money,
                'warriors': warriors,
            },
        }
    else:
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
            'session_state': {
                "sword": False,
                "start_food": False,
                "food_state": False,
                "dog": False,
                "injury": False,
                "energy": False,
                "money": False,
                'warriors': False,
            },
        }


def main(user_input, got_new_sword, food, dog, extremely_little_food, injury, energy, money, warriors):
    text, new_button_text_1, new_button_text_2, new_button_text_3, end = '', '', '', 'Мне надо идти, пока!', 'false'
    # ------------------------- #
    if user_input == 'Да!':
        text = ' Тогда слушай, в эпоху Эдо, в Японии, жил один самурай по имени Такэо. ' \
               ' Он оставил после себя большую книгу, в которой хранилась одна маленькая история' \
               ' из его жизни. Ты всё ещё слушаешь?'
        new_button_text_1 = 'Да, я тут!'
        new_button_text_2 = 'Нет!'
    if user_input == 'Нет!':
        text = 'Тогда пока!'
        new_button_text_1 = 'Пока!'
        new_button_text_2 = 'До встречи!'
        end = 'true'
    # ------------------------- #
    if user_input == 'Да, я тут!':
        text = ' Хорошо, тогда я начинаю читать. 1625 год, месяц сацуки. Выйдя на улицу, я увидел' \
               ' толпу людей, которые столпились у местного кузнеца Хондзе Масамунэ, по совместительству моего ' \
               ' друга. Стоит ли мне подойти к нему?'
        new_button_text_1 = 'Стоит!'
        new_button_text_2 = 'Не надо, зачем, лучше пройдём мимо.'
    # ------------------------- #
    if user_input == 'Стоит!':
        text = ' Кое как пройдя через толпу людей, я увидел довольного друга, который демонстрировал' \
               ' новый клинок, который по его словам способен разрубить гору! Я конечно верю в него, ' \
               ' но в эту сказку верю с трудом... После того как толпа рассосалась, он, увидев меня, ' \
               ' сказал что готов отдать мне этот меч, так как в прошлом я спас его лавку от нападения' \
               ' бандитов. Ну, по крайней мере этот клинок куда лучше, чем моя старая и тупая катана.' \
               ' И ещё он передал письмо от моего господина, страшно открывать. Как думаешь, что там?'
        new_button_text_1 = 'Какое то поручение?'
        new_button_text_2 = 'Награда за службу?'
        got_new_sword = True
    if user_input == 'Не надо, зачем, лучше пройдём мимо.':
        text = ' Через такую толпу мы вряд ли протиснемся, так что пожалуй пойдём пройдёмся перед походом ' \
               ' в горы за травами. Эх, какая же сегодня приятная погода, так хорошо и спокойно... ' \
               ' После этих слов, словно с целью нарушить тишину ко мне подбегает мой друг - тот самый' \
               ' кузнец и вручает мне письмо от моего господина, страшно открывать. Как думаешь, что там?'
        new_button_text_1 = 'Какое то поручение?'
        new_button_text_2 = 'Награда за службу?'
    # ------------------------- #
    if user_input == 'Какое то поручение?':
        text = ' Да, я был совершенно прав, это было поручение... Необходимо срочно выдвинуться' \
               ' в соседнее поселение и собрать парочку человек для того, чтобы сопроводить ' \
               ' жену моего господина в безопасное место... Неужели войско врага так далеко продвинулось..' \
               ' Ладно, нет времени думать, пора собираться, куда пойти бы сначала?'
        new_button_text_1 = 'Взять еды в дорогу'
        new_button_text_2 = 'Попрощаться с другом'
    if user_input == 'Награда за службу?':
        text = ' Окрылённый этой идеей о награде, я с радостью открываю письмо. Это было поручение..' \
               ' Необходимо срочно выдвинуться в соседнее поселение и сопроводить жену моего господина ' \
               ' в безопасное место ... Неужели войско врага так далеко продвинулось.. Пора собираться, ' \
               ' куда пойти бы сначала?'
        new_button_text_1 = 'Взять еды в дорогу'
        new_button_text_2 = 'Попрощаться с другом'
    # ------------------------- #
    if user_input == 'Взять еды в дорогу':
        text = ' Стоит запастись провиантом в дорогу, не хотелось бы умереть от голода..' \
               ' Как раз я вижу рядом повозку где торгуют вяленным мясом.' \
               ' - Привет, по чём продаешь? - спрашиваю я' \
               ' - Ох, ты же Такэо, верно? Господин всё оплачивает, бери сколько нужно - отвечает торговец.' \
               ' А вот такой поворот событый мне нравится, подумал я про себя и набрал провизии на всю дорогу.' \
               ' Чтож, дальше думаю пойду домой, собирать вещи в путь или можно пойти подготовить к бою оружие..'
        food = True
        new_button_text_1 = 'Пойти домой'
        new_button_text_2 = 'Подготовить оружие'
    if user_input == 'Попрощаться с другом':
        text = ' Хм, стоит попрощаться с другом перед долгой дорогой, кто знает, всякое может случиться..' \
               ' Поговорив с единственным другом - Хондзе Масамунэ, я понял что он что-то скрывает и недоговаривает,' \
               ' но ладно, может настроения нет. Ладно, дальше думаю пойду домой, собирать вещи в путь или можно' \
               ' пойти подготовить к бою оружие..'
        new_button_text_1 = 'Пойти домой'
        new_button_text_2 = 'Подготовить оружие'
    # ------------------------- #
    if user_input == 'Пойти домой':
        text = ' И так, я дома. Развернув перед собой карту, я понял что пройти в соседнее поселение можно ' \
               ' через рисовые поля или холодные горы. Как пойдём?'
        new_button_text_1 = 'Пойти через рисовые поля'
        new_button_text_2 = 'Пойти через горы'
    if user_input == 'Подготовить оружие':
        if got_new_sword is True:
            text = ' Хорошо что я заглянул к кузнцу, теперь у меня есть новый клинок, не думаю что его стоит как-то ' \
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
        text = ' Я спокойно прошёл через поля, но на горизонте увидел бандитов. Хорошо что я ' \
               ' вышел раньше. За мной увязалась собака, я могу с ней поделиться мясом и надеюсь что она пойдёт со ' \
               ' мной. Стоит ли мне это сделать?'
        new_button_text_1 = 'Да, она будет хорошим напарником!'
        new_button_text_2 = 'Не стоит на неё трать провизию'
    if user_input == 'Пойти через горы':
        text = ' Идти через эти горы будет тяжело, но так я смогу быстрее добраться до поселения. Начинаю своё ' \
               ' восхождение на гору. Тут очень холодно, я чувствую что придётся сделать остановку. Стоит ли мне это ' \
               ' сделать сейчас?'
        new_button_text_1 = 'Да, остановка сейчас не будет лишней!'
        new_button_text_2 = 'Нет, пройдём и так!'
    # ------------------------- #
    if user_input == 'Бейся как в последний раз!':
        text = ' Я чувствую прилив сил и готов им всем показать как сражается настоящий самурай!!!! ' \
               ' Я получаю лёгкое ранение в ногу, ничего страшного, жить буду. Все бандиты были поражены ' \
               ' и я хромая продолжил свой путь. Стоит ли мне сделать перевал для перевязки раны или и так пойдёт?'
        injury = True
        new_button_text_1 = 'И так пойдёт!'
        new_button_text_2 = 'Лучше сделать перевал!'
    if user_input == 'Не напрягайся, они слабые соперники.':
        text = ' Забавно, враги испугались моей уверенности и почти сразу убежали роняя свои вещи по пути. Я подобрал' \
               ' кошелёк полный денег и счастливый продолжил свой путь. Уже ночь и я сильно устал, стоит ли делать ' \
               ' перевал или поспешим в поселение?'
        money = True
        new_button_text_1 = 'Сделаем перевал!'
        new_button_text_2 = 'Нет, мы спешим!'
    # ------------------------- #
    if user_input == 'Да, она будет хорошим напарником!':
        if food is True:
            text = ' Я решил поделиться едой с собакой. Ей явно понравилось это мяско. Теперь у меня есть верный ' \
                   ' спутник. Думаю как бы её назвать... Она похожа на утренний свет, пусть будет Акирой! В любом ' \
                   ' случае, вместе нам будет явно веселее идти. Уже темнеет, не пора ли нам сделать остановку?'
            dog = True
        else:
            text = ' Эх, у меня и так мало еды, но этот пёсик такой дружелюбный, грех не поделиться.' \
                   ' - Хороший мальчик, хороший. - приговаривал я гладя собаку. Она же в свою очередь понюхала,' \
                   ' облизала кусок мяса, который я ей дал и фыркнув пошла от меня прочь. Что за неблагодарный пёс!' \
                   ' Теперь у меня ещё меньше еды... Уже темнеет, не пора ли нам сделать остановку?'
            extremely_little_food = True
        new_button_text_1 = 'Да, делаем остановку!'
        new_button_text_2 = 'Нет, идём дальше'
    if user_input == 'Не стоит на неё трать провизию':
        text = ' - А ну прочь отсюда, у меня для тебя ничего нет! - сказал я громко в сторону это собаки.' \
               ' Да, мне немного жаль что у я не стал с ней делиться едой, но меня ждёт долгий путь! Уже темнеет, ' \
               ' не пора ли нам сделать остановку?'
        new_button_text_1 = 'Да, делаем остановку!'
        new_button_text_2 = 'Нет, идём дальше'
    # ------------------------- #
    if user_input == 'Да, остановка сейчас не будет лишней!':
        if food is True:
            text = ' Разместив маленький костёр, я смог погреться и поесть еды. Хорошо что у меня её много, я смог ' \
                   ' поесть вдовль! Ну что, отдохнули и хватит, двигаем дальше! Иду, иду, иду... И вот сейчас я вижу ' \
                   ' какой-то спуск с горы, казалось что раньше его не было.. Пойдём по этому спуску или продолжим ' \
                   ' путь по обычному пути?'
        elif extremely_little_food is True:
            text = ' Разместив маленький костёр, я обнаружил что у меня уже почти нет еды и это крайне меня тревожит ' \
                   ' ... В горах я вряд ли смогу найти еду..... Ладно, хоть немного, но отдохнул. Выдвигаемся! ' \
                   ' Меня ждёт тяжёлый путь, надеюсь я дойду... Сейчас я вижу какой-то спуск с горы, казалось что ' \
                   ' раньше его не было.. Может я там найду еду?  Пойдём по этому спуску или продолжим путь по ' \
                   ' обычному пути?'
        else:
            text = ' Разместив маленький костёр, я обнаружил что у меня не так и много еды, надо бы её беречь, ' \
                   ' но тем не менее, я смог поесть и восстановить силы! Пора выдвигаться, по пути я вижу своё ' \
                   ' поселение, оно кажется таким крошечным... Меня ждёт тяжёлый путь, надеюсь я дойду...' \
                   ' Сейчас я вижу какой-то спуск с горы, казалось что раньше его не было.. Пойдём по этому ' \
                   ' спуску или продолжим путь по обычному пути?'
        new_button_text_1 = 'Пойдём по этому спуску'
        new_button_text_2 = 'Пойдём по обычному пути'
        energy = True
    if user_input == 'Нет, пройдём и так!':
        text = 'Я решил пропустить это прекрасное место для остановки. Мне надо торопиться, дама моего Господина ' \
               ' скорее всего сейчас находится в опасности! Я должен добраться до поселения как можно скорее....' \
               ' Невзирая на лёгкую усталость я собрался с силами и продолжил свой путь.. И вот сейчас я вижу ' \
               ' какой-то спуск с горы, казалось что раньше его не было.. Пойдём по этому спуску или продолжим ' \
               ' путь по обычному пути?'
        new_button_text_1 = 'Пойдём по этому спуску'
        new_button_text_2 = 'Пойдём по обычному пути'

    # ------------------------- #
    if user_input == 'И так пойдёт!':
        text = 'Хромая я продолжил свой путь.... Боль в моей ноге давала о себе знать, думаю это серьёзно ' \
               ' меня замедлит на пути к поселению.. Надеюсь дальше будет без происшествий. И так, я уже вижу на ' \
               ' горизонте поселение.... Осталось перейти реку и я буду там. Думаю к восходу солнца дойду.. ' \
               ' Есть выбор, пройти реку вброд или обойти и пройти по мосту. Как поступим?'
        new_button_text_1 = 'Пройдём вброд'
        new_button_text_2 = 'Пройдём по мосту в обход'
    if user_input == 'Лучше сделать перевал!':
        text = 'Я решил сделать перевал и перевязать свою рану... Так то лучше.. Я отдохнул и готов идти дальше...' \
               ' Надеюсь дальше будет без происшествий. И так, я уже вижу на  горизонте поселение.... Осталось ' \
               ' перейти реку и я буду там. Думаю к восходу солнца дойду.. Есть выбор, пройти реку вброд ' \
               ' или обойти и пройти по мосту. Как поступим?'
        injury = False
        energy = True
        new_button_text_1 = 'Пройдём вброд'
        new_button_text_2 = 'Пройдём по мосту в обход'
    # ------------------------- #
    if user_input == 'Сделаем перевал!':
        text = 'Пожалуй лучше сделать перевал и набраться сил для того чтобы быстрее дойти до поселения...' \
               ' И так, во время отдыха ничего интересного не произошло, разве что переживания терзают моё сердце ' \
               ' Я надеюсь у них там всё хорошо и они твёрдо держат оборону.. Надо спешить! Прямо сейчас, там, на ' \
               ' подступах к городу сражаются мои союзники... Я не могу их подвести. Осталось перейти реку и я ' \
               ' буду там. Думаю к восходу солнца дойду.. Есть выбор, пройти реку вброд или обойти и пройти по ' \
               ' мосту. Как поступим?'
        energy = True
        new_button_text_1 = 'Пройдём вброд'
        new_button_text_2 = 'Пройдём по мосту в обход'
    if user_input == 'Нет, мы спешим!':
        text = 'Я решил пропустить это прекрасное место для остановки. Мне надо торопиться, дама моего Господина ' \
               ' скорее всего сейчас находится в опасности! Я должен добраться до поселения как можно скорее....' \
               ' Невзирая на лёгкую усталость я собрался с силами и продолжил свой путь.. Осталось перейти реку и я ' \
               ' буду там. Думаю к восходу солнца дойду.. Есть выбор, пройти реку вброд или обойти и пройти по ' \
               ' мосту. Как поступим?'
        new_button_text_1 = 'Пройдём вброд'
        new_button_text_2 = 'Пройдём по мосту в обход'
    # ------------------------- #
    if user_input == 'Да, делаем остановку!':
        if food is True and dog is True:
            text = 'Я всё таки решил сделать остановку.. После того как я разбил свой лагерь, я вдоволь наелся и ' \
                   ' поиграл с Акирой. Самое главное набраться сил, меня ждёт тяжёлое испытание впереди.... Чтож, ' \
                   ' я поспал и готов идти вперёд. Я должен добраться до поселения как можно скорее.... Осталось ' \
                   ' перейти реку и я буду там. Думаю к восходу солнца дойду..  Есть выбор, пройти реку вброд ' \
                   ' или обойти и пройти по мосту. Как поступим?'
        elif food is True and dog is False:
            text = 'Я всё таки решил сделать остановку.. После того как я разбил свой лагерь, я вдоволь наелся. ' \
                   ' Самое главное набраться сил, меня ждёт тяжёлое испытание впереди.... Чтож, ' \
                   ' я поспал и готов идти вперёд. Я должен добраться до поселения как можно скорее.... Осталось ' \
                   ' перейти реку и я буду там. Думаю к восходу солнца дойду..  Есть выбор, пройти реку вброд ' \
                   ' или обойти и пройти по мосту. Как поступим?'
        elif food is False and dog is False:
            text = 'Я всё таки решил сделать остановку.. После того как я разбил свой лагерь, я кое как смог поесть, ' \
                   ' ведь еды у меня осталость мало.... Самое главное набраться сил, меня ждёт тяжёлое испытание ' \
                   ' впереди.... Чтож, я поспал и готов идти вперёд. Я должен добраться до поселения как можно ' \
                   ' скорее.... Осталось перейти реку и я буду там. Думаю к восходу солнца дойду..  Есть выбор, ' \
                   ' пройти реку вброд или обойти и пройти по мосту. Как поступим?'
        new_button_text_1 = 'Пройдём вброд'
        new_button_text_2 = 'Пройдём по мосту в обход'
    if user_input == 'Нет, идём дальше':
        text = 'Я решил не отдыхать и пойти дальше. У меня нет времени на отдых, я должен быть там как можно скорее!' \
               ' Усталый я продолжил идти... Я уже вижу поселение на горизонте, думаю я буду там к восходу солцна. ' \
               ' Я должен добраться до поселения как можно скорее.... Осталось перейти реку и я буду там. Думаю ' \
               ' к восходу солнца дойду..  Есть выбор, пройти реку вброд или обойти и пройти по мосту. Как поступим?'
        new_button_text_1 = 'Пройдём вброд'
        new_button_text_2 = 'Пройдём по мосту в обход'
    # ------------------------- #
    if user_input == 'Пройдём вброд':
        text = 'Я решил пойти вброд через реку.. Я думаю так выйдет куда быстрее, но есть риск... И так, подойдя ' \
               ' к реке, я собрал все свои вещи в мешок и поднял их над головой, чтобы не намочить их. Перейдя ' \
               ' реку, я оказался рядом с поселением. Осталось совсем чуть чуть... Теперь, находясь рядом с ' \
               ' этой деревней, я увидел на горизонте дым от костра. Сходим проверить?'
        new_button_text_1 = 'Да, сходим и проверим!'
        new_button_text_2 = 'Нет, спешим в поселение!'
    if user_input == 'Пройдём по мосту в обход':
        text = 'Я решил пойти по мосту в обход. Да, так будет куда дольше, но таким образом риск сводится к ' \
               ' минимуму. И так, я перешёл реку через мост. Я нахожусь на основной дороге к поселению. ' \
               ' До места назначения осталость рукой подать. Но.... Что я вижу... Главные ворота... Они горят...' \
               ' Я опоздал? Нет, нет, нет, мне надо бежать. Я подбегаю к главным воротам и забегаю в город ' \
               ' охваченный огнём. Я должен побежать к дому Господина. Как же мне стоит побежать, через главную ' \
               ' улицу (так быстрее, но скорее всего опасней) или пойти дворами (так чуть чуть медленнее, но ' \
               ' думаю что безопаснее)?'
        new_button_text_1 = 'Бежим через главную улицу!'
        new_button_text_2 = 'Бежим через дворы!'
    # ------------------------- #
    if user_input == 'Пойдём по этому спуску':
        text = ' Решил рискнуть и спуститься сейчас. Я думаю так может выйти быстрее, чем идти обычной дорогой.' \
               ' Пройдя по этому пути, я оказался у моста рядом с поселением. Осталось перейти эту реку и я буду ' \
               ' у главных ворот. Правда этот запах..... Запах горелой древесины.... Надо бежать! Я подбегаю к ' \
               ' главным воротам и забегаю в город охваченный огнём. Я должен побежать к дому Господина. Как же ' \
               ' мне стоит побежать, через главную улицу (так быстрее, но скорее всего опасней) или пойти дворами ' \
               ' (так чуть чуть медленнее, но думаю что безопаснее)? '
        new_button_text_1 = 'Бежим через главную улицу!'
        new_button_text_2 = 'Бежим через дворы!'
    if user_input == 'Пойдём по обычному пути':
        text = ' Не стану рисковать и пойду по обычному пути... И так, спустившись с горы и пройдя в пещеру у ' \
               ' подножья, я оказался в тунеле, что ведёт к дому господина. Надо спешить! Я должен вывести его ' \
               ' семью в безопасное место! Выйдя из тунеля, я оказался во дворе дома Господина. В главный вход уже ' \
               ' ломятся враги. Что мне стоит сделать, зачистить местность около дома и потом спасти его семью или ' \
               ' как можно быстрее через двор вывести их??? Думай, думай, думай!!!!!'
        new_button_text_1 = 'Защитим дом и потом спасём семью!'
        new_button_text_2 = 'Выведем их через двор!'
    # ------------------------- #
    if user_input == 'Да, сходим и проверим!':
        text = ' Я решил пойти и проверить что там. Там сидели мои союзники. Они рассказали о жестокой битве, что ' \
               ' началась вчера утром. Многие погибли, город на грани захвата. Про имение Господина не известно ' \
               ' ничего. Я должен спешить! Они сказали что последуют за мной. Теперь по крайней мере в случае битвы ' \
               ' я буду не один. Подойдя к горящим воротам города, я увидел ужасающую картину... Весь город полыхает,' \
               ' все мирные жители убегают... Похоже что ситуация вышла из под контроля. Я должен побежать к дому ' \
               ' Господина. Как же мне стоит побежать, через главную улицу (так быстрее, но скорее всего опасней) ' \
               ' или пойти дворами (так чуть чуть медленнее, но думаю что безопаснее)?'
        warriors = True
        new_button_text_1 = 'Бежим через главную улицу!'
        new_button_text_2 = 'Бежим через дворы!'
    if user_input == 'Нет, спешим в поселение!':
        text = 'Я решил не останавливаться и побежать в поселение. Я решил пройти через восточный вход в город..' \
               ' Так, пройдя чуток по улицам, я увидел печальное состояние города. Всё полыхает, мирные жители ' \
               ' бегут кто куда, а воины этого поселения сражаются до последнего вздоха. Что же мне делать, помочь ' \
               ' им и зачистить территорию около дома Господина или бежать напролом и попытаться под шумок увести ' \
               ' всю семью Господина?'
        new_button_text_1 = 'Защитим дом и потом спасём семью!'
        new_button_text_2 = 'Выведем их через двор!'
    # ------------------------- #
    if user_input == 'Бежим через главную улицу!':
        text = 'Мне надо спешить, нельзя терять ни минуты! Я вижу как сражаются мои союзники, к сожалению ' \
               ' я не могу помочь им, у меня особая миссия, Господин доверяет мне. Пробегая через горящие дома, ' \
               ' поверженных противников и храбро стоящих до последнего вздоха союзников, я наполняюсь энергией ' \
               ' на битву! Я смогу выполннить свою миссию! Подбегая к дому моего Господина, я вижу как его окружили ' \
               ' враги. Что же мне стоит сделать, защитить дом и потом спасти семью или обойти их и так же ' \
               ' спасти семью Господина уйдя с ними через дворы?'
        new_button_text_1 = 'Защитим дом и потом спасём семью!'
        new_button_text_2 = 'Выведем их через двор!'
    if user_input == 'Бежим через дворы!':
        text = ' Я решил побежать через двора, лишний риск уж сейчас то мне точно не нужен. Я близок к цели! Я ' \
               ' спасу их всех! Пробегая через дворы, я увидел как один вражеский воин угрожает мирному жителю ' \
               ' за то, что тот не пускает его в дом. Стоит ли мне вмешаться?'
        new_button_text_1 = 'Конечно, надо защитить жителя!'
        new_button_text_2 = 'Нет, твоя цель куда важнее!'
    # ------------------------- #
    if user_input == 'Защитим дом и потом спасём семью!':
        if energy is True and got_new_sword is True and dog is True and warriors is True:
            text = 'Обхватив свой меч, я вместе с союзниками начал сражаться с захватчиками! Я был полон сил и ' \
                   ' бился как только мог! Кое как мы начали побеждать в этой битве, хотя против нас приходило все ' \
                   ' больше и больше врагов.. Часть моих союзников погибла..их смерть будет ненапрасной. Ещё через' \
                   ' какое то время я и вовсе остался один, только Акира пытался бросаться на оставшихся противников.' \
                   ' И тут..Я услышал горн союзной армии. Не передать словами как я был рад.. Думаю пора идти к дому ' \
                   ' моего Господина. Обессиленный я, зайдя в дом, увидел прячущихся под столом детей Господина и его' \
                   ' жену. Сказав им, что союзная армия уже вошла в город и отвоёвывает его обратно, я сказал что ' \
                   ' дело осталось за малым, дождаться союзников и вместе с ними вернуться в другое поселение. ' \
                   ' Я услышал стук в дверь... Откроем?'
            new_button_text_1 = 'Да, открывай'
            new_button_text_2 = 'Нет, слишком рано для союзников'
        elif energy is False and got_new_sword is False and warriors is False:
            text = 'Я решил вступить в бой.. Преимущество было явно не на моей стороне.. Я один, против нападающих.' \
                   ' Битва будет не из лёгких.. Храбро сражаясь, я почувствовал сильную усталость, я слишком мало ' \
                   ' отдыхал и уже по пути сюда успел устать. Моя катана сломалась из-за того что я ' \
                   ' заблокировал удар слишком плохо. Я безоружен. И тут, я слышу горн союзного войска. ' \
                   ' Но похоже, что мне это не поможет, я оказался в слишком тяжелой ситуации.. Я получил ранение.. ' \
                   ' Ранение глубокое, прямо в живот... В глазах всё темнеет и похоже что это конец... \n ' \
                   ' Всё, это последняя страница. Прибывшие союзники успели записать его последние слова. Грустная ' \
                   ' история конечно, но такова жизнь.' \
                   ' Не всегда истории заканчиваются хорошо. Что на счёт семьи Господина, их спасли союзные войска.' \
                   ' Думаю можно сказать, что их спасли только потому что Такэо до последнего вздоха защищал их дом. ' \
                   ' Да, он погиб, но свой долг выполнил. Вот как-то так. Понравилась история?'
            new_button_text_1 = 'Да, неплохая история.'
            new_button_text_2 = 'Нет, Такэо жаль.'
        else:
            text = 'Я решил вступить в бой.. Преимущество было явно не на моей стороне.. Я один, против нападающих.' \
                   ' Битва будет не из лёгких.. Храбро сражаясь, я почувствовал сильную усталость, бой был тяжелый. ' \
                   ' Моя катана сломалась из-за того что я заблокировал удар слишком плохо. Я безоружен... И тут, я' \
                   ' слышу горн союзного войска. Но похоже, что мне это не поможет, я оказался в слишком тяжелой ' \
                   ' ситуации.... Я получил ранение.. Ранение глубокое, прямо в живот... В глазах всё темнеет и ' \
                   ' похоже что это конец... \n Всё, это последняя страница.' \
                   ' Прибывшие союзники успели дописать это в его личный дневник. Грустная история конечно, ' \
                   ' но такова жизнь. Не всегда истории заканчиваются хорошо. Что на счёт семьи Господина, ' \
                   ' их спасли союзные войска. Думаю можно сказать, что их спасли только потому что Такэо до ' \
                   ' последнего вздоха защищал их дом. Да, он погиб, но свой долг выполнил. Вот как-то так. ' \
                   ' Понравилась история?'
            new_button_text_1 = 'Да, неплохая история.'
            new_button_text_2 = 'Нет, Такэо жаль.'
    if user_input == 'Выведем их через двор!':
        text = ' Я решил тихо зайти к ним в дом и вывести их через задний двор. Где то есть тайный проход, который' \
               ' ведёт в горы близь моего поселения... Аккуратно открыв дверь, я зашёл в главный зал и увидел' \
               ' прячущихся под столом детей Господина и его жену. Они узнали меня и тихо пошли за мной. Выйдя из ' \
               ' дома, я вспомнил о местонахождении тайного туннеля в горы.. Он находился в маленькой пристройке к ' \
               ' основному дому. Зайдя туда, мы почувствовали облегчение, ведь самое страшное позади. Дальше, идя ' \
               ' по сырому и тёмному туннелю, мы почувствовали дикий холод. Мы были в горах. Выйдя из туннеля мы ' \
               ' решили сразу побежать к моему поселению... После долгой пробежки мы оказались в безопасности. ' \
               ' Я сразу же написал письмо Господину о том, что его семья сейчас в безопасности и находится под моей ' \
               ' защитой. Зайдя в поселение, нас встретило тёплое солнце и холодный ветер. На горизонте горел город. ' \
               ' Союзные войска позже отбили его, а беженцы от туда заполонили на какое то время наши улицы. ' \
               ' Господин был крайне благодарен за спасени его семьи. На этом история подходит к концу, я рад что ' \
               ' смог дописать её в свой дневник. На этом я прощаюсь. Такэо 1625 год, месяц сацуки. \n Ну, ' \
               ' как тебе, понравилась история?'
        new_button_text_1 = 'Да, неплохая история.'
        new_button_text_2 = 'Нет, мне не по душе хорошие концовки.'
    # ------------------------- #
    if user_input == 'Конечно, надо защитить жителя!':
        text = 'Собравшись с силами и обхватив свой клинок, я победил противника одним точным ударом. Сказав ' \
               ' жителю, что всё хорошо и теперь ему ничего не угрожает, он поблагодарил меня и я услышал плачь. ' \
               ' Спросив всё ли хорошо, в ответ я услышал о том, что им теперь некуда идти и у них совсем нет денег. ' \
               ' Может я смогу им чем-то помочь?'
        new_button_text_1 = 'Да, давай поможем им'
        new_button_text_2 = 'Нет, мы и так уже помогли, нам надо спешить.'
    if user_input == 'Нет, твоя цель куда важнее!':
        text = ''
        new_button_text_1 = ''
        new_button_text_2 = ''
    if user_input == 'Да, давай поможем им':
        if money is True:
            text = 'Я протянул им удачно подобранный кошелёк с монетами в их дрожащие от страха и горя руки. ' \
                   ' Они были крайне мне благодарны, но теперь мне надо идти дальше... Подбегая к дому моего ' \
                   ' Господина, я вижу как его окружили враги. Что же мне стоит сделать, защитить дом и потом ' \
                   ' спасти семью или обойти их и так же спасти семью Господина уйдя с ними через дворы?'
        else:
            text = 'Я отдал им все свои деньги, думая что для меня они сейчас куда менее ценны чем для них. ' \
                   ' Надеюсь у них всё будет хорошо. Подбегая к дому моего Господина, я вижу как его окружили враги. ' \
                   ' Что же мне стоит сделать, защитить дом и потом спасти семью или обойти их и так же спасти семью ' \
                   ' Господина уйдя с ними через дворы?'
        new_button_text_1 = 'Защитим дом и потом спасём семью!'
        new_button_text_2 = 'Выведем их через двор!'
    # ------------------------- #
    if user_input == 'Да, открывай':
        text = 'Я решил открыть дверь. Как только я сделал это, меня проткнули мечом... Я упал на колени, заслонив' \
               ' собой дверь, чтобы её было тяжелее открыть. Я слышал коней рядом, надеялся что это союзники...' \
               ' Но увы, это были захватчики.. Через некоторое время дверь проломили, а у меня не было сил сделать ' \
               ' хоть что то... Я слышу крики семьи Господина... Их куда то забирают.. Я не справился со своей ' \
               ' задачей, я подвел Господина и его семью... \n На этом всё, это была последняя страница...' \
               ' Эту запись со слов одного из членов семьи Господина, которого не нашли и не забрали в плен, ' \
               ' дописали в дневник союзники, которые успешно отбили это поселенее. Что было потом, информации нет..' \
               ' Ну как, понравился рассказ?'
        new_button_text_1 = 'Да, неплохая история.'
        new_button_text_2 = 'Нет, Такэо жаль.'
    if user_input == 'Нет, слишком рано для союзников':
        text = 'Я понял, что это были не союзники и принялся баррикадировать дом. Я заставил все двери и окна ' \
               ' шкафами, столами, вообщем всем что было. Мы начали ждать, когда союзные войска отобьют этот город. ' \
               ' Я был в полной уверенности что нас не тронут, ведь семью Господина им надо было скорее всего вязть ' \
               ' в плен. Еды в погребе было более чем достаточно для того чтобы прожить несколько дней. Спустя 2 дня' \
               ' в полной изоляции мы услышали горн прям около нашего дома.. Я узнал его, это был горн союзников. ' \
               ' Но вот в чём вопрос, сами союзники ли в него протрубили или его взяли захватчики в целях выманить' \
               ' нас.. Но особо выбора не было, еда заканчивалась, а угроза нет. Надо было решать. Я решил открыть ' \
               ' дверь максимально аккуратно и сам был в боевой готовности. Это были союзники... Не передать ' \
               ' словами те эмоции что я ощутил. Семью Господина забрали и отвезли к нему, а мне оставили еду и ' \
               ' лошадь, чтобы я сам добрался до дома. Дальше, после спокойной дороги домой, я вернулся в своё ' \
               ' любимое поселение. Меня встречало тёплое солнце и холодный ветер. \n На этом всё, это была ' \
               ' последняя страница. Как тебе история? Понравилась?'
        new_button_text_1 = 'Да, неплохая история.'
        new_button_text_2 = 'Нет, мне не по душе хорошие концовки.'
    # ------------------------- #
    if user_input == 'Да, неплохая история.':
        text = 'Мне тоже понравилась эта история. Да, она не самая длинная, но тем не менее она помогает ' \
               ' скоротать время. До встречи, дорогой слушатель! Если найду ещё чьи то истории, то обязательно ' \
               ' расскажу тебе!'
        new_button_text_1 = 'До встречи!'
        new_button_text_2 = 'Прощай!'
    if user_input == 'Нет, мне не по душе хорошие концовки.':
        text = 'Понимаю твоё мнение, история не из самых длинных, не из самых проработанных, ' \
               ' но тем не менее, лично у меня она вызвала положительные эмоции, как после ' \
               ' прослушивания короткого, хорошего рассказа. До встречи, дорогой слушатель! ' \
               ' Если найду ещё чьи то истории, то обязательно расскажу тебе!'
        new_button_text_1 = 'До встречи!'
        new_button_text_2 = 'Прощай!'
    if user_input == 'Нет, Такэо жаль.':
        text = 'Понимаю твои эмоции, мне тоже жаль его... Но ведь сама история то не из самых плохих, да, она не ' \
               ' самая длинная, да она не самая проработанная, ' \
               ' но тем не менее, лично у меня она вызвала положительные эмоции, как после ' \
               ' прослушивания короткого, хорошего рассказа. До встречи, дорогой слушатель! ' \
               ' Если найду ещё чьи то истории, то обязательно расскажу тебе!'
        new_button_text_1 = 'До встречи!'
        new_button_text_2 = 'Прощай!'
    # ------------------------- #

    if user_input == 'Мне надо идти, пока!' or user_input == 'До встречи!' or user_input == 'Прощай!':
        text = 'Тогда пока!'
        end = 'true'

    return [text, new_button_text_1, new_button_text_2, new_button_text_3, end, got_new_sword, food, dog,
            extremely_little_food, injury, energy, money, warriors]
