from twilio.rest import Client
import random
import os
from dotenv import load_dotenv

load_dotenv()

ToDo_List = ["Сходить за водой", "Вынести мусор", "Помыть посуду", "Помыть туалет", "Убирать у котов", "Пропылесосить",
             "Навести порядок в комнате", "Разобрать стол", "Протереть пыль в комнате"]

PHONE = os.getenv("MY_MOBILE_PHONE")  # Заменить на свои значения
SID = os.getenv("MY_TWILIO_SID")  # Заменить на свои значения
TOKEN = os.getenv("MY_TWILIO_TOKEN")  # Заменить на свои значения
client = Client(SID, TOKEN)


def Choose_ToDo(todo_list):
    list_today = []
    for i in range(2):
        random_choose = random.choice(todo_list)
        list_today.append(random_choose)
        todo_list.remove(random_choose)
    return list_today


def Send_sms(my_phone_num, list_today):
    T_PHONE = "+19167212583"  # Заменить на свои значения
    client.messages.create(
        to=my_phone_num,
        from_=T_PHONE,
        body="Задачи на сегодня: " + str(list_today).replace("[", " ").replace("]", " ")
    )


Temp = Choose_ToDo(ToDo_List)
Send_sms(PHONE, Temp)
