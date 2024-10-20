import requests
import json
import time

class FaucetBot:
    def __init__(self, faucet_url, accounts):
        self.faucet_url = faucet_url
        self.accounts = accounts

    def request_faucet(self, account):
        # Data untuk request faucet, menggunakan private key akun
        payload = {
            'private_key': account['private_key'],
            'address': account['address']
        }

        try:
            response = requests.post(self.faucet_url, json=payload)
            if response.status_code == 200:
                print(f"Faucet berhasil untuk akun: {account['address']}")
            else:
                print(f"Error: {response.status_code}, {response.text}")
        except Exception as e:
            print(f"Terjadi kesalahan: {str(e)}")

    def run(self):
        while True:
            for account in self.accounts:
                self.request_faucet(account)
                time.sleep(60)  # Jeda 1 menit untuk mencegah batasan rate
