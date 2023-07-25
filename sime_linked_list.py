from node import Node
from typing import Optional, Any


class SimpleLinkedList:

    def __init__(self):
        self.head: Optional[Node] = None

    def add(self, data: Any) -> None:
        if self.head is None:
            self.head = Node(data)
            return

        current_node = self.head
        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = Node(data)

    def remove_head(self):
        if self.head is not None:
            self.head = self.head.next_node

    def remove_tail(self):
        if self.head is not None:
            current_node = self.head
            previous_node = None
            while current_node.next_node is not None:
                previous_node = current_node
                current_node = current_node.next_node
            previous_node.next_node = None

    def to_list(self) -> list:
        node_values = []
        if self.head is None:
            return []

        current_node = self.head
        while current_node is not None:
            node_values.append(current_node.data)
            current_node = current_node.next_node
        return node_values


if __name__ == "__main__":
    my_list = SimpleLinkedList()
    my_list.add("Head Node")
    my_list.add("Second Node")
    my_list.add("third Node")
    my_list.add("forth Node")
    print(my_list.to_list())
    my_list.remove_head()
    my_list.remove_tail()
    print(my_list.to_list())


