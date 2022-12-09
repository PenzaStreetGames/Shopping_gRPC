import dataclasses


@dataclasses.dataclass
class ShoppingListItem:
    uid: str = None
    name: str = None
    quantity: int = None
    completed: bool = None
