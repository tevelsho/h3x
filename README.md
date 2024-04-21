# h3x

A tool for dumping hexadecimal content from files.

## ⭐ Upcoming features

         _     ____       
        | |   |___ \      
        | |__   __) |_  __
        | '_ \ |__ <\ \/ /
        | | | |___) |>  < 
        |_| |_|____//_/\_\
                   
                   

Currently **IN DEVELOPEMENT** as I work, fix and improve the code.  
Some future features include:
- More CLI Features
- Manipulation of bytes

## Installation


1. Clone the repository:

        git clone https://github.com/trevelling/hexDumper.git

2. Install the dependencies:

        pip install -r requirements.txt

3. Run the application:

        python3 app.py <file_path> [-o | --output]

## Usage

## Example

    python3 app.py test.png -o

    00000000: 48 65 6C 6C 6F 20 57 6F | 72 6C 64 21 0A 54 68 69 | Follow my GH!..}
    00000010: 73 20 69 73 20 61 20 74 | 65 73 74 20 66 69 6C 65 | N.@.k}w.._..l...
    00000020: 20 66 6F 72 20 74 68 65 | 20 68 65 78 44 75 6D 70 | ...Y.n..=H..X@.$
    00000030: 65 72 20 74 6F 6F 6C 2E | 0A 0A 0A 0A 0A 0A 0A 0A | .jz..r@z;..=%...
