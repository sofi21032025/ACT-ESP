class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def add_item(self, item):
        self.items.append(item)

    def out_item(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            raise IndexError("Desencolar de una cola vacía")

    def get_queue_len(self):
        return len(self.items)
    
def sum_queues(queue1, queue2):
    result_queue = Queue()
    while not queue1.isEmpty() or not queue2.isEmpty():
        result_queue.add_item(queue1.out_item() + queue2.out_item())
    return result_queue

Queue1 = Queue()
Queue2 = Queue()
Queue1.add_item(1)
Queue1.add_item(2)  
Queue1.add_item(3)
Queue2.add_item(4)
Queue2.add_item(5)
Queue2.add_item(6)
ResultQueue = sum_queues(Queue1, Queue2)
print(f"Elementos en la cola resultante: {ResultQueue.items}")