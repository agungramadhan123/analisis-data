import requests

def get_ip_info(ip_address):
    # Ganti 'YOUR_ACCESS_TOKEN' dengan token akses API Anda dari ipinfo.io
    access_token = '192.168.18.107'
    url = f'https://ipinfo.io/{ip_address}/json?token={access_token}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    ip = input("Masukkan IP address: ")
    info = get_ip_info(ip)
    if info:
        print(f"Informasi IP: {info}")