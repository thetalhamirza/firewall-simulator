import random
from colorama import init
from termcolor import colored

init()

def generate_random_ip():
    return f"192.168.1.{random.randint(0,50)}"

def check_firewall_rules(ip, rules):
    for ruleIP, action in rules.items():
        if ruleIP == ip:
            return action
    return "Allow"


def main():
    firewall_rules = {
        "192.168.1.3": "Block",
        "192.168.1.5": "Block",
        "192.168.1.9": "Block",
        "192.168.1.12": "Block",
        "192.168.1.14": "Block",
        "192.168.1.18": "Block",
        "192.168.1.23": "Block",
        "192.168.1.35": "Block"
    }

    for _ in range(20):
        ip_address = generate_random_ip()
        action = check_firewall_rules(ip_address, firewall_rules)
        random_integer = random.randint(0,9999)
        if action == "Block":
            print(colored(f"IP: {ip_address}, Action: {action}, ProcessID: {random_integer}", 'red'))
        else:
            print(colored(f"IP: {ip_address}, Action: {action}, ProcessID: {random_integer}", 'green'))
            


if __name__ == "__main__":
    main()