'''
Given a positive integer n, write a function that returns the number of set bits

in its binary representation (also known as the Hamming weight).

 

Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128

Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.

Example 3:

Input: n = 2147483645

Output: 30

Explanation:

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

 
 100110
 011001

Constraints:

    1 <= n <= 231 - 1

 
Follow up: If this function is called many times, how would you optimize it?

'''



from TestFramework import TestFramework



def hamming_weight(n : int) -> int:
    return n if n == 0 or n == 1 else (n & 1) + hamming_weight(n >> 1)


def is_power_two(n : int) -> bool:
    return n > 0 and (n & (n - 1)) == 0


def hamming_weight_2(n : int) -> int:
    if n == 0 or n == 1:
        return n
    
    if is_power_two(n):
        return 1
    
    nb_bits = n.bit_length()
    milieu = nb_bits // 2   

    h1 = n >> milieu
    h2 = n & ((1 << milieu) - 1)
    
    return hamming_weight(h1) + hamming_weight(h2) 


def hamming_weight_kernighan(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count



test_cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 1),
        (5, 2),
        (7, 3),
        (8, 1),
        (9, 2),
        (15, 4),
        (16, 1),
        (31, 5),
        (32, 1),
        (63, 6),
        (64, 1),
        (127, 7),
        (128, 1),
        (255, 8),
        (256, 1),
        (1023, 10),
        (1024, 1),
        (2**20 - 1, 20),
        (2**20, 1),
    ]


# only sets bits
def worst_cases(max_bits):
    return [(1 << k) - 1 for k in range(1, max_bits + 1)]

# only power of two
def best_cases(max_bits):
    return [1 << k for k in range(max_bits)]

# alternance
def sparse_cases(max_bits):
    return [(1 << k) | 1 for k in range(1, max_bits + 1)]


MAX_BITS = 30

cases = {
    "worst": worst_cases(MAX_BITS),
    "best": best_cases(MAX_BITS),
    "sparse": sparse_cases(MAX_BITS),
}

fns = [
    hamming_weight,
    hamming_weight_2,
    hamming_weight_kernighan,
]

tf = TestFramework()

tf.add_test(hamming_weight, test_cases)

tf.run_tests()



for name, values in cases.items():
    print(f"\n=== {name.upper()} CASES ===")
    for fn in fns:
        t = tf.benchmark(fn, values)
        print(f"{fn.__name__:25s} {t:.6f}s")
