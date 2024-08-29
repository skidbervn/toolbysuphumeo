import time
import requests
import threading
import os
import getpass

# Đường dẫn đến tệp chứa cron jobs
cron_file = 'cron.txt'

# Mật khẩu để truy cập các chức năng của công cụ
PASSWORD = 'keyvip'  # Bạn có thể thay đổi mật khẩu này theo yêu cầu

def check_password():
    """Kiểm tra mật khẩu người dùng nhập vào."""
    password = getpass.getpass(prompt='Nhập mật khẩu: ')
    return password == PASSWORD

def create_cron():
    if not check_password():
        print("Mật khẩu không chính xác.")
        return

    url = input("Nhập URL cần chạy: ")
    interval = int(input("Nhập số giây giữa các lần yêu cầu: "))
    
    with open(cron_file, 'a') as file:
        file.write(f"{url} {interval}\n")
    
    print(f"Đã thêm cron job: URL={url}, Interval={interval} giây")

def run_cron_job(url, interval):
    while True:
        try:
            response = requests.get(url)
            print(f"Status Code: {response.status_code} - {url}")
        except requests.RequestException as e:
            print(f"Đã xảy ra lỗi: {e}")
        time.sleep(interval)

def start_cron():
    if not check_password():
        print("Mật khẩu không chính xác.")
        return

    if not os.path.exists(cron_file):
        print("Tệp cron.txt không tồn tại. Hãy tạo một cron job trước.")
        return

    with open(cron_file, 'r') as file:
        cron_jobs = file.readlines()

    threads = []
    for job in cron_jobs:
        url, interval = job.strip().split()
        interval = int(interval)
        
        print(f"Bắt đầu cron job với URL={url} và Interval={interval} giây")
        
        # Tạo và khởi động một luồng cho từng cron job
        thread = threading.Thread(target=run_cron_job, args=(url, interval))
        thread.daemon = True
        thread.start()
        threads.append(thread)

    # Đợi cho tất cả các luồng hoàn thành (nếu cần thiết)
    for thread in threads:
        thread.join()

def main():
    while True:
        print("\nChọn một tùy chọn:")
        print("[1] Create Cron")
        print("[2] Start Cron")
        print("[3] Exit")
        print("[4] SỤC")
        
        choice = input("Nhập lựa chọn của bạn: ")
        
        if choice == '1':
            create_cron()
        elif choice == '2':
            start_cron()
        elif choice == '3':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == '__main__':
    main()
