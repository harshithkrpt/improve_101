# 🚀 Rust Setup Guide (Ubuntu + VS Code)

This guide will help you set up **Rust** on Ubuntu server with **VS Code extensions** for development.

---

## 1. Update your system
```bash
sudo apt update && sudo apt upgrade -y
```

---

## 2. Install dependencies
Rust requires build tools and curl:
```bash
sudo apt install -y build-essential curl pkg-config libssl-dev
```

---

## 3. Install Rust using rustup
Download and run the official Rust installer:
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

- Choose **1 (default installation)** when prompted.

---

## 4. Configure environment
Add Rust binaries to your shell session:
```bash
source $HOME/.cargo/env
```

Make it permanent:

- For **bash**:
  ```bash
  echo 'source $HOME/.cargo/env' >> ~/.bashrc
  ```
- For **zsh**:
  ```bash
  echo 'source $HOME/.cargo/env' >> ~/.zshrc
  ```

Reload:
```bash
exec $SHELL
```

---

## 5. Verify installation
```bash
rustc --version
cargo --version
```

✅ Expected output:
```
rustc 1.xx.x
cargo 1.xx.x
```

---

## 6. Install recommended Rust components
```bash
rustup component add rustfmt clippy
```

---

## 7. VS Code Setup

Install the following extensions:

- **Rust Analyzer** (language support & autocompletion)  
- **Rust Explorer** (project and crate explorer)  
- **CodeLLDB** (debugger)  
- **Even Better TOML** (TOML syntax highlighting)  

Install them via **VS Code Extensions Marketplace** or from terminal:

```bash
code --install-extension rust-lang.rust-analyzer
code --install-extension saadmk11.rust-explorer
code --install-extension vadimcn.vscode-lldb
code --install-extension bungcip.better-toml
```

---

## 8. Test a Rust Project

Create and run a test project:
```bash
cargo new hello-rust
cd hello-rust
cargo run
```

Expected output:
```
Hello, world!
```

---

🎉 You’re all set with Rust + VS Code tooling!