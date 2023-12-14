from SinglyLLImp import SinglyLLImp, Node
class MiddleNodeLL:
    def middleNode(self, head)-> Node:
        if head is None or head.next is None:
            return head
        slow = head
        fast = head
        while fast.next is not None and fast is not None:
            slow = slow.next
            fast = fast.next.next
        return slow    

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
ml = MiddleNodeLL()
ml.printList(head)
mid = ml.middleNode(head)
print()
print(mid.data)
