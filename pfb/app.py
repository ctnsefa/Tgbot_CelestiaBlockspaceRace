from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests
import random

TOKEN = "6088434592:AAHYCTFzdDjv1r2QS7aVyTQzSdRzUpfeQhY"

def generate_random_hex(length=16):
    """Generates a random hex string."""
    return ''.join(random.choices('0123456789abcdef', k=length))

def start(update: Update, context: CallbackContext) -> None:
    update.effective_message.reply_text('Please enter the NODE IP address . (Example : 111.1.11.111) PLEASE MAKE SURE PORT 26659 IS OPEN!', reply_markup=ForceReply())

def explorer(update: Update, context: CallbackContext) -> None:
    update.effective_message.reply_text('https://testnet.mintscan.io/celestia-incentivized-testnet')

def website(update: Update, context: CallbackContext) -> None:
    update.effective_message.reply_text('https://celestia.org/')

def docs(update: Update, context: CallbackContext) -> None:
    update.effective_message.reply_text('https://docs.celestia.org/')

def node_info_received(update: Update, context: CallbackContext) -> None:
    ip = update.effective_message.text  # We only take the IP address now
    port = "26659"  # The port is now fixed
    namespace_id = generate_random_hex(16)  # 16-character random hex string for namespace_id
    data = generate_random_hex(50)  # 50-character random hex string for data

    payload = {
        'namespace_id': namespace_id,
        'data': data,
        'gas_limit': 80000,
        'fee': 2000
    }

    try:
        response = requests.post(f"http://{ip}:{port}/submit_pfb", json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        update.effective_message.reply_text(f"Request error warning: {str(e)}")
        return

    try:
        result = response.json()
    except ValueError as e:
        update.effective_message.reply_text(f"JSON Error: {str(e)}")
        return

    update.effective_message.reply_text(f"Result: {result}")

def main() -> None:
    updater = Updater(token=TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("explorer", explorer))
    dispatcher.add_handler(CommandHandler("website", website))
    dispatcher.add_handler(CommandHandler("docs", docs))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, node_info_received))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
