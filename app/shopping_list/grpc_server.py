from concurrent import futures
import logging

import grpc
import shopping_list_pb2
import shopping_list_pb2_grpc
import models
import convert
import shopping_list.repository


class ShoppingList(shopping_list_pb2_grpc.ShoppingListServicer):
    def __init__(self):
        self.shopping_list_item_repository = shopping_list.repository.ShoppingListItemRepository()
        self.shopping_list: list[models.ShoppingListItem] = []

    def GetShoppingList(self, request, context):
        for item in self.shopping_list_item_repository.get_shopping_list():
            yield convert.item_to_pb2_item(item)

    def GetShoppingListItem(self, request, context):
        item = self.shopping_list_item_repository.get_item_by_uid(request.uid)
        return convert.item_to_pb2_item(item)

    def CreateShoppingListItem(self, request, context):
        item: models.ShoppingListItem = convert.pb2_new_item_to_item(request)
        uid: str = self.shopping_list_item_repository.create_item(item)
        return shopping_list_pb2.Uid(uid=uid)

    def UpdateShoppingListItem(self, request, context):
        item: models.ShoppingListItem = convert.pb2_item_to_item(request)
        updated_item = self.shopping_list_item_repository.update_item(item)
        return convert.item_to_pb2_item(updated_item)

    def DeleteShoppingListItem(self, request, context):
        uid = request.uid
        item = self.shopping_list_item_repository.delete_item(uid=uid)
        return convert.item_to_pb2_item(item)


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    shopping_list_pb2_grpc.add_ShoppingListServicer_to_server(ShoppingList(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
