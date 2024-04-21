# HEX DUMPER

A tool for dumping hexadecimal content from files.

## ⭐ Upcoming features

    __ __    ___  __ __      ___    __ __  ___ ___  ____   ___  ____  
    |  |  |  /  _]|  |  |    |   \  |  |  ||   |   ||    \ /  _]|    \ 
    |  |  | /  [_ |  |  |    |    \ |  |  || _   _ ||  o  )  [_ |  D  )
    |  _  ||    _]|_   _|    |  D  ||  |  ||  \_/  ||   _/    _]|    / 
    |  |  ||   [_ |     |    |     ||  :  ||   |   ||  | |   [_ |    \ 
    |  |  ||     ||  |  |    |     ||     ||   |   ||  | |     ||  .  \
    |__|__||_____||__|__|    |_____| \__,_||___|___||__| |_____||__|\_|

Currently IN DEVELOPEMENT as I work, fix and improve the code.  
Some future features include:

- More CLI Features
- Manipulation of bytes

## Installation

1. Clone the repository:

        git clone https://github.com/trevelling/hexDumper.git

2. Navigate to the project directory:

        cd hexDumper

## Usage

        python main.py <file_path> [-o | --output]

        <file_path>: Path to the input file.
        -o, --output: Print output to the terminal.

## Example

    python3 main.py test.png -o

    00000000: 48 65 6C 6C 6F 20 57 6F | 72 6C 64 21 0A 54 68 69 | Follow my GH!..}
    00000010: 73 20 69 73 20 61 20 74 | 65 73 74 20 66 69 6C 65 | N.@.k}w.._..l...
    00000020: 20 66 6F 72 20 74 68 65 | 20 68 65 78 44 75 6D 70 | ...Y.n..=H..X@.$
    00000030: 65 72 20 74 6F 6F 6C 2E | 0A 0A 0A 0A 0A 0A 0A 0A | .jz..r@z;..=%...
