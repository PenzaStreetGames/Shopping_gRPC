from __future__ import print_function

import logging
import traceback

import grpc
import shopping_list_pb2
import shopping_list_pb2_grpc
import shopping_list.models as models
import convert


class GrpcClient:
    def __init__(self):
        self.host = "localhost:50051"

    def getShoppingList(self) -> list[shopping_list_pb2.ShoppingListItem]:
        with grpc.insecure_channel(self.host) as channel:
            stub = shopping_list_pb2_grpc.ShoppingListStub(channel)
            empty = shopping_list_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
            response = [convert.pb2_item_to_item(item) for item in stub.GetShoppingList(empty)]
        return response

    def getItemById(self, uid: str) -> shopping_list_pb2.ShoppingListItem:
        with grpc.insecure_channel(self.host) as channel:
            stub = shopping_list_pb2_grpc.ShoppingListStub(channel)
            response = stub.GetShoppingListItem(shopping_list_pb2.Uid(uid=uid))
        return convert.pb2_item_to_item(response)

    def createItem(self, item: models.ShoppingListItem) -> str:
        with grpc.insecure_channel(self.host) as channel:
            stub = shopping_list_pb2_grpc.ShoppingListStub(channel)
            pb2_item = convert.item_to_pd2_new_item(item)
            response = stub.CreateShoppingListItem(pb2_item)
        return response.uid

    def updateItem(self, item: models.ShoppingListItem) -> shopping_list_pb2.ShoppingListItem:
        with grpc.insecure_channel(self.host) as channel:
            stub = shopping_list_pb2_grpc.ShoppingListStub(channel)
            response = stub.UpdateShoppingListItem(convert.item_to_pb2_item(item))
        return convert.pb2_item_to_item(response)

    def deleteItem(self, uid) -> shopping_list_pb2.ShoppingListItem:
        with grpc.insecure_channel(self.host) as channel:
            stub = shopping_list_pb2_grpc.ShoppingListStub(channel)
            response = stub.DeleteShoppingListItem(shopping_list_pb2.Uid(uid=uid))
        return convert.pb2_item_to_item(response)


def run():
    grpc_client = GrpcClient()
    print("Welcome to CLI interface of gRPC Shopping List service")
    while True:
        line = input("> ")
        command, *args = line.split()
        try:
            match command:
                case "list":
                    items = grpc_client.getShoppingList()
                    if not items:
                        print([])
                    else:
                        print("[", *[item for item in items], "]", sep="\n")
                case "get":
                    uid = args[0]
                    item = grpc_client.getItemById(uid)
                    if item.uid != "":
                        print(item)
                    else:
                        print(f"no item with uid {uid}")
                case "create":
                    name, quantity, completed = args
                    quantity = int(quantity)
                    completed = completed == "true"
                    new_item = models.ShoppingListItem(
                        name=name, quantity=quantity, completed=completed)
                    uid = grpc_client.createItem(new_item)
                    if uid != "":
                        print(f"created with uid {uid}")
                    else:
                        print("creation failed")
                case "update":
                    uid, name, quantity, completed = args
                    quantity = int(quantity)
                    completed = completed == "true"
                    item = models.ShoppingListItem(
                        uid=uid, name=name,
                        quantity=quantity, completed=completed)
                    updated_item = grpc_client.updateItem(item)
                    if updated_item.uid != "":
                        print(f"updated: {updated_item}")
                    else:
                        print(f"no item with uid {uid}")
                case "delete":
                    uid = args[0]
                    item = grpc_client.deleteItem(uid)
                    if item.uid != "":
                        print(f"deleted: {item}")
                    else:
                        print(f"no item with uid {uid}")
                case "exit":
                    break
        except Exception as e:
            print(repr(e))
            print(traceback.format_exc())


if __name__ == '__main__':
    logging.basicConfig()
    run()
