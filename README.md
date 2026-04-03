# Binance Futures Testnet Trading Bot

This is a simplified trading bot that can place MARKET and LIMIT orders on the Binance Futures Testnet (USDT-M) via direct REST API calls.
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
   .\\venv\\Scripts\\activate

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

The app will prompt you continuously through interactive menus:
1. Enter the Symbol (e.g., `BTCUSDT`)
2. Select BUY or SELL side
3. Select MARKET or LIMIT type
4. Enter quantity (e.g., `0.005`)
5. If LIMIT, enter the target price.
6. A summary will appear where you can confirm or cancel.

*Log Verification*:
To see the underlying HTTP requests and trace events, inspect the generated `bot.log` file in the root directory after running your first trade.

## Assumptions
- Only targeting Binance Testnet for USDT-M (base URL: `https://testnet.binancefuture.com`).
- The user is manually managing virtual environments and dependency instantiation.
- Only supporting Market and Limit order types for simplicity.
- Assuming `Good Till Cancelled (GTC)` implementation for all limit orders.
