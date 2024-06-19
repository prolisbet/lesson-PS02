import requests
import pprint

params = {
    'q': 'JavaScript',
}

response = requests.get(
    'https://api.github.com/search/repositories',
    params=params)
# print(response.status_code)
# if response.ok:
#     print('запрос успешно выполнен')
# else:
#     # print('произошла ошибка')

# print(response.text)
response_json = response.json()
pprint.pprint(response_json['total_count'])
print(
    f"количество репозиториев с использованием js: "
    f"{response_json['total_count']}"
)