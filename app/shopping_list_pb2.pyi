from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NewShoppingListItem(_message.Message):
    __slots__ = ["completed", "name", "quantity"]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    completed: bool
    name: str
    quantity: int
    def __init__(self, name: _Optional[str] = ..., quantity: _Optional[int] = ..., completed: bool = ...) -> None: ...

class ShoppingListItem(_message.Message):
    __slots__ = ["completed", "name", "quantity", "uid"]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    completed: bool
    name: str
    quantity: int
    uid: str
    def __init__(self, uid: _Optional[str] = ..., name: _Optional[str] = ..., quantity: _Optional[int] = ..., completed: bool = ...) -> None: ...

class Uid(_message.Message):
    __slots__ = ["uid"]
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: str
    def __init__(self, uid: _Optional[str] = ...) -> None: ...
