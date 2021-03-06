from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters, CommandHandler, CallbackQueryHandler
from decouple import config
from finder import word_finder
import logging

logger = logging.getLogger('__main__')

updater = Updater(token=config('BOT_TOKEN'))


def start(update: Update, context: CallbackContext):
    Welcome_message = f"""سلام {update.message.chat.first_name}
خیلی خوش اومدی!
برای یادگرفتن اینکه چجوری با من کار کنی روی /help بزن تا بیشتر بهت توضیح بدم😌
"""
    context.user_data['game_mode'] = 'vaajoor'
    first_name = update.message.chat.first_name if update.message.chat.first_name is not None else ''
    last_name = update.message.chat.last_name if update.message.chat.last_name is not None else ''
    username = update.message.chat.username
    context.bot.send_message(chat_id=update.effective_chat.id, text=Welcome_message)

    # log starts in channel
    context.bot.send_message(chat_id=config('CHANNEL_ID'),
                             text=f'{first_name} {last_name} with username @{username} started bot.',
                             disable_notification=True)
    # log starts in logger
    logger.info(
        f'{first_name} {last_name} with username {username} started bot')


def help(update: Update, context: CallbackContext):
    help_message = f"""
❇️برای کار با من کافیه کلماتی که دقیقا جاشون رو میدونی رو به شکل زیر(مثلا میدونی حرف اول نون هست و حرف دوم الف):
ن 1
ا 2
و حروفی که میدونی تو کلمه هستن اما جاشون رو نمیدونی رو به شکل زیر:
د
و حروفی که تو کلمه نیستن رو به شکل زیر به من بدی:
حمکف -

⚠️حواست باشه هرکدوم رو تو یک خط جدا وارد کنی و برای حروفی که تو کلمه نیستن حتما خط فاصله رو بعدشون بزنی.

با دستور /mode هم میتونی حالت بازی رو تغییر بدی.
امیدوارم از بازی لذت ببری🏆😍
"""
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_message)


def about(update: Update, context: CallbackContext):
    about_message = f"""
خوشحال میشم اگر در راستای بهتر شدنم پیشنهادات رو به @SadjadEb بگی.
سورس کد من روی گیتهاب از طریق آدرس زیر در دسترسه:
https://github.com/sadjadeb/wordle_vaajoor_helper
خوشحال میشم با دادن ⭐️ ازم حمایت کنین.
"""
    context.bot.send_message(chat_id=update.effective_chat.id, text=about_message)


def split_input(lines):
    exact = {}
    contains = []
    not_contains = []
    for line in lines:
        line_content = line.split(' ')
        if len(line_content) == 2:
            if line_content[1][0] == '-':
                for character in line_content[0]:
                    not_contains.append(character)
            else:
                exact[int(line_content[1][0]) - 1] = line_content[0].lower()
        elif len(line_content) == 1:
            contains.append(line_content[0][0].lower())
        else:
            raise ValueError

    return exact, contains, not_contains


def get_result(matched_words):
    if len(matched_words["result"]) > 100:
        result = """تعداد کلمه های پیدا شده با این ورودی خیلی زیاده😶
    مجبورم فقط ی بخشیش رو بهت نشون بدم😔
    """
        result += '\n'.join(matched_words["result"][:80])
    elif len(matched_words["result"]) == 0:
        result = "متاسفانه هیچ کلمه ای پیدا نشد😢"
    elif len(matched_words["result"]) == 1:
        result = f"""فقط یک کلمه پیدا شد که احتمالا جوابه😁
    ||{matched_words["result"][0]}||"""
    else:
        result = f'{matched_words["result_count"]} تا کلمه پیدا شد:\n'
        result += '\n'.join(matched_words["result"])

    return result


def find(update: Update, context: CallbackContext):
    if update.message is None:
        return

    try:
        lines = update.message.text.splitlines()
        exact, contains, not_contains = split_input(lines)

        game_mode = context.user_data.get('game_mode', 'vaajoor')
        matched_words = word_finder(game_mode, exact, contains, not_contains)

        result = get_result(matched_words)

        first_name = update.message.chat.first_name if update.message.chat.first_name is not None else ''
        last_name = update.message.chat.last_name if update.message.chat.last_name is not None else ''
        username = update.message.chat.username
        inlined_input = update.message.text.replace('\n', ' ')
        logger.info(
            f'{first_name} {last_name} - @{username} sent {inlined_input}')
    except:
        result = 'لطفا پیامت رو تو فرمتی که من میفهمم وارد کن\!😖'

    context.bot.send_message(chat_id=update.effective_chat.id, text=result,
                             reply_to_message_id=update.message.message_id, parse_mode=ParseMode.MARKDOWN_V2)


def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="ببخشید من این دستوری که زدی رو نمیفهمم🥲")


def mode(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [InlineKeyboardButton("Wordle", callback_data='wordle')],
        [InlineKeyboardButton("Vaajoor", callback_data='vaajoor')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('لطفا بازی رو انتخاب کن:', reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    query.answer()
    context.user_data['game_mode'] = query.data
    query.edit_message_text(text=f"حالت بازی: {query.data}")


handler_objects = [
    CommandHandler('start', start),
    CommandHandler('help', help),
    CommandHandler('about', about),
    CommandHandler('mode', mode),
    CallbackQueryHandler(button),
    MessageHandler(Filters.text & (~Filters.command), find),
    MessageHandler(Filters.command, unknown),
]


def run_bot():
    for handler in handler_objects:
        updater.dispatcher.add_handler(handler)
    updater.start_polling()
    updater.idle()
