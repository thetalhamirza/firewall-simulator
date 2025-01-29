# Firewall Simulator

This is a simple Python-based firewall simulator that randomly generates IP addresses within the `192.168.1.0/24` range and checks whether they are allowed or blocked based on predefined firewall rules.

## Features

- Generates random IP addresses dynamically.
    
- Uses predefined firewall rules to allow or block specific IPs.
    
- Displays the result with color-coded output (`red` for blocked, `green` for allowed).
    
- Assigns a random process ID for each IP request.
    

## Requirements

Ensure you have Python installed along with the required dependencies:

```
pip install colorama termcolor
```

## Usage

Run the script using:

```
python firewall_simulator.py
```

## How It Works

1. The script generates 20 random IP addresses in the `192.168.1.0/24` subnet.
    
2. It checks each IP against the predefined firewall rules.
    
3. If the IP is in the blocklist, it prints the result in **red**.
    
4. If the IP is not in the blocklist, it prints the result in **green**.
    
5. A random process ID is assigned for each request.
    

## Firewall Rules

The firewall currently blocks the following IPs:

```
192.168.1.3
192.168.1.5
192.168.1.9
192.168.1.12
192.168.1.14
192.168.1.18
192.168.1.23
192.168.1.35
```

Any other IPs are allowed by default.

## Example Output

```
IP: 192.168.1.7, Action: Allow, ProcessID: 3452  (Green)
IP: 192.168.1.5, Action: Block, ProcessID: 8723  (Red)
...
```

## License

This project is for educational purposes and is released under the MIT License.