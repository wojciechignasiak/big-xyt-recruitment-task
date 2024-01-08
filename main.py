from stock_market import StockMarket
from stock_market_abc import StockMarketABC
from order_model import OrderModel

def main():

    stock_market2: StockMarketABC = StockMarket()

    orders = [
    {"Id": "001", "Order": "Buy", "Type": "Add", "Price": 20.0, "Quantity": 100},
    {"Id": "002", "Order": "Sell", "Type": "Add", "Price": 25.0, "Quantity": 200},
    {"Id": "003", "Order": "Buy", "Type": "Add", "Price": 23.0, "Quantity": 50},
    {"Id": "004", "Order": "Buy", "Type": "Add", "Price": 23.0, "Quantity": 70},
    {"Id": "003", "Order": "Buy", "Type": "Remove", "Price": 23.0, "Quantity": 50},
    {"Id": "005", "Order": "Sell", "Type": "Add", "Price": 28, "Quantity": 100}
    ]
    
    for order in orders:
        order = {key.lower(): value for key, value in order.items()}
        order_model: OrderModel = OrderModel(**order)
        stock_market2.place_order(order_model)