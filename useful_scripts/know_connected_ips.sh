#!/bin/bash

# Function to check and install arp-scan
install_arp_scan() {
    echo "Checking for arp-scan..."
    if ! command -v arp-scan &>/dev/null; then
        echo "arp-scan not found. Installing..."
        if [[ "$OSTYPE" == "linux-gnu"* ]]; then
            if command -v apt &>/dev/null; then
                # Ubuntu/Debian
                sudo apt update && sudo apt install -y arp-scan
            elif command -v dnf &>/dev/null; then
                # Fedora
                sudo dnf install -y arp-scan
            elif command -v yum &>/dev/null; then
                # RHEL/CentOS
                sudo yum install -y arp-scan
            else
                echo "Unsupported Linux package manager. Install arp-scan manually."
                exit 1
            fi
        elif [[ "$OSTYPE" == "darwin"* ]]; then
            # macOS
            if ! command -v brew &>/dev/null; then
                echo "Homebrew not found. Installing Homebrew..."
                /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            fi
            brew install arp-scan
        else
            echo "Unsupported OS: $OSTYPE"
            exit 1
        fi
    else
        echo "arp-scan is already installed."
    fi
}

# Function to find the Wi-Fi interface
get_wifi_interface() {
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        networksetup -listallhardwareports | \
        awk '/Wi-Fi/{getline; print $2}'
    else
        # Linux
        nmcli device status | grep wifi | awk '{print $1}'
    fi
}

# Main
install_arp_scan

INTERFACE=$(get_wifi_interface)

if [ -z "$INTERFACE" ]; then
    echo "No Wi-Fi interface detected. Are you connected to Wi-Fi?"
    exit 1
fi

echo "Scanning devices connected to Wi-Fi on interface: $INTERFACE..."
sudo arp-scan --interface=$INTERFACE --localnet
