import json
import requests
import time
import os
from datetime import datetime
import socket
from time import strftime

def generate_key():
    """Generate a key based on the current day."""
    ngay = int(strftime('%d'))
    key = str(ngay * 25937 + 469173)
    return key

def fetch_key_from_api(api_url, api_key, url):
    """Fetch shortened URL from the API."""
    full_url = f"{api_url}?api={api_key}&url={url}"
    response = requests.get(full_url)
    
    try:
        post_url = response.json()
    except json.JSONDecodeError:
        print("Phản hồi không phải là JSON hợp lệ")
        return None
    
    return post_url

def run_python_code_from_url(script_url):
    """Download and execute Python script from a URL."""
    try:
        response = requests.get(script_url)
        response.raise_for_status()  # Raise an error for bad responses
        
        script_code = response.text
        print("Nội dung mã nguồn:\n", script_code)  # In ra nội dung để kiểm tra
        
        # Execute the script code
        exec(script_code, globals())
        
    except requests.RequestException as e:
        print(f"Không thể tải script từ URL: {e}")
    except SyntaxError as e:
        print(f"Lỗi cú pháp khi thực thi script: {e}")
    except Exception as e:
        print(f"Lỗi khi thực thi script: {e}")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def fast_print(message):
    """Print message quickly to the console."""
    print(message)

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
    fast_print("Cron job created and saved in config.json")

    run_now = input("Bạn muốn chạy ngay bây giờ không? (Nhấn Enter để chạy, hoặc nhập bất kỳ để thoát): ")
    if run_now == "":
        start_cron()

def start_cron():
    config = load_config()
    if not config:
        fast_print("No cron job configuration found.")
        return
    
    link = config['link']
    seconds = config['seconds']
    
    while True:
        clear_console()
        current_time = get_local_time()
        ip_address = get_ip_address()
        device_type = get_device_type()

        fast_print(f"IP: {ip_address}")
        fast_print(f"Thời gian hiện tại: {current_time}")
        fast_print(f"Thiết bị: {device_type}")

        for remaining in range(seconds, 0, -1):
            clear_console()
            fast_print(f"[SUPHUMEO] TRẠNG THÁI")
            fast_print(f"Link: {link}")
            fast_print(f"Thời gian còn lại: {remaining} giây...")
            time.sleep(1)
        
        fast_print(f"[SUPHUMEO] Đang thực thi liên kết: {link}")
        os.system(f"curl {link}")

def main():
    key = generate_key()
    url = f'https://vanhauclond.site/keytool.php?key={key}'

    api_key_link4m = "66d010f75a7bc446a34b2716"
    link4m_api_url = 'https://link4m.co/api-shorten/v2'
    
    post_url = fetch_key_from_api(link4m_api_url, api_key_link4m, url)
    
    if post_url:
        if post_url.get('status') == "error":
            print(post_url.get('message', 'Lỗi không xác định'))
        else:
            link_key = post_url.get('shortenedUrl')
            nhap_key = input(f'''\033[1;32m Link lấy key: \033[1;33m{link_key}
                  \033[1;36m   /$$$$$$  /$$   /$$ /$$$$$$$  /$$   /$$ /$$   /$$ /$$      /$$ /$$$$$$$   /$$$$$$ 
 /$$__  $$| $$  | $$| $$__  $$| $$  | $$| $$  | $$| $$$    /$$$| $$__  $$ /$$__  $$
| $$  \__/| $$  | $$| $$  \ $$| $$  | $$| $$  | $$| $$$$  /$$$$| $$  \ $$| $$  \ $$
|  $$$$$$ | $$  | $$| $$$$$$$/| $$$$$$$$| $$  | $$| $$ $$/$$ $$| $$$$$$$/| $$  | $$
 \____  $$| $$  | $$| $$____/ | $$__  $$| $$  | $$| $$  $$$| $$| $$__  $$| $$  | $$
 /$$  \ $$| $$  | $$| $$      | $$  | $$| $$  | $$| $$\  $ | $$| $$  \ $$| $$  | $$
|  $$$$$$/|  $$$$$$/| $$      | $$  | $$|  $$$$$$/| $$ \/  | $$| $$  | $$|  $$$$$$/
 \______/  \______/ |__/      |__/  |__/ \______/ |__/     |__/|__/  |__/ \______/ 
                                                                                   
                                                                                   
                                                                                     \033[1;97m  \033[1;90m\033[0;31m
    \033[1;35m        \033[1;97m \033[1;97m


              \033[1;34mQuả Tool Siêu Cấp Pro By: SUPHUMEO 
                  [-----------------------------]
                   \033[1;31m1.Support TooL:SUPHUMEO .
                   \033[1;33m2.YouTube:SUPHUMEO .
                   \033[1;36m3.Zalo:.
                   \033[1;36m4. Fb.com/suphumeo.dev.
                   \033[0;35m5. Website:suphumeo.com.
                  [-----------------------------]
                    \033[1;32m KeyTool Hôm Nay: \033[1;33m''')

            if nhap_key == key:
                print('\033[1;32m Key chính xác. Chúc bạn ngày tốt lành!')
                
                sub_choice = input("Chọn công cụ (2.9: Cron Job V1, 2.8: Cron Job V2): ")
                if sub_choice == '2.9':
                    create_cron('V1')
                elif sub_choice == '2.8':
                    sub_sub_choice = input("1. CREATE CRON\n2. START CRON\nChọn: ")
                    if sub_sub_choice == '1':
                        create_cron('V2')
                    elif sub_sub_choice == '2':
                        start_cron()
            else:
                print('\033[1;31m Key sai. Vui lòng vượt link để lấy.')
    else:
        print("Không thể lấy dữ liệu từ API.")

if __name__ == "__main__":
    main()
