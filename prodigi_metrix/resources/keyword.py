from prodigi_metrix.resources.api_resource import Resource
from typing import List
import time

class Keyword(Resource):

    def __init__(self, plugin_id: str, auth_token: str):
        """
        Initializes a REST interface for logging keyword events to ProdigiLink Metrix.

        Parameters:
            plugin_id (str): The plugin ID.
            auth_token (str): The authorization token.
        """
        super().__init__(plugin_id, auth_token, "keyword")
    
    async def log(self, timestamp: int, keywords: List[str]):
        """
        Logs a keyword event.

        Parameters:
            timestamp (int): The unix timestamp of the event.
            keyword (str): The keyword.
        """
        try:
            assert isinstance(keywords, list)
        except:
            raise Exception("Keyword must be a list of strings.")
        
        data = {
            "plugin_id": self.plugin_id,
            "timestamp": timestamp,
            "keywords": keywords
        }
        return await self._send(data)

    async def log_now(self, keywords: List[str]):
        """Logs a keyword event and automatically generates the timestamp. """
        response = await self.log(int(time.time()), keywords)
        return response