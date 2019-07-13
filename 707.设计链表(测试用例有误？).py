class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        curr = self.head
        i = 0
        while curr and i <= index:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        node.next = self.head
        self.head = node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr:
                if curr.next is None:
                    curr.next = node
                else:
                    curr = curr.next

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        node = Node(val)
        curr = self.head
        # 如果是添加到头结点
        if index == 0:
            self.addAtHead(val)
        else:
            i = 0
            while i < index and curr:
                if i + 1 == index:
                    node.next = curr.next
                    curr.next = node
                    break
                else:
                    i += 1
                    curr = curr.next
            if i == index:
                curr = node


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if not self.head:
            return None
        i = 0
        curr = self.head.next
        pre = self.head
        while i <= index and curr:
            if i == index:
                pre.next = curr.next
                break
            else:
                pre = pre.next
                curr = curr.next





