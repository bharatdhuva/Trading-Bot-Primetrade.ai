import sys
import os
from dotenv import load_dotenv
import questionary
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from bot.client import BinanceFuturesClient
from bot.orders import place_order
from bot.validators import validate_symbol, validate_positive_float

console = Console()

def print_summary(response: dict):
    if not response:
        return
        
    table = Table(title="Order Response Details")
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="magenta")

    fields_to_show = ["orderId", "symbol", "status", "clientOrderId", "price", "origQty", "executedQty", "avgPrice", "type", "side"]
    for field in fields_to_show:
        if field in response:
            table.add_row(field, str(response[field]))

    console.print(table)


def main():
    load_dotenv()
    api_key = os.getenv("BINANCE_TESTNET_API_KEY")
    api_secret = os.getenv("BINANCE_TESTNET_API_SECRET")

    if not api_key or not api_secret:
        console.print(Panel("[red]Missing API Credentials![/red]\nPlease set BINANCE_TESTNET_API_KEY and BINANCE_TESTNET_API_SECRET in a .env file or as environment variables."))
        sys.exit(1)

    console.print(Panel.fit("[bold green]Welcome to Binance Futures Testnet Trading Bot[/bold green]"))

    try:
        symbol = questionary.text(
            "Enter the trading symbol (e.g., BTCUSDT):",
            validate=lambda text: True if validate_symbol(text) else "Please enter a valid alphanumeric symbol."
        ).ask()

        if symbol is None: sys.exit(0)

        side = questionary.select(
            "Select order side:",
            choices=["BUY", "SELL"]
        ).ask()
        if side is None: sys.exit(0)

        order_type = questionary.select(
            "Select order type:",
            choices=["MARKET", "LIMIT"]
        ).ask()
        if order_type is None: sys.exit(0)

        quantity = questionary.text(
            "Enter quantity (e.g., 0.001):",
            validate=lambda text: True if validate_positive_float(text) else "Please enter a valid positive number."
        ).ask()
        if quantity is None: sys.exit(0)

        price = None
        if order_type == "LIMIT":
            price = questionary.text(
                "Enter price for LIMIT order:",
                validate=lambda text: True if validate_positive_float(text) else "Please enter a valid positive number."
            ).ask()
            if price is None: sys.exit(0)

        console.print(f"\n[bold]Order Summary Preview:[/bold]")
        console.print(f"Symbol: {symbol.upper()}")
        console.print(f"Side: {side}")
        console.print(f"Type: {order_type}")
        console.print(f"Quantity: {quantity}")
        if price:
            console.print(f"Price: {price}")
        
        confirm = questionary.confirm("Do you want to place this order?").ask()
        
        if confirm:
            client = BinanceFuturesClient(api_key, api_secret)
            with console.status("[bold green]Placing order...") as status:
                response = place_order(
                    client=client,
                    symbol=symbol,
                    side=side,
                    order_type=order_type,
                    quantity=float(quantity),
                    price=float(price) if price else None
                )
            console.print("\n[bold green]Order Request Successful![/bold green]")
            print_summary(response)
        else:
            console.print("[yellow]Order cancelled by user.[/yellow]")

    except KeyboardInterrupt:
        console.print("\n[yellow]Bot terminated.[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[bold red]Error:[/bold red] {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
