from SinglyLLImp import SinglyLLImp, Node
class ReverseLL:
    def reverseLL(self, head)-> Node:
        next = None
        prev = None
        while head is not None:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev    
    def printList(self, head)-> None:
        while(head!=None):
            print(head.data, end = " ")
            head = head.next

sl = SinglyLLImp()
sl.addNode(10)
sl.addNode(20)
sl.addNode(30)
sl.addNode(40)
sl.addNode(50)
head = sl.getHead()
rl = ReverseLL()
rl.printList(head)
head = rl.reverseLL(head)
print()
rl.printList(head)