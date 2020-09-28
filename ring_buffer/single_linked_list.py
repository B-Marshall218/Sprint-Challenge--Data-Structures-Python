class Ring:
    def _def_init_(self, value):
        self.value = value
        self.next_ring = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def _init_(self):
        self.head = None
        self.tail = None

    def add_tail_remove_head(self, value):
        new_node = Ring(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
        if self.head is None and self.tail is None:
            return None
        if self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            return value

    # def remove_head(self):
    #     if self.head is None and self.tail is None:
    #         return None
    #     if self.head == self.tail:
    #         value = self.head.get_value()
    #         self.head = None
    #         self.tail = None
    #         return value
    #     else:
    #         value = self.head.get_value()
    #         self.head = self.head.get_next()
    #         return value
