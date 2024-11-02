class Array:
    def __init__(self, capacity):
        """Initialize the array with a specified capacity."""
        self.capacity = capacity
        self.size = 0  # Logical size
        self.elements = [None] * capacity  # Physical storage

    def get(self, index):
        """Access an element at the specified index."""
        if 0 <= index < self.size:
            return self.elements[index]
        else:
            raise IndexError("Index out of bounds")

    def set(self, index, value):
        """Update the element at the specified index with a new value."""
        if 0 <= index < self.size:
            self.elements[index] = value
        else:
            raise IndexError("Index out of bounds")

    def append(self, value):
        """Add an element to the end of the array, resizing if necessary."""
        if self.size == self.capacity:
            self.resize(self.capacity * 2)  # Double the capacity
        self.elements[self.size] = value
        self.size += 1

    def resize(self, new_capacity):
        """Resize the array to a new capacity."""
        new_elements = [None] * new_capacity
        for i in range(self.size):
            new_elements[i] = self.elements[i]
        self.elements = new_elements
        self.capacity = new_capacity

    def shrink(self):
        """Decrease the array's size if necessary."""
        if self.size <= self.capacity // 4:
            self.resize(self.capacity // 2)

    def logical_equals_physical(self):
        """Check if logical size equals physical capacity and resize if true."""
        if self.size == self.capacity:
            self.resize(self.capacity * 2)

    def __str__(self):
        """Return a string representation of the logical contents of the array."""
        return str(self.elements[:self.size])

# Example usage:
if __name__ == "__main__":
    arr = Array(5)  # Create an array with a capacity of 5

    # Populate the array
    arr.append(10)
    arr.append(20)
    arr.append(30)
    arr.append(40)
    arr.append(50)

    print("Array after adding 5 elements:", arr)

    # Accessing elements
    print("Element at index 2:", arr.get(2))  # Output: 30

    # Modifying an element
    arr.set(2, 100)
    print("Array after modifying index 2:", arr)  # Output: [10, 20, 100, 40, 50]

    # Demonstrate resizing
    arr.append(60)  # This will trigger a resize
    print("Array after appending one more element (triggers resize):", arr)  # New capacity should be reflected

    # Check if logical size equals physical size
    arr.logical_equals_physical()
    print("Array after checking logical vs physical size:", arr)

    # Shrinking the array (example)
    arr.size = 2  # Simulating that only two elements are used
    arr.shrink()  # This will potentially shrink the capacity
    print("Array after shrinking:", arr)  # Check the new capacity and elements


