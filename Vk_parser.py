import requests
import os


def take_Some_photos():
    token = "ee0cbef5ee0cbef5ee0cbef533ee7d9361eee0cee0cbef5b096227ad29d52f6cf1beed1"
    version = 5.103
    domian = "ohthumbelina"
    offset = 0  # Смещение от 0 поста
    count = 199  # Количество отсмотренных постов
    all_posts = []
    while offset < 1000:
        response = requests.get("https://api.vk.com/method/wall.get",
                                params={"access_token": token,
                                        "v": version,
                                        "domain": domian,
                                        "count": count,
                                        "offset": offset})

        data = response.json()['response']['items']
        offset += 200
        all_posts.extend(data)
    return all_posts


def file_writer(data):
    num = 1
    os.chdir("D://")
    os.makedirs("Downloads", exist_ok=True)
    for posts in data:
        try:
            for i in range(len(posts['attachments'])):
                with open(os.path.join("Downloads", str(num) + ".png"), "wb") as file_photo:
                    resp = posts['attachments'][i]['photo']['sizes'][-1]['url']
                    resp_url = requests.get(resp)
                    resp_url.raise_for_status()
                    for chunk in resp_url.iter_content(100000):
                        file_photo.write(chunk)
                    print("Фото сохранено", num)
                    num += 1

        except KeyError:
            pass


all_post = take_Some_photos()
file_writer(all_post)

print("Done...")