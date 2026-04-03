# Binance Futures Testnet Trading Bot

This is a simplified trading bot that can place MARKET, LIMIT, and STOP_MARKET orders on the Binance Futures Testnet (USDT-M) via direct REST API calls.
It comes with an interactive CLI utilizing `questionary` and `rich` for great UX, fulfilling the bonus requirements.

## Project Structure
```text
trading_bot/
  bot/
    __init__.py
    client.py          # Binance testnet wrapper w/ HMAC signatures
    orders.py          # logic to execute trades
    validators.py      # Input validation
    logging_config.py  # File logging separated from CLI 
  cli.py               # Main entry point with interactive UI
  requirements.txt
```

## Setup Steps

1. Install Python 3.8+ if not already installed.
2. Clone this repository and navigate to the project directory.
   ```bash
   cd trading_bot
   ```
3. Create and activate a Virtual Environment.
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Create a `.env` file in the root directory:
   ```env
   BINANCE_TESTNET_API_KEY=your_testnet_api_key
   BINANCE_TESTNET_API_SECRET=your_testnet_api_secret
   ```

## How to Run Examples

Start the CLI application:

```bash
python cli.py
```

## Sample Output

Here is an example of what the interactive CLI UX looks like when placing a trade:

```text
╭────────────────────────────────────────────────╮
│ Welcome to Binance Futures Testnet Trading Bot │
╰────────────────────────────────────────────────╯
? Enter the trading symbol (e.g., BTCUSDT): BTCUSDT
? Select order side: BUY                           
? Select order type: MARKET          
? Enter quantity (e.g., 0.05): 0.05
                                   
Order Summary Preview:
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.05
? Do you want to place this order? Yes
                  
Order Request Successful!            
          Order Response Details
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Field         ┃ Value                  ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ orderId       │ 13020177998            │
│ symbol        │ BTCUSDT                │
│ status        │ NEW                    │
│ clientOrderId │ u4NlfUmexDI4VYQlYqd89p │
│ price         │ 0.00                   │
│ origQty       │ 0.0500                 │
│ executedQty   │ 0.0000                 │
│ avgPrice      │ 0.00                   │
│ type          │ MARKET                 │
│ side          │ BUY                    │
│ stopPrice     │ 0.00                   │
└───────────────┴────────────────────────┘
```

*Log Verification*:
To see the underlying HTTP requests and trace events, inspect the generated `bot.log` file in the root directory after running your trades.

## Assumptions
- Only targeting Binance Testnet for USDT-M (base URL: `https://testnet.binancefuture.com`).
- The user is manually managing virtual environments and dependency instantiation.
- Only supporting Market, Limit and Stop_Market order types for simplicity.
- Assuming `Good Till Cancelled (GTC)` implementation for all limit orders.
