import shopping_list.models as models
import uuid


class ShoppingListItemRepository:
    def __init__(self):
        self.shopping_list: list[models.ShoppingListItem] = []

    def get_shopping_list(self) -> list[models.ShoppingListItem]:
        return self.shopping_list

    def get_item_by_uid(self, uid: str) -> models.ShoppingListItem:
        for item in self.shopping_list:
            if item.uid == uid:
                return item
        return models.ShoppingListItem(uid="", name="", quantity=0, completed=False)

    def create_item(self, new_item: models.ShoppingListItem) -> str:
        uid = str(uuid.uuid4())
        new_item.uid = uid
        self.shopping_list.append(new_item)
        return uid

    def update_item(self, item: models.ShoppingListItem) -> models.ShoppingListItem:
        old_item = self.get_item_by_uid(item.uid)
        if old_item.uid == "":
            return old_item
        index = self.shopping_list.index(old_item)
        old_item.name = item.name
        old_item.quantity = item.quantity
        old_item.uid = item.uid
        old_item.completed = item.completed
        self.shopping_list[index] = old_item
        return old_item

    def delete_item(self, uid: str) -> models.ShoppingListItem:
        old_item = self.get_item_by_uid(uid)
        if old_item.uid == "":
            return old_item
        index = self.shopping_list.index(old_item)
        return self.shopping_list.pop(index)
