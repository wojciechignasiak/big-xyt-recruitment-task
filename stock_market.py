from stock_market_abc import StockMarketABC
from order_model import OrderModel
from error_logging import logger
from typing import (
    List,
    Tuple,
    Set
)

class StockMarket(StockMarketABC):

    def __init__(self) -> None:
        self.all_orders: Tuple[OrderModel] = ()
        self.filtered_orders: Tuple[OrderModel] = ()

    def place_order(self, order: OrderModel) -> None:
        try:
            self.all_orders = self.all_orders + (order,)
            self.filtered_orders = self.__filter_orders()
            self.__print_orders_sum()
            self.filtered_orders = ()
        except Exception as e:
            logger.error(f"StockMarket.place_order() Error: {e}")
            print("Error occurred during placing order.")


    def __filter_orders(self) -> Tuple[OrderModel]:
        try:
            filtered_orders: List[OrderModel] = list(self.all_orders)
            indexes_to_delete: Set = set()

            for index, order in enumerate(self.all_orders):
                if order.type == "Remove":

                    indexes_to_delete.add(index)
                    search_order: OrderModel = OrderModel(
                        id=order.id,
                        order=order.order,
                        type="Add",
                        price=order.price,
                        quantity=order.quantity
                    )

                    index_of_order_to_remove: int = self.all_orders.index(search_order)

                    indexes_to_delete.add(index_of_order_to_remove)

            if indexes_to_delete:
                for index in sorted(indexes_to_delete, reverse=True):
                    del filtered_orders[index]

            return tuple(filtered_orders)
        except Exception as e:
            logger.error(f"StockMarket.__filter_orders() Error: {e}")
            print("Error occurred during filtering orders list.")

    def __print_orders_sum(self) -> None:
        try:
            buy_orders = tuple(filter(lambda x: x.order == "Buy", self.filtered_orders))
            if buy_orders:
                best_buy_price = min(buy_orders, key=lambda x: x.price).price
                sum_of_buy_orders = sum(order.quantity for order in buy_orders if order.price == best_buy_price)
            else:
                best_buy_price = 0
                sum_of_buy_orders = 0

            sell_orders = tuple(filter(lambda x: x.order == "Sell", self.filtered_orders))
            if sell_orders:
                best_sell_price = max(sell_orders, key=lambda x: x.price).price
                sum_of_sell_orders = sum(order.quantity for order in sell_orders if order.price == best_sell_price)
            else:
                best_sell_price = 0
                sum_of_sell_orders = 0

            print("-" * 50)
            print(f"Sum of Buy Orders with Best Price. Best buy price: {best_buy_price}, Quantity: {sum_of_buy_orders}")
            print(f"Sum of Sell Orders with Best Price. Best sell price: {best_sell_price}, Quantity: {sum_of_sell_orders}")
            print("-" * 50)

        except Exception as e:
            logger.error(f"StockMarket.__print_orders_sum() Error: {e}")
            print("Error occurred during counting best buy/sell and sum prices.")