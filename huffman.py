import heapq
from collections import defaultdict
import os

class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoding:
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    def frequency_dict(self, text):
        frequency = defaultdict(int)
        for char in text:
            frequency[char] += 1
        return frequency

    def build_heap(self, frequency):
        for char, freq in frequency.items():
            node = Node(freq, char)
            heapq.heappush(self.heap, node)

    def merge_nodes(self):
        while len(self.heap) > 1:
            left = heapq.heappop(self.heap)
            right = heapq.heappop(self.heap)
            merged = Node(left.freq + right.freq, left=left, right=right)
            heapq.heappush(self.heap, merged)

    def build_codes(self, root, current_code=""):
        if root is None:
            return
        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return
        self.build_codes(root.left, current_code + "0")
        self.build_codes(root.right, current_code + "1")

    def encode(self, text):
        frequency = self.frequency_dict(text)
        print("Frequency Table:", frequency)
        self.build_heap(frequency)
        self.merge_nodes()
        root = self.heap[0]
        self.build_codes(root)
        encoded_text = "".join(self.codes[char] for char in text)
        return encoded_text

    def decode(self, encoded_text):
        current_code = ""
        decoded_text = ""
        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                decoded_text += self.reverse_mapping[current_code]
                current_code = ""
        return decoded_text


def compress_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        huffman = HuffmanCoding()
        encoded_text = huffman.encode(content)

        compressed_file = file_path + ".bin"
        with open(compressed_file, 'wb') as output:
            byte_array = int(encoded_text, 2).to_bytes((len(encoded_text) + 7) // 8, byteorder='big')
            output.write(byte_array)

        original_size = os.path.getsize(file_path)
        compressed_size = os.path.getsize(compressed_file)

        compression_ratio = original_size / compressed_size if compressed_size != 0 else 0

        print(f"Compression Ratio for {file_path}: {compression_ratio:.2f}")
        return compressed_file, compression_ratio
    except Exception as e:
        print(f"Error during compression: {e}")
        raise


if __name__ == "__main__":
    file_path = "C:/Users/Sumant Vetal/OneDrive/Documents/Windows installation.txt"
    try:
        compressed_file, ratio = compress_file(file_path)
        print(f"Compressed file saved at: {compressed_file}")
    except Exception as error:
        print(f"Failed to compress file: {error}")
