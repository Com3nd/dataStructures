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


if __name__ == "__main__":
    my_list = SimpleLinkedList()
    my_list.add("Head Node")
    my_list.add("Second Node")


