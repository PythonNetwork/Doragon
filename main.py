from loguru import logger
from bot.dispatcher import updater, jobq

logger.add("logs/{time}.log", rotation='00:00')
updater.start_polling()
jobq.start()
logger.info("Doragon is now running")
updater.idle()