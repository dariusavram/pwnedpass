import requests
import hashlib

def check_pwned_api(password):
    # Hash the password using SHA-1 algorithm
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    # Send GET request to the Have I Been Pwned API
    response = requests.get(url)

    # Check if the status code is successful
    if response.status_code == 200:
        hashes = (line.split(':') for line in response.text.splitlines() if line)
        # Iterate through the response to find matching hash suffix
        for h, count in hashes:
            if h == suffix:
                return int(count)
        return 0
    else:
        # If request failed, print error message
        print(f"Error: {response.status_code}")
        return None

def main():
    file_path = 'pass.txt'
    with open(file_path, 'r') as file:
        passwords = file.readlines()

    for password in passwords:
        password = password.strip()  # Remove leading/trailing whitespaces
        pwned_count = check_pwned_api(password)
        if pwned_count is not None:
            if pwned_count > 0:
                print(f"The password '{password}' has been pwned {pwned_count} times!")
            else:
                print(f"The password '{password}' has not been pwned.")

if __name__ == "__main__":
    main()
