import time
import hmac
import hashlib
import requests
from urllib.parse import urlencode
from .logging_config import logger

class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://testnet.binancefuture.com"
    
    def _generate_signature(self, query_string: str) -> str:
        return hmac.new(
            self.api_secret.encode('utf-8'),
            query_string.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        
    def dispatch_request(self, method: str, endpoint: str, params: dict = None):
        if params is None:
            params = {}
            
        params['timestamp'] = int(time.time() * 1000)
        query_string = urlencode(params)
        signature = self._generate_signature(query_string)
        
        headers = {
            'X-MBX-APIKEY': self.api_key
        }
        
        url = f"{self.base_url}{endpoint}?{query_string}&signature={signature}"
        
        logger.debug(f"Sending {method} request to {endpoint}")
        
        try:
            if method == "POST":
                response = requests.post(url, headers=headers)
            elif method == "GET":
                response = requests.get(url, headers=headers)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
                
            response.raise_for_status()
            logger.debug(f"Response: {response.json()}")
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            error_data = response.json() if 'response' in locals() and response.content else str(http_err)
            logger.error(f"HTTP error occurred: {error_data}")
            raise Exception(f"API Error: {error_data}")
        except Exception as err:
            logger.error(f"Network/Other error occurred: {err}")
            raise Exception(f"Connection Error: {err}")
