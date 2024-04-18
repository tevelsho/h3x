# Hex Dumper

A tool for dumping hexadecimal content from files.
Features

    Dump hexadecimal content from a file.
    Print output to the terminal.
    Replace non-readable characters with '.'.

Installation

    Clone the repository:

    sh

git clone https://github.com/your-username/hexDumper.git

Navigate to the project directory:

sh

    cd hexDumper

Usage

css

python main.py <file_path> [-o|--output]

    <file_path>: Path to the input file.
    -o, --output: Print output to the terminal.

Example:

sh

python main.py input.txt -o

Example Output

mathematica

00000000: 48 65 6C 6C 6F 20 57 6F | 72 6C 64 21 0A 54 68 69 | Hello World!.Thi
00000010: 73 20 69 73 20 61 20 74 | 65 73 74 20 66 69 6C 65 | s is a test file
00000020: 20 66 6F 72 20 74 68 65 | 20 68 65 78 44 75 6D 70 |  for the hexDump
00000030: 65 72 20 74 6F 6F 6C 2E | 0A 0A 0A 0A 0A 0A 0A 0A | er tool.........

License

This project is licensed under the MIT License - see the LICENSE file for details.