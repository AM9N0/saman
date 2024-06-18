import requests
import time
import random
import os
from colorama import init, Fore

init(autoreset=True)

# Corrected logos list
logos = [
    '''
    ##     ##   ##    ##     ##  ##
   ####    ### ###   ####    ### ##
  ##  ##   #######  ##  ##   ######
  ######   ## # ##  ######   ######
  ##  ##   ##   ##  ##  ##   ## ###
  ##  ##   ##   ##  ##  ##   ##  ##
  ##  ##   ##   ##  ##  ##   ##  ##
                                    
  $$$$$$\                  $$$$$$$$\ $$\
 $$  __$$\                 $$  _____|\__|
 $$ /  $$ |$$$$$$$\        $$ |      $$\  $$$$$$\   $$$$$$\
 $$ |  $$ |$$  __$$\       $$$$$\    $$ |$$  __$$\ $$  __$$\
 $$ |  $$ |$$ |  $$ |      $$  __|   $$ |$$ |  \__|$$$$$$$$ |
 $$ |  $$ |$$ |  $$ |      $$ |      $$ |$$ |      $$   ____|
  $$$$$$  |$$ |  $$ |      $$ |      $$ |$$ |      \$$$$$$$\ 
  \______/ \__|  \__|      \__|      \__|\__|       \_______|
    '''
]

def approval():
    os.system('git pull')
    time.sleep(1)
    uuid = str(os.geteuid()) + 'DS' + str(os.geteuid())
    id = 'AMAN-' + ''.join(uuid)
    os.system('clear')
    print(random.choice(logos))  # Print a random logo from logos list
    print('\x1b[1;37m [\x1b[36m•\x1b[1;37m] You Need Approval To Use This Tool')
    print('\x1b[1;37m [\x1b[36m•\x1b[1;37m] Your Key :\x1b[36m ' + id)
    time.sleep(0.1)
    print('\x1b[1;37m----------------------------------------------')

    try:
        httpCaht = requests.get('https://raw.githubusercontent.com/AM9N0/approvalmulti/main/multitoken1.py').text
        if id in httpCaht:
            print('\x1b[1;97m >> Your Key Has Been Approved !!!')
            msg = str(os.geteuid())
            time.sleep(1)
        else:
            print('\x1b[1;97m >> Sorry Your Key Has Not Been Approved ')
            time.sleep(0.1)
            input('IF U WANT TO BUY THEN PRESS ENTER ')
            tks = 'Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20' + id
            os.system('am start https://wa.me/+918700850020?text=' + tks)
            approval()  # Removed unnecessary parentheses here
            time.sleep(1)
            exit()
    except Exception as e:
        print(e)
        print(' >> Unable To Fetch Data From Server ')
        time.sleep(2)
        exit()

def send_messages(tokens_file, target_id, messages_file, haters_name, speed):
    with open(messages_file, "r") as file:
        messages = file.readlines()
    with open(tokens_file, "r") as file:
        tokens = file.readlines()

    headers = {
        "User-Agent": ("Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36"),
        "Referer": "https://www.google.com",
    }

    while True:
        for message_index, message in enumerate(messages):
            token_index = message_index % len(tokens)
            access_token = tokens[token_index].strip()
            full_message = f"{haters_name} {message.strip()}"

            url = f"https://graph.facebook.com/v17.0/{target_id}/feed"
            parameters = {"access_token": access_token, "message": full_message}
            try:
                response = requests.post(url, data=parameters, headers=headers)
                response.raise_for_status()
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                current_logo = random.choice(logos)
                print(Fore.GREEN + current_logo)
                print(Fore.YELLOW + f"[+] Message {message_index + 1} sent to {target_id} with token {token_index + 1}: {full_message} at {current_time}")
            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"[x] Failed to send message {message_index + 1} to {target_id} with token {token_index + 1}: {full_message} - Error: {e}")

            time.sleep(speed)
        print(Fore.CYAN + "\n[+] All messages sent. Restarting the process...\n")

def main():
    approval()

    print(Fore.MAGENTA + " XM9RTY AYUSH K1NG TOOL ")
    print(Fore.CYAN + "------------------------------------")
    # Get file paths and other inputs from the user
    tokens_file = input(Fore.YELLOW + "Enter the path to the tokens file: ").strip()
    target_id = input(Fore.YELLOW + "Enter the target_id: ").strip()
    messages_file = input(Fore.YELLOW + "Enter the path to the messages file: ").strip()
    haters_name = input(Fore.YELLOW + "Enter the hater's name: ").strip()
    speed = float(input(Fore.YELLOW + "Enter the speed (in seconds) between messages: ").strip())

    # Start sending messages
    send_messages(tokens_file, target_id, messages_file, haters_name, speed)

if __name__ == "__main__":
    main()
