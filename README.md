# InSyst

Display system information in a user-friendly interface.

## Overview

InSyst is a lightweight command-line tool designed for Linux systems. 
It provides detailed system information across various categories.
Users can navigate through the menu options by selecting the corresponding number.

![menu](https://github.com/user-attachments/assets/64bfaf33-a7c8-4ddf-8f85-1d165ee926e7)

![hw](https://github.com/user-attachments/assets/32fcd5e8-4e03-4320-a164-670af877099a)

## Features

- Displays system overview and detailed information.

- Retrieves hardware specifications.

- Provides network configuration details.

- Monitors system performance metrics.

- Lists installed applications.

- Shows system error logs.

- Simple menu-based navigation.

- Option to save output to a text file.


## Installation

### Prerequisites
Ensure you have the following installed on your Linux system:

- Python (version 3.6 or later)

- Required dependencies

### Installation Steps

1. Install required system dependencies:
```bash
sudo apt update && sudo apt install -y inxi
```
2. Install InSyst from the git repository:
```bash
git clone https://github.com/alxpxx/insyst
```
3. Navigate to the directory:
```bash
cd insyst
```
3. Build the package:
```bash
pip install .
```
3. Run InSyst:	
```bash
insyst
```

## Usage

Upon execution, a menu is displayed. Press the respective number to view system details.

### Menu Options

1. Overview - Displays a summary of system details and basic specs.

2. Detailed - Provides an indepth look at system configuration.

3. Hardware - Shows CPU, memory, disk and other hardware specifications.

4. Network - Displays active network interfaces, IP addresses and connectivity.

5. Performance - Monitors CPU usage and memory consumption.

6. Lists installed applications with version numbers (must be run as root).

7. Errors - Fetches and displays system logs and error messages.


### License

This project is licensed under GNU General Public License.

### Support

For issues and suggestions, please open an issue in Github.

### Author

Alxpx
