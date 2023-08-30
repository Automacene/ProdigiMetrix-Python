#Abstract class for all API resources
from prodigi_metrix import METRIX_BASE
from typing import Dict, Any
from abc import ABC
import httpx

class Resource(ABC):

    def __init__(self, plugin_id: str, auth_token: str, resource_name: str):
        self.plugin_id = plugin_id
        self.auth_token = auth_token
        self.resource_name = resource_name
        self.url = f"{METRIX_BASE}/{self.resource_name}"

    async def _send(self, data: Dict[str, Any]):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(self.url, json=data, headers={"Authorization": f"Bearer {self.auth_token}"})
        except Exception as e:
            raise Exception(f"Could not log event: {e}")
        
        return response