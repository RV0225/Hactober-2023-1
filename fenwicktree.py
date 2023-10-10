class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, idx, delta):
        # Add delta to the element at index idx and update the Fenwick Tree
        idx += 1
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def query(self, idx):
        # Compute the prefix sum up to index idx
        idx += 1
        result = 0
        while idx > 0:
            result += self.bit[idx]
            idx -= idx & -idx
        return result

# Example usage:
if __name__ == "__main__":
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = len(values)

    # Create a Fenwick Tree and initialize it with values
    fenwick = FenwickTree(n)
    for i in range(n):
        fenwick.update(i, values[i])

    # Query prefix sums
    print(fenwick.query(2))  # Output: 6 (1 + 2 + 3)
    print(fenwick.query(5))  # Output: 21 (1 + 2 + 3 + 4 + 5 + 6)
