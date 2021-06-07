# importações
from instabot import Bot  # pip install instabot
from time import localtime
import time

# variáveis globais 
igBot = Bot()
files = list()

# funções
def postFileOnInstagram(): # função que faz os uploads para o instagram
    for index in files:
        while True:
            if (f'{localtime().tm_hour}:{localtime().tm_min}' in files[files.index(index)]['time']):
                try:
                    igBot.upload_photo(files[files.index(index)]['name'], caption = files[files.index(index)]['caption'] or '')
                    time.sleep(120)
                    break
                except Exception as error:
                    time.sleep(120)
                    break


def addFiles(): # função que coloca informações no sistema
    while True:
        name = str(input('nome do arquivo: '))
        schedule = str(input('horário do post: '))
        caption = str(input('legenda: '))
        addMore = str(input('Continuar? (S/N) '))

        if(addMore in ['s', 'S'] and len(name) > 0 and len(schedule) > 0):
            files.append({'name' : name, 'time' : schedule, 'caption' : caption})
        elif(addMore in ['n', 'N'] and len(name) > 0 and len(schedule) > 0): 
            postFileOnInstagram() 
            break
        else:
            print('desculpa não entendi')
            break


def instagramLog(): # função que loga no instagram
    try:
        login = str(input('nome da conta: '))
        password = str(input('senha: '))

        if(len(login) > 0 and len(password) > 0):
            igBot.login(username = login, password = password)
            addFiles()
    except:
        print('não foi possível concluir')

# chamada de funções
instagramLog()