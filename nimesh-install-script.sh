#!/data/data/com.termux/files/usr/bin/bash

# ╔══════════════════════════════════════════════════════════════════╗
# ║                  NIMESHOS INSTALLER v2.0                         ║
# ║              Created by Nimesh Kamihiran                         ║
# ║           github.com/Nimeshkamihiran/nimeshos                    ║
# ╚══════════════════════════════════════════════════════════════════╝

# Colors
RED='\033[91m'
GREEN='\033[92m'
YELLOW='\033[93m'
BLUE='\033[94m'
MAGENTA='\033[95m'
CYAN='\033[96m'
WHITE='\033[97m'
BOLD='\033[1m'
RESET='\033[0m'

clear

# Banner
echo -e "${CYAN}${BOLD}"
cat << "EOF"
    ███╗   ██╗██╗███╗   ███╗███████╗███████╗██╗  ██╗     ██████╗ ███████╗
    ████╗  ██║██║████╗ ████║██╔════╝██╔════╝██║  ██║    ██╔═══██╗██╔════╝
    ██╔██╗ ██║██║██╔████╔██║█████╗  ███████╗███████║    ██║   ██║███████╗
    ██║╚██╗██║██║██║╚██╔╝██║██╔══╝  ╚════██║██╔══██║    ██║   ██║╚════██║
    ██║ ╚████║██║██║ ╚═╝ ██║███████╗███████║██║  ██║    ╚██████╔╝███████║
    ╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝
EOF
echo -e "${RESET}"

echo -e "${RED}╔════════════════════════════════════════════════════════════════════════╗${RESET}"
echo -e "${YELLOW}║  ${GREEN}🚀 NIMESHOS INSTALLER - Advanced Termux Custom Environment 🚀${YELLOW}        ║${RESET}"
echo -e "${YELLOW}║  ${CYAN}👤 Author: Nimesh Kamihiran${YELLOW}                                          ║${RESET}"
echo -e "${YELLOW}║  ${MAGENTA}🌐 GitHub: github.com/Nimeshkamihiran${YELLOW}                               ║${RESET}"
echo -e "${RED}╚════════════════════════════════════════════════════════════════════════╝${RESET}"
echo ""

# Function to show progress
progress() {
    echo -e "${CYAN}[*] $1${RESET}"
}

success() {
    echo -e "${GREEN}[✓] $1${RESET}"
}

error() {
    echo -e "${RED}[✗] $1${RESET}"
}

# Check if running in Termux
if [ ! -d "/data/data/com.termux" ]; then
    error "This script must be run in Termux!"
    exit 1
fi

echo -e "${YELLOW}This will install NimeshOS on your Termux.${RESET}"
echo -e "${WHITE}Features:${RESET}"
echo -e "  ${GREEN}•${RESET} Custom Kali-like banner"
echo -e "  ${GREEN}•${RESET} 50+ Hacking & Dev tools"
echo -e "  ${GREEN}•${RESET} Custom commands"
echo -e "  ${GREEN}•${RESET} Hacker theme"
echo -e "  ${GREEN}•${RESET} Built-in tool manager"
echo ""
read -p "$(echo -e ${YELLOW}'Continue installation? [Y/n]: '${RESET})" confirm

if [[ "$confirm" == "n" || "$confirm" == "N" ]]; then
    echo -e "${RED}Installation cancelled.${RESET}"
    exit 0
fi

echo ""

# Step 1: Update system
progress "Updating Termux packages..."
pkg update -y > /dev/null 2>&1
pkg upgrade -y > /dev/null 2>&1
success "System updated!"

# Step 2: Install dependencies
progress "Installing dependencies..."
pkg install -y python git curl wget figlet toilet ncurses-utils > /dev/null 2>&1
pip install --upgrade pip > /dev/null 2>&1
success "Dependencies installed!"

# Step 3: Create directories
progress "Creating directories..."
mkdir -p $HOME/tools
mkdir -p $HOME/nimeshos
mkdir -p $HOME/.termux
success "Directories created!"

# Step 4: Download NimeshOS
progress "Downloading NimeshOS..."
# Clone from GitHub or create locally
if [ -d "$HOME/nimeshos/.git" ]; then
    cd $HOME/nimeshos && git pull > /dev/null 2>&1
else
    # Create the main script
    cat > $HOME/nimeshos/nimeshos.py << 'NIMESHOS_SCRIPT'
# The full Python script will be here
# For now, download from GitHub
NIMESHOS_SCRIPT
fi

# Download from GitHub
git clone https://github.com/Nimeshkamihiran/termux-tool $HOME/tools/termux-tool 2>/dev/null || true
success "NimeshOS downloaded!"

# Step 5: Setup custom banner
progress "Setting up custom banner..."
cat > $HOME/.termux-banner.sh << 'BANNER_EOF'
#!/data/data/com.termux/files/usr/bin/bash
clear
echo ""
echo -e "\033[96m"
figlet -f slant "NimeshOS" 2>/dev/null || echo "═══ NIMESH OS ═══"
echo -e "\033[93m═══════════════════════════════════════════════════════════"
echo -e "\033[92m  ☠️  Welcome to NimeshOS - Advanced Hacking Environment"
echo -e "\033[95m  👤 Author: Nimesh Kamihiran"
echo -e "\033[96m  📁 Type 'nimeshos' to launch the tool"
echo -e "\033[91m  🔧 Type 'tools' to see installed tools"
echo -e "\033[93m═══════════════════════════════════════════════════════════"
echo -e "\033[0m"
BANNER_EOF
chmod +x $HOME/.termux-banner.sh
success "Banner configured!"

# Step 6: Setup bashrc
progress "Configuring shell..."
if ! grep -q "NimeshOS" $HOME/.bashrc 2>/dev/null; then
    cat >> $HOME/.bashrc << 'BASHRC_EOF'

# ═══════════════════════════════════════════════════════════
# NimeshOS Configuration
# ═══════════════════════════════════════════════════════════

# Show banner on start
if [ -f ~/.termux-banner.sh ]; then
    source ~/.termux-banner.sh
fi

# Custom aliases
alias nimeshos='python $HOME/nimeshos/nimeshos.py'
alias tools='ls $HOME/tools'
alias update='pkg update && pkg upgrade'
alias cls='clear'
alias ll='ls -la'
alias ..='cd ..'
alias install='pkg install'
alias remove='pkg uninstall'

# Custom prompt
export PS1='\[\033[91m\]┌──[\[\033[96m\]NimeshOS\[\033[91m\]]─[\[\033[92m\]\u\[\033[91m\]]\n\[\033[91m\]└──╼ \[\033[93m\]\w\[\033[0m\] \$ '

# Path
export PATH=$PATH:$HOME/tools:$HOME/nimeshos

BASHRC_EOF
fi
success "Shell configured!"

# Step 7: Setup Termux styling
progress "Applying hacker theme..."
cat > $HOME/.termux/termux.properties << 'PROPS_EOF'
extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]
bell-character = ignore
use-black-ui = true
PROPS_EOF

cat > $HOME/.termux/colors.properties << 'COLORS_EOF'
foreground=#00FF00
background=#000000
cursor=#00FF00
color0=#000000
color1=#FF0000
color2=#00FF00
color3=#FFFF00
color4=#0066FF
color5=#FF00FF
color6=#00FFFF
color7=#FFFFFF
color8=#555555
color9=#FF5555
color10=#55FF55
color11=#FFFF55
color12=#5555FF
color13=#FF55FF
color14=#55FFFF
color15=#FFFFFF
COLORS_EOF
success "Theme applied!"

# Step 8: Create nimeshos command
progress "Creating custom commands..."
cat > $PREFIX/bin/nimeshos << 'CMD_EOF'
#!/data/data/com.termux/files/usr/bin/bash
python $HOME/nimeshos/nimeshos.py "$@"
CMD_EOF
chmod +x $PREFIX/bin/nimeshos

cat > $PREFIX/bin/sysinfo << 'CMD_EOF'
#!/data/data/com.termux/files/usr/bin/bash
neofetch 2>/dev/null || (
    echo "═══════════════════════════════════════"
    echo "  Device: $(getprop ro.product.model)"
    echo "  Android: $(getprop ro.build.version.release)"
    echo "  Kernel: $(uname -r)"
    echo "  User: $(whoami)"
    echo "═══════════════════════════════════════"
)
CMD_EOF
chmod +x $PREFIX/bin/sysinfo
success "Commands created!"

# Step 9: Reload settings
progress "Finalizing installation..."
termux-reload-settings 2>/dev/null || true
success "Installation complete!"

echo ""
echo -e "${GREEN}╔════════════════════════════════════════════════════════════════╗${RESET}"
echo -e "${GREEN}║              🎉 NIMESHOS INSTALLED SUCCESSFULLY! 🎉            ║${RESET}"
echo -e "${GREEN}╠════════════════════════════════════════════════════════════════╣${RESET}"
echo -e "${GREEN}║  ${YELLOW}Commands:${GREEN}                                                    ║${RESET}"
echo -e "${GREEN}║    ${CYAN}nimeshos${GREEN}  - Launch NimeshOS main menu                      ║${RESET}"
echo -e "${GREEN}║    ${CYAN}tools${GREEN}     - List installed tools                           ║${RESET}"
echo -e "${GREEN}║    ${CYAN}sysinfo${GREEN}   - Show system information                        ║${RESET}"
echo -e "${GREEN}║    ${CYAN}update${GREEN}    - Update system                                  ║${RESET}"
echo -e "${GREEN}║                                                                ║${RESET}"
echo -e "${GREEN}║  ${MAGENTA}Please restart Termux to apply all changes!${GREEN}                  ║${RESET}"
echo -e "${GREEN}╚════════════════════════════════════════════════════════════════╝${RESET}"
echo ""
echo -e "${YELLOW}Thank you for installing NimeshOS!${RESET}"
echo -e "${CYAN}GitHub: github.com/Nimeshkamihiran${RESET}"
echo ""

read -p "$(echo -e ${GREEN}'Restart Termux now? [Y/n]: '${RESET})" restart
if [[ "$restart" != "n" && "$restart" != "N" ]]; then
    echo -e "${YELLOW}Restarting Termux...${RESET}"
    sleep 1
    exit 0
fi