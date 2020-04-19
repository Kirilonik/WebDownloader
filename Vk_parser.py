import requests
import os
import time


def take_Some_photos():
    version = 5.103
    token = "ee0cbef5ee0cbef5ee0cbef533ee7d9361eee0cee0cbef5b096227ad29d52f6cf1beed1"

    domian = "itpedia_youtube"
    offset, count = 0, 10
    all_posts = []

    count_posts = 120  # Количество постов которое нужно просмотреть

    while offset < count_posts:
        response = requests.get("https://api.vk.com/method/wall.get",
                                params={"access_token": token,
                                        "v": version,
                                        "domain": domian,
                                        "count": count,
                                        "offset": offset})

        data = response.json()['response']['items']
        offset += 10
        all_posts.extend(data)
        time.sleep(0.5)
    return all_posts


def file_writer(data):
    num = 1
    postNum = 0
    os.chdir("D://")
    os.makedirs("itpedia_youtube", exist_ok=True)
    for posts in data:
        postNum += 1
        try:
            for i in range(len(posts['attachments'])):
                with open(os.path.join("itpedia_youtube", str(postNum) + "_" + str(num) + ".png"), "wb") as file_photo:
                    resp = posts['attachments'][i]['photo']['sizes'][-1]['url']
                    resp_url = requests.get(resp)
                    resp_url.raise_for_status()
                    for chunk in resp_url.iter_content(200000):
                        file_photo.write(chunk)
                    print("Фото сохранено", num)
                    num += 1

        except KeyError:
            pass


all_post = take_Some_photos()
file_writer(all_post)

print("Done...")