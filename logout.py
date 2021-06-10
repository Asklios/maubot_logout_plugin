from maubot import Plugin


class Logout(Plugin):
    async def start(self) -> None:
        self.log.warning("Clearing all access tokens")
        await self.client.logout_all(True)
        exit()
