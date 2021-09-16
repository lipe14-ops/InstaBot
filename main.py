import getpass 
from instabot import Bot
from time import localtime, sleep
from dataclasses import dataclass
from enum import Enum, auto
from threading import Thread

class PostTypes(Enum):
    VIDEO = auto()
    IMAGE = auto()

@dataclass
class Post:
    file: str
    post_time: str
    post_type: PostTypes
    caption: str

@dataclass
class Client:
    account: str
    password: str
    posts = []

class InstagramHandler:
    """handle client's instagram account."""
    def __init__(self, client: Client) -> None:
        self.bot = Bot()
        self.account = client.account
        self.password = client.password
        self.bot.login(username=self.account, password=self.password)

    def post_feed(self, post: Post) -> None:
        """post image on instagram."""
        try:
            if post.post_type is PostTypes.IMAGE:
                self.bot.upload_photo(post.file, caption=post.caption)

            elif post.post_type is PostTypes.VIDEO:
                self.bot.upload_video(post.file, caption=post.caption)

            sleep(60)

        except FileNotFoundError:
            print('file not found.')


def set_client() -> Client:
    """define a client."""
    account = input('account: ')
    password = getpass.getpass('password: ')
    return Client(account, password)


def set_post(client: Client) -> None:
    """define a client post."""
    file = input('file: ')
    caption = input('caption: ')
    post_time = input('time: ')
    post_type = input('type: ').upper()

    if not post_time.isnumeric() and post_time.count(':') != 1:
        raise Exception('time not allowed format.')

    post = Post(file, caption, post_time, PostTypes[post_type])

    client.posts.append(post)


def get_time() -> str:
    """get the real time."""
    return f'{localtime().tm_hour}:{localtime().tm_min}'


def menu(client: Client) -> None:
    """creates a menu to control the bot."""
    while True:
        print('1. set new post\n2. exit')
        choice = input()

        try:
            if int(choice) == 1:
                set_post(client)

            elif int(choice) == 2:
                exit()

        except ValueError:
            print('i did not undestand.')


def main() -> None:
    client = set_client()
    Thread(target=menu, args=(client,)).start()

    insta_handler = InstagramHandler(client)

    while True:
        for post in client.posts:
            if get_time() == post.post_time:
                insta_handler.post_feed(post)


if __name__ == '__main__':
    main()