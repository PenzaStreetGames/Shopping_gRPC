import shopping_list.models as models
import shopping_list_pb2


def item_to_pb2_item(item: models.ShoppingListItem) -> shopping_list_pb2.ShoppingListItem:
    return shopping_list_pb2.ShoppingListItem(
        uid=item.uid,
        name=item.name,
        quantity=item.quantity,
        completed=item.completed
    )


def item_to_pd2_new_item(item: models.ShoppingListItem) -> shopping_list_pb2.NewShoppingListItem:
    return shopping_list_pb2.NewShoppingListItem(
        name=item.name,
        quantity=item.quantity,
        completed=item.completed
    )


def pb2_new_item_to_item(pb_2_item: shopping_list_pb2.ShoppingListItem) -> models.ShoppingListItem:
    return models.ShoppingListItem(
        name=pb_2_item.name,
        quantity=pb_2_item.quantity,
        completed=pb_2_item.completed
    )


def pb2_item_to_item(pb_2_item: shopping_list_pb2.ShoppingListItem) -> models.ShoppingListItem:
    return models.ShoppingListItem(
        uid=pb_2_item.uid,
        name=pb_2_item.name,
        quantity=pb_2_item.quantity,
        completed=pb_2_item.completed
    )
