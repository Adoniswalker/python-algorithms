class ItemCollection:
    def __init__(self):
        self.collection = []

    def add(self, name):
        if name not in self.collection:
            self.collection.append(name)

    def remove(self, name):
        if name in self.collection:
            self.collection.remove(name)

    def getNames(self):
        return self.collection


def itemsCollection():
    obj = ItemCollection()
    return obj


if __name__ == '__main__':
    collection = itemsCollection()
    collection.add('Name')
    collection.add('Shirt')
    collection.add('Trouser')
    collection.add('Shirt')
    collection.remove('Shirt')
    collection.remove('Shirt')
    print(collection.getNames())
