from collections.abc import MutableSequence

class MagicList(MutableSequence):
    """MagicList class"""
    def __init__(self, data=None):
        """Initialize the class"""
        super(MagicList, self).__init__()
        if (data is not None):
            self._list = list(data)
        else:
            self._list = list()

    def __repr__(self):
        return "<{0} {1}>".format(self.__class__.__name__, self._list)

    def __len__(self):
        """List length"""
        return len(self._list)

    def __getitem__(self, ii):
        """Get a list item"""
        return self._list[ii]

    def __delitem__(self, ii):
        """Delete an item"""
        del self._list[ii]

    def __setitem__(self, ii, val):
        """Set a list item"""
        if not len(self._list) and (ii == 0):
            self._list.append(val)
        else:
            self._list[ii] = val

    def __str__(self):
        return str(self._list)

    def insert(self, ii, val):
        # Insert an item in the list
        self._list.insert(ii, val)

    def append(self, val):
        self.insert(len(self._list), val)

if __name__ == "__main__":
    a = MyList()
    a[0] = 5
    print(a)
    b = MyList()
    b[1] = 5
    print(b)
