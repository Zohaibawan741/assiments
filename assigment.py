class UniqueIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.unique_set = set()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.iterable):
            element = self.iterable[self.index]
            self.index += 1
            if element not in self.unique_set:
                self.unique_set.add(element)
                return element
        raise StopIteration


# Test the UniqueIterator with a list containing duplicates
my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]

unique_iterator = UniqueIterator(my_list)

for unique_element in unique_iterator:
    print(unique_element)
