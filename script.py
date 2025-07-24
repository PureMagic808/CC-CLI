import requests
import argparse

API_KEY = "YOUR_API_KEY"  # зарегистрируйтесь и получите API-ключ

def convert(amount, frm, to):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{frm}"
    resp = requests.get(url)
    data = resp.json()
    rate = data["conversion_rates"].get(to)
    if rate:
        print(f"{amount} {frm} = {round(amount * rate, 4)} {to}")
    else:
        print(f"❌ Валюта {to} не поддерживается.")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--amount", type=float, required=True)
    p.add_argument("--from", dest="frm", required=True)
    p.add_argument("--to", required=True)
    args = p.parse_args()
    convert(args.amount, args.frm.upper(), args.to.upper())
