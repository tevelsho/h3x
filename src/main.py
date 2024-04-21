import argparse


def Main():
    parser = argparse.ArgumentParser(
        description="Hex Dumper is a versatile tool for dumping the hexadecimal content of files, offering additional features for enhanced functionality."
    )
    
    #CLI Arguements
    parser.add_argument("file", help="Specify the file to dump its hexadecimal content")
    parser.add_argument(
        "-o", "--output", help="Display the hexadecimal output to the terminal", action="store_true"
    )

    # Grab arguements from the command line
    args = parser.parse_args()

    # If user inputs a file
    if args.file:
        offset = 0
        with open(args.file, "rb") as infile:

            # Dumping out of hex values
            with open(args.file + ".dump", "w") as outfile:
                while True:
                    chunk = infile.read(16)  # Read 16 bytes of the file at a time
                    if len(chunk) == 0:  # Empty file
                        break

                    # Human readable text
                    text = str(chunk)

                    # Replace any non valid readable characters with valid characters
                    text = "".join(
                        [i if ord(i) < 128 and ord(i) > 32 else "." for i in text]
                    )

                    # Formatting
                    # TODO: Fix bug with ord(c)
                    output = "{:#08x}".format(offset) + ": "
                    output += " ".join("{:02X}".format(ord(c)) for c in chunk[:8])
                    output += " | "
                    output += " ".join("{:02X}".format(ord(c)) for c in chunk[8:])

                    # Padding
                    if len(chunk) % 16 != 0:
                        output += "   " * (16 - len(chunk)) + text
                    else:
                        output += " " + text

                    if args.output:
                        print(output)
                    outfile.write(output + "\n")

                    offset += 16  # Increase the bytes by 16
    else:
        print(parser.usage)

if __name__ == "__main__":
    Main()
