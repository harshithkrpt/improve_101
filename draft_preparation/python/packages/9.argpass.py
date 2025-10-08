import argparse

# Create a parser
parser = argparse.ArgumentParser(description="A simple greeter program")

# Add arguments
parser.add_argument("--name", required=True, help="Your name")
parser.add_argument("--age", type=int, default=18, help="Your age")

# Parse arguments
args = parser.parse_args()

# Use them
print(f"Hello {args.name}, you are {args.age} years old!")
