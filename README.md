APICore BASE - Все базовые продукты от студии APICore в одном Python пакете!

Пакет включает в себя продукты:
- NetI SDK - SDK Для зарегестрированных Нейросетевых моделей на портале APICore Technology

Пример использования:
from apicore.base import NetiSDK
neti = NetiSDK()
token = "key"
client = neti.client(
    model="NetI.FS-0.1",
    key=token
)
response = client.response(
    messages=[
        {
            "role": "user",
            "content": "Hello!"
        }
    ]
)
print(response.return_answer)

Также в client можно дописать пользовстельский эендпоинт чтобы выбранные модели брались оттуда
Чтобы получить API ключ от всех серий NetI, надо зайти на https://JDdijeyTwo.github.io/apicore-portal
И заполнить форму.
