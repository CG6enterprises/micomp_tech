#!/usr/bin/env python
"""
Database Inspector - View what's stored in the database
"""

import sqlite3
import json
from colorama import Fore, Back, Style, init
from tabulate import tabulate

init(autoreset=True)

DATABASE_PATH = "micomp_tech.db"

def print_header(title):
    """Print formatted header"""
    print(f"\n{Fore.CYAN}{'='*70}")
    print(f"{Fore.CYAN}  {title}")
    print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")

def inspect_table(table_name):
    """Inspect a database table"""
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # Get column names
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [row[1] for row in cursor.fetchall()]
        
        # Get data
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        
        print_header(f"Table: {table_name}")
        print(f"Total Records: {Fore.YELLOW}{len(rows)}{Style.RESET_ALL}\n")
        
        if rows:
            data = []
            for row in rows:
                data.append([row[col] for col in columns])
            print(tabulate(data, headers=columns, tablefmt="grid"))
        else:
            print(f"{Fore.YELLOW}No records found{Style.RESET_ALL}")
        
        conn.close()
    except Exception as e:
        print(f"{Fore.RED}Error reading table {table_name}: {e}{Style.RESET_ALL}")

def inspect_database():
    """Inspect entire database"""
    print(f"{Fore.MAGENTA}")
    print("""
╔═════════════════════════════════════════════════════════════════════╗
║       MICOMP_TECH DATABASE INSPECTOR                                ║
║       View All Data Stored in Database                              ║
╚═════════════════════════════════════════════════════════════════════╝
    """)
    print(f"{Style.RESET_ALL}")
    
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        # Get all table names
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        conn.close()
        
        if not tables:
            print(f"{Fore.YELLOW}No tables found in database. Run Flask first to create tables.{Style.RESET_ALL}")
            return
        
        print(f"Database: {Fore.YELLOW}{DATABASE_PATH}{Style.RESET_ALL}")
        print(f"Tables Found: {Fore.YELLOW}{len(tables)}{Style.RESET_ALL}\n")
        
        for table in sorted(tables):
            inspect_table(table)
    
    except FileNotFoundError:
        print(f"{Fore.RED}Database not found: {DATABASE_PATH}")
        print(f"Run Flask server first: {Fore.GREEN}python backend/app.py{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    # Check if tabulate is installed
    try:
        import tabulate
    except ImportError:
        print(f"{Fore.YELLOW}Installing required package: tabulate{Style.RESET_ALL}")
        import subprocess
        subprocess.check_call(["pip", "install", "tabulate"])
    
    inspect_database()
