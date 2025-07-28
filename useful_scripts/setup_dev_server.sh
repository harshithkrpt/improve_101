#!/bin/bash

set -e

echo "🚀 Starting Ubuntu Dev Server Setup..."

# Update packages
sudo apt update -y

# ----------------------------------------------------------
# Function to check if a package is installed
# ----------------------------------------------------------
is_installed() {
    dpkg -s "$1" &> /dev/null
}

# ----------------------------------------------------------
# 1. Install basic development tools
# ----------------------------------------------------------
for pkg in curl wget git build-essential ufw fail2ban; do
    if is_installed $pkg; then
        echo "✅ $pkg is already installed."
    else
        echo "📦 Installing $pkg..."
        sudo apt install -y $pkg
    fi
done

# ----------------------------------------------------------
# 2. Secure SSH
# ----------------------------------------------------------
echo "🔐 Configuring SSH security..."
sudo sed -i 's/#\?PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config
sudo sed -i 's/#\?PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config
sudo systemctl restart ssh

# ----------------------------------------------------------
# 3. Setup UFW Firewall
# ----------------------------------------------------------
if sudo ufw status | grep -q "active"; then
    echo "✅ UFW firewall is already enabled."
else
    echo "🔒 Enabling UFW firewall..."
    sudo ufw allow OpenSSH
    sudo ufw --force enable
fi

# ----------------------------------------------------------
# 4. Install Docker & Docker Compose
# ----------------------------------------------------------
if command -v docker &> /dev/null; then
    echo "✅ Docker is already installed."
else
    echo "🐳 Installing Docker..."
    sudo apt install -y docker.io docker-compose
    sudo systemctl enable docker
    sudo usermod -aG docker $USER
fi

# ----------------------------------------------------------
# 5. Install Node.js (LTS)
# ----------------------------------------------------------
if command -v node &> /dev/null; then
    echo "✅ Node.js is already installed."
else
    echo "📦 Installing Node.js LTS..."
    curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
    sudo apt install -y nodejs
fi

# ----------------------------------------------------------
# 6. Install VS Code Server
# ----------------------------------------------------------
if command -v code-server &> /dev/null; then
    echo "✅ VS Code Server is already installed."
else
    echo "🖥 Installing VS Code Server..."
    curl -fsSL https://code-server.dev/install.sh | sh
    sudo systemctl enable --now code-server@$USER
fi

# ----------------------------------------------------------
# 7. Install Tailscale
# ----------------------------------------------------------
if command -v tailscale &> /dev/null; then
    echo "✅ Tailscale is already installed."
else
    echo "🌐 Installing Tailscale..."
    curl -fsSL https://tailscale.com/install.sh | sh
    sudo tailscale up --ssh --accept-routes
fi

# ----------------------------------------------------------
# 8. Fail2Ban Setup
# ----------------------------------------------------------
if sudo systemctl is-active --quiet fail2ban; then
    echo "✅ Fail2Ban is already running."
else
    echo "🛡 Starting Fail2Ban..."
    sudo systemctl enable fail2ban
    sudo systemctl start fail2ban
fi

echo "🎉 Setup Completed!"
echo "-----------------------------------------"
echo "1. VS Code Server: http://<server-ip>:8080 (password in ~/.config/code-server/config.yaml)"
echo "2. Tailscale: Use 'tailscale up' to connect your laptop."
echo "3. Re-login or run 'newgrp docker' to use Docker without sudo."
echo "-----------------------------------------"

