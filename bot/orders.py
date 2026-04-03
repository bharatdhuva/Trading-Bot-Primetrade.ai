from .client import BinanceFuturesClient
from .logging_config import logger

def place_order(
    client: BinanceFuturesClient, 
    symbol: str, 
    side: str, 
    order_type: str, 
    quantity: float, 
    price: float = None,
    stop_price: float = None
):
    """
    Executes a trade order via the Binance Futures Client wrapper.
    Supports MARKET, LIMIT, and STOP_MARKET orders.
    """
    endpoint = "/fapi/v1/order"
    params = {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": order_type.upper(),
        "quantity": str(quantity),
    }

    if order_type.upper() == "LIMIT":
        if not price:
            raise ValueError("Price is required for LIMIT orders.")
        params["price"] = str(price)
        params["timeInForce"] = "GTC"  # Good Till Cancelled
        
    elif order_type.upper() == "STOP_MARKET":
        if not stop_price:
            raise ValueError("Stop Price is required for STOP_MARKET orders.")
        params["stopPrice"] = str(stop_price)

    logger.info(f"Placing {order_type} order for {quantity} {symbol} ({side})")
    try:
        response = client.dispatch_request("POST", endpoint, params)
        logger.info(f"Order placed successfully: Order ID {response.get('orderId')}")
        return response
    except Exception as e:
        logger.error(f"Failed to place order: {e}")
        raise
