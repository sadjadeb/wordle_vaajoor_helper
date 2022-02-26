from webserver import run_webserver
from terminal import run_terminal
from telegram_bot import run_bot
import logging
from multiprocessing import Process

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("log.txt", encoding='utf-8'), logging.StreamHandler()])
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    run_mode = int(input('Enter run mode: 1 for terminal, 2 for webserver, 3 for telegram bot, 4 for all: '))
    if run_mode == 1:
        run_terminal()
    elif run_mode == 2:
        run_webserver()
    elif run_mode == 3:
        run_bot()
    elif run_mode == 4:
        p1 = Process(target=run_webserver)
        p1.start()
        p2 = Process(target=run_bot)
        p2.start()
    else:
        print('Error: run mode not acceptable')
        exit()
