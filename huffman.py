from collections import deque

class Huffman:
    class HuffmanNode:
        def __init__(self, val, freq, next=None, left=None, right=None):
            self.val = val
            self.freq = freq
            self.next = next
            self.left = left
            self.right = right

    def __init__(self, file):
        with open(file, 'r') as f:
            self.data = f.read()
        self.freq_table = {}
        self.head = None
        self.root = None
        self.encodings = {}

    def build_freq_table(self):
        # Task 1
        pass

    def build_tree(self):
        # Task 2
        pass

    def encode(self, s):
        # Task 3
        pass

    def decode(self, code):
        # Task 4
        pass

    #
    # Note: you should NOT alter any of the following methods.
    # Doing so may hinder our ability to test your code.
    #

    # Create a new HuffmanNode and prepend it to the head of the linked list.
    def prepend_to_list(self, char, freq):
        new_node = Huffman.HuffmanNode(char, freq, next=self.head)
        self.head = new_node

    # Build the linked list of Huffman nodes from the frequency table.
    def build_list(self):
        sorted_freqs = sorted(self.freq_table.items(), key=lambda x:x[1], reverse=True)
        for char, freq in sorted_freqs:
            self.prepend_to_list(char, freq)

    # Insert a node into a sorted linked list referenced by self.head.
    # Helper method for build_tree().
    def insert_sorted(self, new_node):
        if self.head is None:
            self.head = new_node
            return

        prev = None
        trav = self.head

        # find the place in the list where the new node belongs
        while trav is not None and trav.freq < new_node.freq:
            prev = trav
            trav = trav.next

        if trav is None:
            # new node goes last in the sorted list
            prev.next = new_node
        else:
            # new_node goes between prev and trav
            prev.next = new_node
            new_node.next = trav

    # Recursive helper method to set the encodings
    # from the Huffman tree.
    def __compute_encodings(self, node, code):
        if node.left is None and node.right is None:
            # at a leaf node -- set the encoding
            self.encodings[node.val] = code

        if node.left is not None:
            self.__compute_encodings(node.left, code + '0')
        if node.right is not None:
            self.__compute_encodings(node.right, code + '1')

    # Set the encodings from the Huffman tree.
    def compute_encodings(self):
        self.__compute_encodings(self.root, '')

    # Build a Huffman tree.
    def build(self):
        self.build_freq_table()
        self.build_list()
        self.build_tree()
        self.compute_encodings()
