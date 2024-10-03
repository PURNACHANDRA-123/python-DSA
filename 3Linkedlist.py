# Accessing: O(n) in the worst case (you might have to traverse the entire list). Unlike arrays, we can't directly access an element using its index.
# Searching: O(n) (linear search).
# Insertion (at the beginning - prepend): O(1).
# Insertion (at the end - append): O(n) because we need to find the last node first. (Question: How could we optimize appending?)
# Deletion: O(n) in the worst case (we have to find the node to delete). Deleting the head node is O(1).

class Node:
    def __init__(self, data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head = new_node
        else:
            last=self.head
            while last.next:
                last=last.next
            last.next=new_node

    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head  # Point the new node's next to the current head
        self.head=new_node  # Update the head to the new node

    def delete(self,key):
        temp = self.head
# If the head node itself holds the key to be deleted
        if temp is not None:
            if temp.data==key:
                self.head = temp.next   # Change head
                temp=None   # Free old head
                return 
        # Search for the key to be deleted
            
        while temp is not None:
            if temp.data==key:
                break
            prev=temp
            temp=temp.next

         # If the key was not present in the linked list
            if temp is None:
                    return

          #unlinking node
            prev.next=temp.next
            temp=None
    def print_func(self):
        current_node=self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
    def get_length(self):
        count=0
        current_node=self.head
        while current_node:
            count+=1
            current_node=current_node.next
        return count
    def search(self,target_value):
        cc_node=self.head

        while cc_node:
            if cc_node.data==target_value:
                return True
            cc_node=cc_node.next

        return False
            
ll=LinkedList()
ll.append(4)
ll.append(6)
ll.print_func()

ll.prepend(1)
ll.prepend(2)
ll.prepend(3)
ll.print_func()

ll.delete(2)
ll.print_func()


print(ll.get_length())

print(ll.search(9))
print(ll.search(3))