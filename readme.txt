A Python tool to sanitize Cisco 'show tech' outputs by extracting the 'show run' section and masking
 sensitive information.

This script processes a 'show tech' file from a Cisco switch, extracts the 'show running-config' section,
 and comments out any lines containing 'aaa' settings or keys with the string <removed>. It's designed to help
 network engineers share configuration data without exposing sensitive details.

📋 Features
Extracts 'show run' section from a full 'show tech' output.

Comments out lines containing:

aaa configurations.

Any key with the string <removed>.

Outputs a sanitized version of the configuration for safe sharing or documentation.

🚀 Getting Started
Prerequisites
Python 3.x installed on your system.

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/campagnollo/showTechStripper.git
cd showTechStripper
(Optional) Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

There are no external dependencies required for this script.

🖥️ Usage
Prepare your 'show tech' file:

Ensure you have a text file containing the output of the show tech command from a Cisco switch.

Run the script:

bash
Copy
Edit
python desec_config.py path/to/show_tech_output.txt
Replace path/to/show_tech_output.txt with the actual path to your 'show tech' file.

Output:

The script will generate a new file named sanitized_config.txt in the same directory, containing the sanitized
 configuration.

📄 Example
Given a 'show tech' file with the following lines:

nginx
Copy
Edit
aaa new-model
username admin secret 5 <removed>
interface GigabitEthernet0/1
 ip address 192.168.1.1 255.255.255.0
The sanitized_config.txt output will be:

nginx
Copy
Edit
# aaa new-model
# username admin secret 5 <removed>
interface GigabitEthernet0/1
 ip address 192.168.1.1 255.255.255.0
🧑‍💻 Author
Eric L. Moore
DevOps & Cloud Infrastructure Engineer
GitHub Profile

📜 License
This project is licensed under the MIT License.