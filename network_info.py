#!/usr/bin/env python
"""
Network Test Helper - Find local IP address for testing on other devices
"""

import socket
import platform
import subprocess
from colorama import Fore, Back, Style, init

init(autoreset=True)

def get_local_ip():
    """Get local IP address"""
    try:
        # Connect to a public DNS to find local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def get_local_hostname():
    """Get local hostname"""
    try:
        return socket.gethostname()
    except Exception:
        return "localhost"

def print_network_info():
    """Print network information for accessing on other devices"""
    print(f"{Fore.CYAN}")
    print("""
╔═════════════════════════════════════════════════════════════════════╗
║       MICOMP_TECH - ACCESS ON OTHER DEVICES                         ║
║       Network Configuration Guide                                   ║
╚═════════════════════════════════════════════════════════════════════╝
    """)
    print(f"{Style.RESET_ALL}")
    
    local_ip = get_local_ip()
    hostname = get_local_hostname()
    port = 5000
    
    print(f"{Fore.YELLOW}Your Device Information:{Style.RESET_ALL}")
    print(f"  Local IP Address: {Fore.GREEN}{local_ip}{Style.RESET_ALL}")
    print(f"  Hostname: {Fore.GREEN}{hostname}{Style.RESET_ALL}")
    print(f"  Port: {Fore.GREEN}{port}{Style.RESET_ALL}")
    print(f"  OS: {Fore.GREEN}{platform.system()}{Style.RESET_ALL}\n")
    
    print(f"{Fore.YELLOW}Access URLs:{Style.RESET_ALL}")
    print(f"  ✓ From this device:")
    print(f"    {Fore.BLUE}http://localhost:5000{Style.RESET_ALL}")
    print(f"    {Fore.BLUE}http://127.0.0.1:5000{Style.RESET_ALL}\n")
    
    print(f"  ✓ From other devices on same network:")
    print(f"    {Fore.BLUE}http://{local_ip}:5000{Style.RESET_ALL}")
    print(f"    {Fore.BLUE}http://{hostname}:5000{Style.RESET_ALL}\n")
    
    print(f"{Fore.YELLOW}On Other Device (Phone, Tablet, Computer):{Style.RESET_ALL}")
    print(f"  1. Make sure other device is on {Fore.GREEN}same WiFi network{Style.RESET_ALL}")
    print(f"  2. Open browser and go to: {Fore.BLUE}http://{local_ip}:5000{Style.RESET_ALL}")
    print(f"  3. You should see the Micomp_Tech landing page\n")
    
    print(f"{Fore.YELLOW}Testing Instructions:{Style.RESET_ALL}")
    print(f"  • Test from phone/tablet using above URL")
    print(f"  • Check responsive design works")
    print(f"  • Test all buttons and forms")
    print(f"  • Verify API endpoints work from other device\n")
    
    print(f"{Fore.YELLOW}API Access from Other Device:{Style.RESET_ALL}")
    print(f"  Base URL: {Fore.BLUE}http://{local_ip}:5000/api{Style.RESET_ALL}")
    print(f"  Example: {Fore.BLUE}http://{local_ip}:5000/api/courses{Style.RESET_ALL}\n")
    
    print(f"{Fore.YELLOW}Troubleshooting:{Style.RESET_ALL}")
    print(f"  ✗ Can't connect? Check:")
    print(f"    1. Flask server is running on your device")
    print(f"    2. Both devices are on same WiFi network")
    print(f"    3. Firewall isn't blocking port 5000")
    print(f"    4. Use IP address, not hostname (if hostname doesn't work)\n")
    
    print(f"{Fore.YELLOW}To run Flask on all interfaces:{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}python backend/app.py{Style.RESET_ALL}")
    print(f"  (Default: already runs on all interfaces at 0.0.0.0:5000)\n")
    
    print(f"{Fore.CYAN}{'='*71}{Style.RESET_ALL}")

if __name__ == "__main__":
    print_network_info()
