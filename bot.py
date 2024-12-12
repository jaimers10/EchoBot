from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from config import BOT_TOKEN

# Función para manejar el comando /start
async def start(update: Update, context) -> None:
    await update.message.reply_text("¡Hola! Soy un bot Echo. Envíame un mensaje y lo repetiré.")

# Función para manejar mensajes de texto
async def echo(update: Update, context) -> None:
    await update.message.reply_text(update.message.text)

# Función principal para ejecutar el bot
def main():
    # Crear la aplicación con el token del bot
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Agregar el manejador para el comando /start
    app.add_handler(CommandHandler("start", start))

    # Agregar el manejador para mensajes de texto
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Ejecutar el bot
    app.run_polling()

if __name__ == "__main__":
    main()