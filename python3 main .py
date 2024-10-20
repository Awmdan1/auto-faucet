if __name__ == "__main__":
    faucet_url = "URL_FAUCET"
    
    # Membaca akun dari file JSON
    with open("accounts.json", "r") as f:
        accounts = json.load(f)

    bot = FaucetBot(faucet_url, accounts)
    bot.run()
