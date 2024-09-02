import time
import import json
import time
import os
from datetime import datetime
import socket

# Đổi màu cho các thông báo
RED = "\033[91m"
RESET = "\033[0m"

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_message(message, color=RESET):
    print(f"{color}{message}{RESET}")

def get_device_type():
    return "PC" if os.name == 'nt' else "MOBILE"

def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "Unavailable"
    finally:
        s.close()
    return ip

def get_local_time():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def save_config(link, seconds, version):
    config = {
        'link': link,
        'seconds': seconds,
        'version': version
    }
    with open('config.json', 'w') as f:
        json.dump(config, f)

def load_config():
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def create_cron(version):
    link = input("LINK CẦN CHẠY: ")
    seconds = int(input("SỐ GIÂY: "))
    save_config(link, seconds, version)
    print_message("Cron job created and saved in config.json")

    # Hỏi người dùng nếu muốn chạy cron job ngay
    run_now = input("Bạn muốn chạy ngay bây giờ không? (Nhấn Enter để chạy, hoặc nhập bất kỳ để thoát): ")
    if run_now == "":
        start_cron()

def start_cron():
    config = load_config()
    if not config:
        print_message("No cron job configuration found.")
        return
    
    link = config['link']
    seconds = config['seconds']
    
    while True:
        clear_console()
        # Hiển thị thông tin thiết bị và thời gian
        print_message(f"IP: {get_ip_address()}", RED)
        print_message(f"Thời gian hiện tại: {get_local_time()}", RED)
        print_message(f"Thiết bị: {get_device_type()}", RED)

        # Đếm ngược thời gian
        for remaining in range(seconds, 0, -1):
            clear_console()
            print_message(f"[SUPHUMEO] TRẠNG THÁI", RED)
            print_message(f"Link: {link}", RED)
            print_message(f"Thời gian còn lại: {remaining} giây...", RED)
            time.sleep(1)
        
        # Thực thi liên kết
        print_message(f"[SUPHUMEO] Đang thực thi liên kết: {link}", RED)
        os.system(f"curl {link}")  # Hoặc sử dụng lệnh khác để mở liên kết

def main():
    while True:
        clear_console()
        print_message(f"2.8: Cron Job Siêu Vip V1", RED)
        print_message(f"2.9: Cron Job Siêu Vip V2", RED)
        
        choice = input("Nhập lựa chọn: ")
        
        if choice == '2.8':
            create_cron('V1')
        
        elif choice == '2.9':
            sub_choice = input("1. CREATE CRON\n2. START CRON\nChọn: ")
            if sub_choice == '1':
                create_cron('V2')
            elif sub_choice == '2':
                start_cron()

if __name__ == "__main__":
    main()
