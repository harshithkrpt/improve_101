import subprocess

# Run a simple command
result = subprocess.run(["echo", "Hello, world!"], capture_output=True, text=True)

print(result.stdout)  # "Hello, world!\n"

result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)

process = subprocess.run(
    ["grep", "world"],
    input="Hello world\nPython subprocess\n",
    text=True,
    capture_output=True
)
print(process.stdout)  # "Hello world"
