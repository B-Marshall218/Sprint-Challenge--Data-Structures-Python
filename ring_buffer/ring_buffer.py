

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest = None

    def append(self, item):
        # Return the number of items in storage
        length = len(self.storage)
        #  If there are no items in storage
        if length == 0:
            self.storage.append(item)
            self.oldest = 0
        #  If there is room to add items below capacity
        elif length < self.capacity:
            self.storage.append(item)
        # If storage is at capacity
        else:
            # Isolating the oldest item
            self.storage[self.oldest] = item
            # If the oldest item is less than what is capactity,
            # delete item in storage, and add item
            if self.oldest < self.capacity - 1:
                self.oldest += 1
            # If oldest item is going to be greater than capacity,
            # do not add item.
            else:
                self.oldest = 0

    def get(self):
        return self.storage
