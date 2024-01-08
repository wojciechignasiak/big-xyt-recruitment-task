from dataclasses import dataclass

@dataclass
class OrderModel:
    __slots__ = (
        'id',
        'order',
        'type',
        'price',
        'quantity'
    )

    id: str
    order: str
    type: str
    price: float
    quantity: int
