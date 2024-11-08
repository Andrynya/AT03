import requests

def get_random_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[0]['url']  # Возвращаем URL случайного изображения кошки
    else:
        return None

