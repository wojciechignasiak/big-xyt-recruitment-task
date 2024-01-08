from abc import (
    ABC, 
    abstractmethod
)
from order_model import OrderModel


class StockMarketABC(ABC):

    @abstractmethod
    def place_order(self, order: OrderModel) -> None:
        pass