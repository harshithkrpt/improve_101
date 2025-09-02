import torch
import matplotlib.pyplot as plt

print("Torch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())


words = open("names.txt", "r").read().splitlines()
print(words[:10])

# Create a set of all characters that appear in the words
chars = sorted(list(set(''.join(words))))
stoi = {s:i+1 for i,s in enumerate(chars)}
stoi['.'] = 0
itos = {i:s for s,i in stoi.items()}

# Create the Tensors
N = torch.zeros(27, 27, dtype=torch.int)

for w in words:
    complete_word = ['.'] + list(w) + ['.']
    for ch1, ch2 in zip(complete_word, complete_word[1:]):
        N[stoi[ch1], stoi[ch2]] += 1
