from prodigi_metrix.resources.api_resource import Resource
from typing import List
import time

class Basic(Resource):

    def __init__(self, plugin_id: str, auth_token: str):
        """
        Initializes a REST interface for logging basic events to ProdigiLink Metrix.

        Parameters:
            plugin_id (str): The plugin ID.
            auth_token (str): The authorization token.
        """
        super().__init__(plugin_id, auth_token, "basic")

    async def log(self, timestamp: int):
        """
        Logs a basic event.

        Parameters:
            timestamp (int): The unix timestamp of the event.
        """
        data = {
            "plugin_id": self.plugin_id,
            "timestamp": timestamp
        }
        return await self._send(data)
    
    async def log_now(self):
        """Logs a basic event and automatically generates the timestamp. """
        return await self.log(int(time.time()))

    def log_buffer(self, timestamps: List[int]):
        #TODO: implement in backend
        pass

    def get(self):
        """Get the basic metrics for the plugin."""
        return self._get()