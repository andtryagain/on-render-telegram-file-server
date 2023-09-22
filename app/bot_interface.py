import logging
from urllib.parse import quote

from pyrogram import Client, filters
from pyrogram.types import Message

class PyrogramTelegramBotInterface:
    def __init__(
        self, 
        pyro_bot_client: Client,
        config: object,
        logger: logging.Logger,
        *args,
        **kwargs
    ) -> None:
        self.pyro_bot_client = pyro_bot_client
        self.config = config
        self.logger = logger

    def start(self):
        self.pyro_bot_client.start()
        self.listen()


    def stop(self):
        self.pyro_bot_client.stop()


    def listen(self):
        @self.pyro_bot_client.on_message(filters.command('start') & filters.private)
        async def start_handler(client, message: Message) -> None:
            await message.reply('started... send me your file to distribute and get the link :)')


        # TODO: validation and doc types

        @self.pyro_bot_client.on_message(filters.document & filters.private)
        async def doc_handler(client, message: Message) -> None:
            async def progress(current, total):
                self.logger.info(f"{current * 100 / total:.1f}%")

            file = await self.pyro_bot_client.download_media(message, in_memory=True, progress=progress)
            self.write_bytes_to_file(file)

            await message.reply(f'''file link:\n{self.config['URL_PAGE']}/{quote(file.name)}.\n\nwill be availible for 30 mins''')


    def write_bytes_to_file(self, file) -> None:
        file_name = file.name
        file_bytes = bytes(file.getbuffer())
        
        with open(f'files/{file_name}', 'wb') as f:
            f.write(file_bytes)