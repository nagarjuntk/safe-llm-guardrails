from datetime import datetime

def log_request(user_input, status):
    with open("logs.txt", "a") as f:
        f.write(f"{datetime.now()} | {status} | {user_input}\n")