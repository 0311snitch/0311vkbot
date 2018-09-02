import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


def main():

    login, password = 'login', 'password'
    vk_session = vk_api.VkApi(login, password)
    vk = vk_session.get_api()

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():

        if event.type == VkEventType.MESSAGE_NEW:
            print('Новое сообщение:')

            if event.from_me:
                print('От меня для: ', end='')
            elif event.to_me:
                print('Для меня от: ', end='')

            if event.from_user:
                print(event.user_id)
            elif event.from_chat:
                print(event.user_id, 'в беседе', event.chat_id)
            elif event.from_group:
                print('группы', event.group_id)

            if event.text == 'Стас':
                vk.messages.send(chat_id=4, message='Сука')
            elif event.text == 'Саня':
                vk.messages.send(chat_id=4, message='Каблук')
            elif event.text == 'Серёга':
                vk.messages.send(chat_id=4, message='Ждун')
            elif event.text == 'Илюха':
                vk.messages.send(chat_id=4, message='Тефтеля')
            elif event.text == 'Антоха':
                vk.messages.send(chat_id=4, message='Кто такой Антоха?')
            elif event.text == 'Кирюха':
                vk.messages.send(chat_id=4, message='Сексальфач')

            print('Текст: ', event.text)
            print()

        else:
            print(event.type, event.raw[1:])


if __name__ == '__main__':
    main()