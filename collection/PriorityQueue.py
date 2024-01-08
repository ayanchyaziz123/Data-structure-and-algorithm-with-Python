from queue import PriorityQueue
class PriorityQueueClass:
    def priorityQueue_operations(self):
        pq = PriorityQueue()
        pq.put(10)
        pq.put(30)
        pq.put(20)
        pq.put(40)

        while pq:
            element = pq.get()
            print(element)            

PriorityQueueClass().priorityQueue_operations()