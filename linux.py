import os
import time
import subprocess
from colorama import Fore, Style, init

# Initialize colorama
init()

# ASCII art for OS selection
linux_ascii = """

*****************************************************                                                                                                                                                                                                                                                                                                                                                                                       
* Author: Winston Ighodaro                          *                                                                                                                                                                                                                                                                                                                                                                                       
* Website: https://cybergeneration.tech             *                                                                                                                                                                                                                                                                                                                                                                                       
* X : https://x.com/officialwhyte22                 *                                                                                                                                                                                                                                                                                                                                                                                       
* Language : Python                                 *                                                                                                                                                                                                                                                                                                                                                                                       
*****************************************************

"""

windows_ascii = """

*****************************************************                                                                                                                                                                                                                                                                                                                                                                                       
* Author: Winston Ighodaro                          *                                                                                                                                                                                                                                                                                                                                                                                       
* Website: https://cybergeneration.tech             *                                                                                                                                                                                                                                                                                                                                                                                       
* X : https://x.com/officialwhyte22                 *                                                                                                                                                                                                                                                                                                                                                                                       
* Language : Python                                 *                                                                                                                                                                                                                                                                                                                                                                                       
*****************************************************


"""

# Function to print text with a typing effect in green color
def delay_print(text, color=Fore.GREEN, delay=0.01):
    print(color, end='')
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)

# Function to search for a command in the specified file
def search_command(command, file_name):
    try:
        with open(file_name, 'r') as file:
            commands = [line.strip() for line in file]
            for line in commands:
                if command == line.split(':')[0].strip():  # Exact match with the command name
                    return line, None
            for line in commands:
                if command in line.split(':')[0].strip():  # Partial match for suggestion
                    return None, line.split(':')[0].strip()
        return "Command not found.", None
    except FileNotFoundError:
        return f"File '{file_name}' not found.", None

# Function to update text files from GitHub
def update_text_files(github_link):
    print(Fore.CYAN + "Checking for updates to text files..." + Style.RESET_ALL)
    try:
        subprocess.run(["git", "pull", github_link, "config.txt", "kernel.txt"], check=True)
        print(Fore.GREEN + "Text files updated successfully." + Style.RESET_ALL)
    except subprocess.CalledProcessError:
        print(Fore.RED + "Failed to update text files. Please make sure you have git installed and the script is part of a git repository." + Style.RESET_ALL)

# Main menu function
def main_menu():
    github_link = "https://github.com/yourusername/yourrepository.git"  # Replace with your GitHub repository link
    
    while True:
        print(Fore.CYAN + "\nSelect an Operating System:" + Style.RESET_ALL)
        print(Fore.GREEN + "1. Linux" + Style.RESET_ALL)
        print(Fore.GREEN + "2. Windows" + Style.RESET_ALL)
        print(Fore.YELLOW + "3. Update text files from GitHub" + Style.RESET_ALL)
        choice = input("Enter your choice (1/2/3) or 'exit' to quit: ").strip().lower()

        if choice == '1':
            delay_print(linux_ascii, delay=0)
            os_type = "Linux"
            file_name = 'config.txt'
        elif choice == '2':
            delay_print(windows_ascii, delay=0)
            os_type = "Windows"
            file_name = 'kernel.txt'
        elif choice == '3':
            update_text_files(github_link)
            continue
        elif choice == 'exit':
            print(Fore.GREEN + "Exiting..." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)
            continue

        while True:
            command = input(Fore.GREEN + f"Enter a {os_type} command (or 'opt' to go back to OS selection): " + Style.RESET_ALL).strip().lower()
            if command == 'opt':
                break
            info, suggestion = search_command(command, file_name)
            if info:
                delay_print(info)
            elif suggestion:
                delay_print(f"Command not found. Did you mean '{suggestion}'?")
            else:
                delay_print("Command not found.")
            print()

if __name__ == "__main__":
    main_menu()