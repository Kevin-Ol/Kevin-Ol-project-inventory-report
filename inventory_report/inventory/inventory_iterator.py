from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, products):
        self._products = products
        self._pos = 0

    def __next__(self):
        try:
            product = self._products[self._pos]
        except IndexError:
            raise StopIteration()
        else:
            self._pos += 1
            return product
