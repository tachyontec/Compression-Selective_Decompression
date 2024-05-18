#!/bin/python3

from sys import argv
import math
import hashlib

with open(argv[1]) as f:  # Open file and save at s
    s = [int(i) for i in f.readlines()]

# -----------------l and u calculations----------------------
n = len(s)  # How many numbers we have
m = s[-1]  # maximum of the numbers is the last
ll = int(math.log(m / n, 2))  # int for round down

print("l " + str(ll))
L = bytearray(math.ceil(ll * n / 8))
# Number of zeros + number of ones /8 -> size of U
U = bytearray(int((m / math.pow(2, ll)) / 8) + math.ceil(n / 8))

for i in range(len(s)):  # For each number in main list
    # Split byte in parts we will add to L and U

    x = s[i] & (2 ** ll - 1)  # Last ll bits for L
    # L already has (i-1) numbers filled completely (8bits)
    bits_filled = i * ll  # Total bits filled
    pos = int(bits_filled / 8)  # Bytearray position to be filled
    bits_left = 8 - bits_filled % 8  # Bits left to use in pos
    size = ll  # Size of number we are adding in every loop (updated in)
    while x > 0:
        shift = bits_left - size  # shift to put number in the right place
        # We will keep all bits if we have enough space
        bits_to_keep = size - max(bits_left, 0)

        if shift >= 0:
            # We have enough space -> shifting left as much as possible to fit
            L[pos] += x << shift
            break  # x added
        else:
            # shift<0 -> number doesn't fit in that position
            # (-shift) bits doesn't fit in pos
            to_add = x >> (-shift)  # ignore those bits
            L[pos] += to_add  # Filling the whole 'pos' of bytearray
            size = size - bits_left  # Size of the number which is left
            # Now we don't need those bits
            x = x & (2 ** bits_to_keep - 1)  # so now again x will have 'size' bits
            bits_left = 8  # The next position is empty, so it has 8 bits left
            pos += 1  # Go to the next position (in case x still >0)

    # Rest number goes to U
    to_U = s[i] >> ll  # Ignore last ll bits which were added to L
    # We will add a 1 in the (k+i) bit (second method to fill U)
    bit = i + to_U  # Bit we want to make 1
    U[int(bit / 8)] += 1 << (8 - bit % 8 - 1)

# Printing:
print("L")
for i in L:
    print(bin(i)[2:].zfill(8))

print("U")
for i in U:
    print(bin(i)[2:].zfill(8))

m = hashlib.sha256()
m.update(L)
m.update(U)
print(m.hexdigest())

