# Compression-Selective_Decompression
Elias-Fano compression implementation in Python, created for the Data Structures and Algorithms course. The script reads a list of integers from a file, compresses them into two bit arrays (L and U), and prints the compressed representation along with their SHA-256 hash.

## Overview
This Python script implements the Elias-Fano compression technique for a sorted list of integers. The program reads a list of integers from a file, compresses it using two bit arrays (L and U), and prints the compressed representations along with their SHA-256 hash.

## Features
- **Input Handling:** Reads integers from a specified input file.
- **Compression:** Compresses the integers using the Elias-Fano scheme into two bit arrays, L and U.
- **Output:** Prints the bit arrays L and U in binary format.
- **Hashing:** Generates and prints the SHA-256 hash of the concatenated bit arrays L and U.

## Files
- `elias_fano.py`: Main script containing the compression implementation.
- `README.md`: Documentation for the project.
- `example_*.txt` : Example input files used for testing.

## Requirements
- Python 3.x
- Required Libraries: `sys`, `math`, `hashlib`

## Usage
To run the script, use the following command:
```sh
python elias_fano.py <input_file>
```
where <input_file> is the path to the file containing the list of integers.

## Implementation Details

### Steps:

1. **Reading Input:** The script reads integers from the input file and stores them in a list.
2. **Calculating Parameters:**
    - `n`: Number of integers.
    - `m`: Maximum integer in the list.
    - `l`: Number of bits used for the least significant part, calculated as `int(math.log(m / n, 2))`.
3. **Creating Bit Arrays:**
    - `L`: Contains the last `l` bits of each integer.
    - `U`: Encodes the remaining bits in unary form.
4. **Populating Bit Arrays:**
    - The script splits each integer into parts for `L` and `U` and fills the respective bit arrays.
5. **Output:** Prints the bit arrays `L` and `U` in binary format and the SHA-256 hash of the concatenated arrays.
