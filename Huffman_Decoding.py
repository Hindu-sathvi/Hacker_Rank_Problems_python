#Huffman Decoding
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
def decode_huff(root, s):
    decoded_string = ""
    current = root
    for char in s:
        if char == '0':
            current = current.left
        else:
            current = current.right
        
        if current.left is None and current.right is None:
            decoded_string += current.symbol
            current = root
    
    return decoded_string
root = Node(None, None)
root.left = Node(None, None)
root.right = Node(None, 'A')
root.left.left = Node(None, 'B')
root.left.right = Node(None, 'C')
encoded_string = "1001011"
decoded_string = decode_huff(root, encoded_string)
print(decoded_string)
