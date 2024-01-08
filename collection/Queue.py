from queue import Queue
class QueueClass:
    def queueOperations(self):
        queue_list = Queue()
        #insert item in queue
        queue_list.put(10)
        queue_list.put(20)
        queue_list.put(30)
        # Dequeue (pop) an element
        data = queue_list.get()
        print(data)
        #print queue list
        while queue_list:
            print(queue_list.get())

q = QueueClass()
q.queueOperations()        



    