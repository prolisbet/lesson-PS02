import requests

img = "https://cs14.pikabu.ru/post_img/big/2023/01/09/10/1673284598156298028.jpg"

response = requests.get(img)

with open("test.jpg", "wb") as file:
    file.write(response.content)
