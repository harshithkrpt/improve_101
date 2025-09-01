# Notes on Neural Network with Sigmoid Activation

## Network Structure
- **Input layer**: 728 nodes (flattened 28×28 grayscale image).
- **Hidden layers**: 2 layers, each with 16 neurons.
- **Output layer**: 10 neurons (digits 0–9).

---

## Core Concepts

### Nodes, Weights, and Edges
- Each **node** receives input from all nodes of the previous layer.
- Each connection (**edge**) carries a **weight**.
- Computation inside a neuron:
  \[
  z = \sum (w_i \cdot x_i) + b
  \]
  where:
  - \( w_i \): weights
  - \( x_i \): inputs
  - \( b \): bias (trainable constant)

### Activation Function (Sigmoid)
- The **sigmoid** squashes input into range (0, 1):
  \[
  \sigma(z) = \frac{1}{1 + e^{-z}}
  \]
- Adds **non-linearity** so the network can learn complex functions.
- For classification tasks:
  - Hidden layers often use **ReLU** in practice.
  - Output layer usually uses **softmax** for probability distribution.

### Bias
- Bias shifts the activation curve.
- Ensures a neuron can output a non-zero value even if all inputs are zero.

---

## Layer-by-Layer Flow
1. **Input layer (728)**: pixel intensities normalized between 0–1.
2. **Hidden Layer 1 (16 neurons)**: computes weighted sums of all 728 inputs, applies sigmoid.
3. **Hidden Layer 2 (16 neurons)**: computes from previous 16 outputs, applies sigmoid.
4. **Output layer (10 neurons)**: outputs class scores, then softmax → probabilities.

---

## Training Process
- **Forward pass**: inputs propagate through layers → predictions.
- **Loss function**: measures error (e.g., cross-entropy).
- **Backpropagation**: calculates contribution of each weight/bias to error.
- **Gradient descent**: updates weights/biases to minimize loss.

---

## Example Output
- Input: flattened digit image.
- Output (softmax applied):  
  ```
  [0.01, 0.05, 0.02, 0.03, 0.09, 0.80, 0.00, 0.00, 0.00, 0.00]
  ```
- Predicted digit: **5** (highest probability).

---

## Visual Representation

```mermaid
graph TD
    A[Input Layer: 728 nodes] --> B[Hidden Layer 1: 16]
    B --> C[Hidden Layer 2: 16]
    C --> D[Output Layer: 10 classes (0–9)]
```

---