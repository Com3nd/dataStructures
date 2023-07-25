from __future__ import annotations
from typing import Any, Optional


class Node:

    def __init__(self, data: Any):
        self.data = data
        self.next_node: Optional[Node] = None

