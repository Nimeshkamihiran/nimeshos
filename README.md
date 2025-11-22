# 🔥 NimeshOS - Advanced Termux Custom Environment

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Termux-green?style=for-the-badge&logo=android"/>
  <img src="https://img.shields.io/badge/Version-2.0-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/License-MIT-red?style=for-the-badge"/>
</p>

<p align="center">
  <img src="banner.png" alt="NimeshOS Banner" width="600"/>
</p>

---

## ⚡ Features

| Feature | Description |
|---------|-------------|
| 🎨 **Custom Theme** | Kali Linux-like hacker theme with green text on black |
| 📦 **50+ Tools** | Pre-configured security & development tools |
| 🖥️ **Custom Banner** | Beautiful ASCII art banner on startup |
| ⚙️ **Auto Installer** | One-command installation for all tools |
| 🔄 **Auto Updates** | Update all tools with single command |
| 🐙 **GitHub Cloner** | Clone popular hacking repos automatically |
| 💻 **Custom Shell** | Built-in NimeshOS terminal |
| ☠️ **Hacking Menu** | Quick access to security tools |

---

## 📥 Installation

### One-Line Install (Recommended)
```bash
pkg update && pkg install -y curl && curl -sL https://raw.githubusercontent.com/Nimeshkamihiran/nimeshos/main/install.sh | bash
```

### Manual Installation
```bash
# Update packages
pkg update && pkg upgrade -y

# Install dependencies
pkg install -y python git curl wget

# Clone repository
git clone https://github.com/Nimeshkamihiran/nimeshos.git

# Run installer
cd nimeshos && bash install.sh
```

---

## 🚀 Usage

### Launch NimeshOS
```bash
nimeshos
```

### Available Commands
| Command | Description |
|---------|-------------|
| `nimeshos` | Launch main menu |
| `tools` | List installed tools |
| `sysinfo` | Show system info |
| `update` | Update system |
| `cls` | Clear screen |

---

## 📁 Main Menu Options

```
╔════════════════════════════════════════════════════════╗
║                    MAIN MENU                           ║
╠════════════════════════════════════════════════════════╣
║  [1] 📦 Install Tools          [6] 🖥️  Terminal Shell  ║
║  [2] 📋 List Tools             [7] ☠️  Hacking Menu   ║
║  [3] 🚀 Run Tool               [8] ⌨️  Custom Commands ║
║  [4] 🔄 Update System          [9] ℹ️  About          ║
║  [5] 🎨 Customize Termux       [0] 🚪 Exit            ║
║  [S] 📊 System Info                                    ║
╚════════════════════════════════════════════════════════╝
```

---

## 🛠️ Included Tool Categories

### 🔍 Information Gathering
- Nmap, Whois, DNSUtils, Traceroute, Netcat

### 🌐 Web Tools
- Curl, Wget, HTTPie, SQLMap

### 🔐 Password Tools
- Hydra, John the Ripper, Hashcat, Crunch

### 📡 Wireless
- Aircrack-ng, Macchanger

### 💻 Development
- Python, Ruby, Go, Node.js, PHP, Rust, Clang

### 🔧 Utilities
- Git, Vim, Nano, Tmux, Htop, Neofetch

---

## 🐙 GitHub Tools (Auto-Clone)

| Tool | Description |
|------|-------------|
| SQLMap | SQL Injection tool |
| Sherlock | Username OSINT |
| theHarvester | Email/Domain harvester |
| PhoneInfoga | Phone number OSINT |
| Seeker | Location tracker |
| Maigret | Social media finder |
| CamPhish | Camera phishing |

---

## 📸 Screenshots

<details>
<summary>Click to view screenshots</summary>

### Main Menu
![Main Menu](screenshots/main-menu.png)

### Tool Installer
![Installer](screenshots/installer.png)

### Hacker Theme
![Theme](screenshots/theme.png)

</details>

---

## ⚙️ Configuration

### Change Theme
```bash
nimeshos
# Select option [5] Customize Termux
# Select option [5] Apply Hacker Theme
```

### Add Custom Banner
```bash
nimeshos
# Select option [5] Customize Termux
# Select option [3] Set Custom Banner
```

---

## 🔄 Update NimeshOS

```bash
cd ~/nimeshos && git pull
# OR
nimeshos
# Select option [4] Update System
```

---

## ❓ FAQ

**Q: Does this work on Android?**
> Yes! This is specifically designed for Termux on Android.

**Q: Is root required?**
> No, all features work without root access.

**Q: How to uninstall?**
```bash
rm -rf ~/nimeshos ~/tools ~/.termux-banner.sh
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Nimesh Kamihiran**

- GitHub: [@Nimeshkamihiran](https://github.com/Nimeshkamihiran)

---

## ⭐ Star History

If you like this project, please give it a ⭐!

---

<p align="center">
  <b>Made with ❤️ in Sri Lanka 🇱🇰</b>
</p>
