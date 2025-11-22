#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════╗
║                     NIMESH OS v2.0                               ║
║              Advanced Termux Custom Environment                  ║
║                   Created by Nimesh Kamihiran                    ║
╚══════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import subprocess
import json
import random
from datetime import datetime

# Colors
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_BLUE = '\033[44m'

c = Colors()

def clear():
    os.system('clear')

def slow_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner():
    clear()
    banner_art = f"""
{c.CYAN}{c.BOLD}
    ███╗   ██╗██╗███╗   ███╗███████╗███████╗██╗  ██╗     ██████╗ ███████╗
    ████╗  ██║██║████╗ ████║██╔════╝██╔════╝██║  ██║    ██╔═══██╗██╔════╝
    ██╔██╗ ██║██║██╔████╔██║█████╗  ███████╗███████║    ██║   ██║███████╗
    ██║╚██╗██║██║██║╚██╔╝██║██╔══╝  ╚════██║██╔══██║    ██║   ██║╚════██║
    ██║ ╚████║██║██║ ╚═╝ ██║███████╗███████║██║  ██║    ╚██████╔╝███████║
    ╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝
{c.RESET}
{c.RED}╔════════════════════════════════════════════════════════════════════════╗
{c.YELLOW}║  {c.GREEN}🔥 ADVANCED TERMUX CUSTOM ENVIRONMENT 🔥{c.YELLOW}                            ║
{c.YELLOW}║  {c.CYAN}👤 Author: Nimesh Kamihiran{c.YELLOW}                                          ║
{c.YELLOW}║  {c.MAGENTA}🌐 GitHub: github.com/Nimeshkamihiran{c.YELLOW}                               ║
{c.YELLOW}║  {c.WHITE}📅 Version: 2.0 | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{c.YELLOW}                          ║
{c.RED}╚════════════════════════════════════════════════════════════════════════╝{c.RESET}
"""
    print(banner_art)

def loading_animation(text="Loading", duration=2):
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f'\r{c.CYAN}{chars[i % len(chars)]} {text}...{c.RESET}')
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    print(f'\r{c.GREEN}✓ {text} Complete!{c.RESET}     ')

def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except:
        return False, "", "Error"

def system_info():
    clear()
    print(f"\n{c.CYAN}{'═'*60}{c.RESET}")
    print(f"{c.YELLOW}{c.BOLD}         📊 SYSTEM INFORMATION 📊{c.RESET}")
    print(f"{c.CYAN}{'═'*60}{c.RESET}\n")
    
    cmds = [
        ("🖥️  Device", "getprop ro.product.model"),
        ("📱 Android", "getprop ro.build.version.release"),
        ("🏗️  Architecture", "uname -m"),
        ("💾 Kernel", "uname -r"),
        ("👤 User", "whoami"),
        ("📂 Home", "echo $HOME"),
        ("🐍 Python", "python --version"),
    ]
    
    for name, cmd in cmds:
        success, out, _ = run_cmd(cmd)
        val = out.strip() if success else "N/A"
        print(f"  {c.GREEN}{name}:{c.RESET} {c.WHITE}{val}{c.RESET}")
    
    # Storage info
    success, out, _ = run_cmd("df -h $HOME | tail -1")
    if success:
        parts = out.split()
        if len(parts) >= 4:
            print(f"  {c.GREEN}💿 Storage:{c.RESET} {c.WHITE}{parts[2]}/{parts[1]} used ({parts[4]}){c.RESET}")
    
    print(f"\n{c.CYAN}{'═'*60}{c.RESET}")
    input(f"\n{c.YELLOW}Press Enter to continue...{c.RESET}")

# Tool Database
TOOLS_DB = {
    "information-gathering": {
        "nmap": {"pkg": "nmap", "desc": "Network scanner"},
        "whois": {"pkg": "whois", "desc": "Domain lookup"},
        "dnsutils": {"pkg": "dnsutils", "desc": "DNS utilities"},
        "traceroute": {"pkg": "traceroute", "desc": "Trace packet route"},
        "netcat": {"pkg": "netcat-openbsd", "desc": "Network utility"},
    },
    "web-tools": {
        "curl": {"pkg": "curl", "desc": "Data transfer tool"},
        "wget": {"pkg": "wget", "desc": "File downloader"},
        "httpie": {"pkg": "httpie", "desc": "HTTP client"},
        "sqlmap": {"pkg": "python", "git": "https://github.com/sqlmapproject/sqlmap", "desc": "SQL injection"},
    },
    "password-tools": {
        "hydra": {"pkg": "hydra", "desc": "Password cracker"},
        "john": {"pkg": "john", "desc": "John the Ripper"},
        "hashcat": {"pkg": "hashcat", "desc": "Hash cracker"},
        "crunch": {"pkg": "crunch", "desc": "Wordlist generator"},
    },
    "wireless": {
        "aircrack-ng": {"pkg": "aircrack-ng", "desc": "WiFi security"},
        "macchanger": {"pkg": "macchanger", "desc": "MAC changer"},
    },
    "exploitation": {
        "metasploit": {"pkg": "unstable-repo", "special": "metasploit", "desc": "Exploitation framework"},
    },
    "utilities": {
        "git": {"pkg": "git", "desc": "Version control"},
        "python": {"pkg": "python", "desc": "Python language"},
        "ruby": {"pkg": "ruby", "desc": "Ruby language"},
        "golang": {"pkg": "golang", "desc": "Go language"},
        "nodejs": {"pkg": "nodejs", "desc": "Node.js"},
        "vim": {"pkg": "vim", "desc": "Text editor"},
        "nano": {"pkg": "nano", "desc": "Easy editor"},
        "tmux": {"pkg": "tmux", "desc": "Terminal multiplexer"},
        "htop": {"pkg": "htop", "desc": "Process viewer"},
        "neofetch": {"pkg": "neofetch", "desc": "System info"},
        "figlet": {"pkg": "figlet", "desc": "ASCII art text"},
        "toilet": {"pkg": "toilet", "desc": "Colored ASCII"},
        "cmatrix": {"pkg": "cmatrix", "desc": "Matrix effect"},
        "sl": {"pkg": "sl", "desc": "Steam locomotive"},
        "cowsay": {"pkg": "cowsay", "desc": "Talking cow"},
    },
    "development": {
        "clang": {"pkg": "clang", "desc": "C/C++ compiler"},
        "rust": {"pkg": "rust", "desc": "Rust language"},
        "php": {"pkg": "php", "desc": "PHP language"},
        "perl": {"pkg": "perl", "desc": "Perl language"},
        "lua": {"pkg": "lua54", "desc": "Lua language"},
    }
}

# GitHub repos to clone
GITHUB_REPOS = {
    "termux-tool": "https://github.com/Nimeshkamihiran/termux-tool",
    "sqlmap": "https://github.com/sqlmapproject/sqlmap",
    "theHarvester": "https://github.com/laramies/theHarvester",
    "sherlock": "https://github.com/sherlock-project/sherlock",
    "phoneinfoga": "https://github.com/sundowndev/phoneinfoga",
    "social-analyzer": "https://github.com/qeeqbox/social-analyzer",
    "holehe": "https://github.com/megadose/holehe",
    "maigret": "https://github.com/soxoj/maigret",
    "h8mail": "https://github.com/khast3x/h8mail",
    "seeker": "https://github.com/thewhiteh4t/seeker",
    "saycheese": "https://github.com/hangetzzu/saycheese",
    "camphish": "https://github.com/techchipnet/CamPhish",
}

def install_tool(pkg_name, pkg_info):
    print(f"\n{c.YELLOW}📦 Installing {pkg_name}...{c.RESET}")
    
    if "git" in pkg_info:
        # Clone from git
        repo_url = pkg_info["git"]
        target_dir = f"$HOME/tools/{pkg_name}"
        run_cmd(f"mkdir -p $HOME/tools")
        success, _, err = run_cmd(f"git clone {repo_url} {target_dir}")
        if success:
            print(f"{c.GREEN}✓ {pkg_name} cloned successfully!{c.RESET}")
            # Install requirements if exists
            run_cmd(f"cd {target_dir} && pip install -r requirements.txt 2>/dev/null")
        else:
            print(f"{c.RED}✗ Failed to clone {pkg_name}{c.RESET}")
    else:
        # Install via pkg
        pkg = pkg_info.get("pkg", pkg_name)
        success, _, _ = run_cmd(f"pkg install -y {pkg}")
        if success:
            print(f"{c.GREEN}✓ {pkg_name} installed!{c.RESET}")
        else:
            print(f"{c.RED}✗ Failed to install {pkg_name}{c.RESET}")

def install_menu():
    while True:
        clear()
        print(f"\n{c.CYAN}{'═'*60}{c.RESET}")
        print(f"{c.YELLOW}{c.BOLD}         📦 TOOL INSTALLATION CENTER 📦{c.RESET}")
        print(f"{c.CYAN}{'═'*60}{c.RESET}\n")
        
        categories = list(TOOLS_DB.keys())
        for i, cat in enumerate(categories, 1):
            print(f"  {c.GREEN}[{i}]{c.RESET} {c.WHITE}{cat.upper()}{c.RESET}")
        
        print(f"\n  {c.GREEN}[A]{c.RESET} {c.YELLOW}Install ALL Tools{c.RESET}")
        print(f"  {c.GREEN}[U]{c.RESET} {c.CYAN}Update All Packages{c.RESET}")
        print(f"  {c.GREEN}[G]{c.RESET} {c.MAGENTA}Clone GitHub Tools{c.RESET}")
        print(f"  {c.GREEN}[0]{c.RESET} {c.RED}Back to Main Menu{c.RESET}")
        
        choice = input(f"\n{c.CYAN}NimeshOS>{c.RESET} ").strip().lower()
        
        if choice == '0':
            break
        elif choice == 'a':
            print(f"\n{c.YELLOW}🚀 Installing ALL tools...{c.RESET}\n")
            run_cmd("pkg update -y && pkg upgrade -y")
            for cat, tools in TOOLS_DB.items():
                print(f"\n{c.MAGENTA}▶ {cat.upper()}{c.RESET}")
                for name, info in tools.items():
                    install_tool(name, info)
            input(f"\n{c.GREEN}All installations complete! Press Enter...{c.RESET}")
        elif choice == 'u':
            print(f"\n{c.YELLOW}🔄 Updating system...{c.RESET}\n")
            run_cmd("pkg update -y && pkg upgrade -y")
            input(f"\n{c.GREEN}Update complete! Press Enter...{c.RESET}")
        elif choice == 'g':
            clone_github_tools()
        elif choice.isdigit() and 1 <= int(choice) <= len(categories):
            cat = categories[int(choice)-1]
            show_category_tools(cat)

def show_category_tools(category):
    while True:
        clear()
        print(f"\n{c.CYAN}{'═'*60}{c.RESET}")
        print(f"{c.YELLOW}{c.BOLD}    📁 {category.upper()} TOOLS{c.RESET}")
        print(f"{c.CYAN}{'═'*60}{c.RESET}\n")
        
        tools = list(TOOLS_DB[category].items())
        for i, (name, info) in enumerate(tools, 1):
            desc = info.get("desc", "No description")
            print(f"  {c.GREEN}[{i}]{c.RESET} {c.WHITE}{name}{c.RESET} - {c.CYAN}{desc}{c.RESET}")
        
        print(f"\n  {c.GREEN}[A]{c.RESET} {c.YELLOW}Install All in Category{c.RESET}")
        print(f"  {c.GREEN}[0]{c.RESET} {c.RED}Back{c.RESET}")
        
        choice = input(f"\n{c.CYAN}NimeshOS/{category}>{c.RESET} ").strip().lower()
        
        if choice == '0':
            break
        elif choice == 'a':
            for name, info in tools:
                install_tool(name, info)
            input(f"\n{c.GREEN}Press Enter to continue...{c.RESET}")
        elif choice.isdigit() and 1 <= int(choice) <= len(tools):
            name, info = tools[int(choice)-1]
            install_tool(name, info)
            input(f"\n{c.GREEN}Press Enter to continue...{c.RESET}")

def clone_github_tools():
    clear()
    print(f"\n{c.CYAN}{'═'*60}{c.RESET}")
    print(f"{c.YELLOW}{c.BOLD}         🐙 GITHUB TOOLS CLONER 🐙{c.RESET}")
    print(f"{c.CYAN}{'═'*60}{c.RESET}\n")
    
    repos = list(GITHUB_REPOS.items())
    for i, (name, url) in enumerate(repos, 1):
        print(f"  {c.GREEN}[{i}]{c.RESET} {c.WHITE}{name}{c.RESET}")
        print(f"      {c.CYAN}{url}{c.RESET}\n")
    
    print(f"  {c.GREEN}[A]{c.RESET} {c.YELLOW}Clone ALL Repos{c.RESET}")
    print(f"  {c.GREEN}[0]{c.RESET} {c.RED}Back{c.RESET}")
    
    choice = input(f"\n{c.CYAN}NimeshOS/github>{c.RESET} ").strip().lower()
    
    if choice == 'a':
        run_cmd("mkdir -p $HOME/tools")
        for name, url in repos:
            print(f"\n{c.YELLOW}📥 Cloning {name}...{c.RESET}")
            success, _, _ = run_cmd(f"git clone {url} $HOME/tools/{name}")
            if success:
                print(f"{c.GREEN}✓ {name} cloned!{c.RESET}")
                run_cmd(f"cd $HOME/tools/{name} && pip install -r requirements.txt 2>/dev/null")
        input(f"\n{c.GREEN}All repos cloned! Press Enter...{c.RESET}")
    elif choice.isdigit() and 1 <= int(choice) <= len(repos):
        name, url = repos[int(choice)-1]
        run_cmd("mkdir -p $HOME/tools")
        print(f"\n{c.YELLOW}📥 Cloning {name}...{c.RESET}")
        run_cmd(f"git clone {url} $HOME/tools/{name}")
        run_cmd(f"cd $HOME/tools/{name} && pip install -r requirements.txt 2>/dev/null")
        input(f"\n{c.GREEN}Press Enter to continue...{c.RESET}")

def list_tools():
    clear()
    print(f"\n{c.CYAN}{'═'*60}{c.RESET}")
    print(f"{c.YELLOW}{c.BOLD}         📋 INSTALLED TOOLS LIST 📋{c.RESET}")
    print(f"{c.CYAN}{'═'*60}{c.RESET}\n")
    
    # Check cloned tools
    print(f"{c.MAGENTA}▶ CLONED TOOLS ($HOME/tools):{c.RESET}\n")
    success, out, _ = run_cmd("ls $HOME/tools 2>/dev/null")
    if success and out.strip():
        for tool in out.strip().split('\n'):
            print(f"  {c.GREEN}✓{c.RESET} {c.WHITE}{tool}{c.RESET}")
    else:
        print(f"  {c.YELLOW}No tools cloned yet{c.RESET}")
    
    # Check installed packages
    print(f"\n{c.MAGENTA}▶ INSTALLED PACKAGES:{c.RESET}\n")
    success, out, _ = run_cmd("pkg list-installed 2>/dev/null | head -20")
    if success:
        for line in out.strip().split('\n')[:15]:
            print(f"  {c.CYAN}•{c.RESET} {line}")
        print(f"\n  {c.YELLOW}(Showing first 15 packages){c.RESET}")
    
    input(f"\n{c.YELLOW}Press Enter to continue...{c.RESET}")

def run_tool():
    clear()
    print(f"\n{c.CYAN}{'═'*60}{c.RESET}")
    print(f"{c.YELLOW}{c.BOLD}         🚀 RUN TOOLS 🚀{c.RESET}")
    print(f"{c.CYAN}{'═'*60}{c.RESET}\n")
    
    success, out, _ = run_cmd("ls $HOME/tools 2>/dev/null")
    if success and out.strip():
        tools = out.strip().split('\n')
        for i, tool in enumerate(tools, 1):
            print(f"  {c.GREEN}[{i}]{c.RESET} {c.WHITE}{tool}{c.RESET}")
        
        print(f"\n  {c.GREEN}[0]{c.RESET} {c.RED}Back{c.RESET}")
        
        choice = input(f"\n{c.CYAN}Select tool to run>{c.RESET} ").strip()
        
        if choice.isdigit() and 1 <= int(choice) <= len(tools):
            tool = tools[int(choice)-1]
            tool_path = f"$HOME/tools/{tool}"
            
            # Try to find main file
            for main in ["main.py", f"{tool}.py", "app.py", "run.py"]:
                success, _, _ = run_cmd(f"test -f {tool_path}/{main}")
                if success:
                    print(f"\n{c.GREEN}Running {tool}...{c.RESET}\n")
                    os.system(f"cd {tool_path} && python {main}")
                    break
            else:
                print(f"\n{c.YELLOW}Tool directory: {tool_path}{c.RESET}")
                print(f"{c.CYAN}Enter command to run or 'exit' to go back{c.RESET}")
                while True:
                    cmd = input(f"{c.MAGENTA}{tool}>{c.RESET} ")
                    if cmd.lower() == 'exit':
                        break
                    os.system(f"cd {tool_path} && {cmd}")
    else:
        print(f"{c.YELLOW}No tools installed. Use 'Install Tools' first.{c.RESET}")
        input(f"\n{c.YELLOW}Press Enter to continue...{c.RESET}")

def customize_termux():
    clear()
    print(f"\n{c.CYAN}{'═'*60}{c.RESET}")
    print(f"{c.YELLOW}{c.BOLD}         🎨 CUSTOMIZE TERMUX 🎨{c.RESET}")
    print(f"{c.CYAN}{'═'*60}{c.RESET}\n")
    
    print(f"  {c.GREEN}[1]{c.RESET} Install Oh My ZSH")
    print(f"  {c.GREEN}[2]{c.RESET} Install Termux Styling")
    print(f"  {c.GREEN}[3]{c.RESET} Set Custom Banner")
    print(f"  {c.GREEN}[4]{c.RESET} Install Powerline Fonts")
    print(f"  {c.GREEN}[5]{c.RESET} Apply Hacker Theme")
    print(f"  {c.GREEN}[0]{c.RESET} {c.RED}Back{c.RESET}")
    
    choice = input(f"\n{c.CYAN}NimeshOS/customize>{c.RESET} ").strip()
    
    if choice == '1':
        print(f"\n{c.YELLOW}Installing ZSH & Oh My ZSH...{c.RESET}")
        run_cmd("pkg install -y zsh curl git")
        run_cmd('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended')
        run_cmd("chsh -s zsh")
        print(f"{c.GREEN}✓ Oh My ZSH installed! Restart Termux.{c.RESET}")
    elif choice == '2':
        print(f"\n{c.YELLOW}Installing Termux Styling...{c.RESET}")
        run_cmd("pkg install -y termux-styling")
        print(f"{c.GREEN}✓ Run 'termux-style' to change colors/fonts{c.RESET}")
    elif choice == '3':
        set_custom_banner()
    elif choice == '4':
        print(f"\n{c.YELLOW}Installing fonts...{c.RESET}")
        run_cmd("pkg install -y figlet toilet")
        print(f"{c.GREEN}✓ Fonts installed!{c.RESET}")
    elif choice == '5':
        apply_hacker_theme()
    
    if choice != '0':
        input(f"\n{c.GREEN}Press Enter to continue...{c.RESET}")

def set_custom_banner():
    banner_script = '''
#!/data/data/com.termux/files/usr/bin/bash
clear
echo ""
echo -e "\\033[96m"
figlet -f slant "NimeshOS" 2>/dev/null || echo "NIMESH OS"
echo -e "\\033[93m"
echo "═══════════════════════════════════════════════════"
echo -e "\\033[92m  Welcome to NimeshOS Custom Environment"
echo -e "\\033[95m  Author: Nimesh Kamihiran"
echo -e "\\033[96m  Type 'nimeshos' to start the tool"
echo -e "\\033[93m═══════════════════════════════════════════════════"
echo -e "\\033[0m"
'''
    with open(os.path.expanduser("~/.termux-banner.sh"), "w") as f:
        f.write(banner_script)
    run_cmd("chmod +x ~/.termux-banner.sh")
    
    # Add to bashrc
    bashrc_entry = '\n# NimeshOS Banner\nif [ -f ~/.termux-banner.sh ]; then\n    source ~/.termux-banner.sh\nfi\n'
    bashrc_path = os.path.expanduser("~/.bashrc")
    
    # Check if already added
    if os.path.exists(bashrc_path):
        with open(bashrc_path, "r") as f:
            if "NimeshOS Banner" not in f.read():
                with open(bashrc_path, "a") as f:
                    f.write(bashrc_entry)
    else:
        with open(bashrc_path, "w") as f:
            f.write(bashrc_entry)
    
    print(f"{c.GREEN}✓ Custom banner set! Restart Termux to see it.{c.RESET}")

def apply_hacker_theme():
    print(f"\n{c.YELLOW}Applying hacker theme...{c.RESET}")
    
    # Create termux properties
    props = """
extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]
bell-character = ignore
use-black-ui = true
"""
    run_cmd("mkdir -p ~/.termux")
    with open(os.path.expanduser("~/.termux/termux.properties"), "w") as f:
        f.write(props)
    
    # Create colors
    colors = """
foreground=#00FF00
background=#000000
cursor=#00FF00
color0=#000000
color1=#FF0000
color2=#00FF00
color3=#FFFF00
color4=#0000FF
color5=#FF00FF
color6=#00FFFF
color7=#FFFFFF
"""
    with open(os.path.expanduser("~/.termux/colors.properties"), "w") as f:
        f.write(colors)
    
    run_cmd("termux-reload-settings")
    print(f"{c.GREEN}✓ Hacker theme applied! Restart Termux.{c.RESET}")

def update_system():
    clear()
    print(f"\n{c.CYAN}{'═'*60}{c.RESET}")
    print(f"{c.YELLOW}{c.BOLD}         🔄 SYSTEM UPDATE 🔄{c.RESET}")
    print(f"{c.CYAN}{'═'*60}{c.RESET}\n")
    
    print(f"{c.CYAN}Updating package lists...{c.RESET}")
    run_cmd("pkg update -y")
    
    print(f"\n{c.CYAN}Upgrading packages...{c.RESET}")
    run_cmd("pkg upgrade -y")
    
    print(f"\n{c.CYAN}Updating cloned tools...{c.RESET}")
    success, out, _ = run_cmd("ls $HOME/tools 2>/dev/null")
    if success and out.strip():
        for tool in out.strip().split('\n'):
            print(f"  {c.YELLOW}Updating {tool}...{c.RESET}")
            run_cmd(f"cd $HOME/tools/{tool} && git pull 2>/dev/null")
    
    print(f"\n{c.GREEN}✓ System update complete!{c.RESET}")
    input(f"\n{c.YELLOW}Press Enter to continue...{c.RESET}")

def custom_commands():
    clear()
    print(f"\n{c.CYAN}{'═'*60}{c.RESET}")
    print(f"{c.YELLOW}{c.BOLD}         ⌨️  CUSTOM COMMANDS ⌨️{c.RESET}")
    print(f"{c.CYAN}{'═'*60}{c.RESET}\n")
    
    commands = {
        "nimeshos": "Launch NimeshOS",
        "sysinfo": "Show system information",
        "tools": "List installed tools",
        "update": "Update system and tools",
        "hack-theme": "Apply hacker theme",
        "matrix": "Matrix rain effect",
        "train": "Steam locomotive",
    }
    
    for cmd, desc in commands.items():
        print(f"  {c.GREEN}{cmd}{c.RESET} - {c.CYAN}{desc}{c.RESET}")
    
    print(f"\n{c.YELLOW}Installing custom commands...{c.RESET}")
    
    # Create bin directory
    run_cmd("mkdir -p $PREFIX/bin")
    
    # Get current script path
    script_path = os.path.abspath(__file__)
    
    # Create nimeshos command
    nimeshos_cmd = f'''#!/data/data/com.termux/files/usr/bin/bash
python {script_path}
'''
    cmd_path = os.path.expanduser("$PREFIX/bin/nimeshos")
    try:
        with open(os.path.expandvars("$PREFIX/bin/nimeshos"), "w") as f:
            f.write(nimeshos_cmd)
        run_cmd("chmod +x $PREFIX/bin/nimeshos")
        print(f"{c.GREEN}✓ 'nimeshos' command installed!{c.RESET}")
    except:
        print(f"{c.YELLOW}Run: alias nimeshos='python {script_path}'{c.RESET}")
    
    # Create other commands
    other_cmds = {
        "sysinfo": "neofetch || echo 'Install neofetch first'",
        "matrix": "cmatrix || echo 'Install: pkg install cmatrix'",
        "train": "sl || echo 'Install: pkg install sl'",
        "hack-theme": f"python {script_path} --theme",
    }
    
    for cmd, action in other_cmds.items():
        try:
            with open(os.path.expandvars(f"$PREFIX/bin/{cmd}"), "w") as f:
                f.write(f"#!/data/data/com.termux/files/usr/bin/bash\n{action}\n")
            run_cmd(f"chmod +x $PREFIX/bin/{cmd}")
        except:
            pass
    
    print(f"{c.GREEN}✓ Custom commands installed!{c.RESET}")
    input(f"\n{c.YELLOW}Press Enter to continue...{c.RESET}")