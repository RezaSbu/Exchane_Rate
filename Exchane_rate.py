# # import requests
# # from bs4 import BeautifulSoup
# # import logging

# # logging.basicConfig(level=logging.INFO)

# # currencies = {
# #     "USD (US Dollar)": "price_dollar_rl",
# #     "AED (UAE Dirham)": "price_aed",
# #     "EUR (Euro)": "price_eur",
# #     "GBP (British Pound)": "price_gbp",
# #     "TRY (Turkish Lira)": "price_try",
# #     "CHF (Swiss Franc)": "price_chf",
# #     "CAD (Canadian Dollar)": "price_cad",
# #     "PKR (Pakistani Rupee)": "price_pkr",
# #     "SAR (Saudi Riyal)": "price_sar",
# #     "OMR (Omani Rial)": "price_omr",
# #     "KWD (Kuwaiti Dinar)": "price_kwd",
# #     "RUB (Russian Ruble)": "price_rub"
# # }

# # def get_live_price(currency_row):
# #     live_price = currency_row.find('td', {'class': 'nf'}).text.strip()
# #     return float(live_price.replace(',', '')) / 10

# # def fetch_currency_prices():
# #     url = "https://www.tgju.org/currency"
# #     headers = {
# #         'Cache-Control': 'no-cache',
# #         'Pragma': 'no-cache'
# #     }

# #     try:
# #         response = requests.get(url, headers=headers)
# #         response.raise_for_status()
# #     except requests.exceptions.RequestException as e:
# #         logging.error(f"Error fetching data: {e}")
# #         return {}

# #     soup = BeautifulSoup(response.text, 'html.parser')
# #     live_prices = {}

# #     for currency_name, market_row in currencies.items():
# #         currency_row = soup.find('tr', {'data-market-row': market_row})
# #         if currency_row:
# #             live_prices[currency_name] = get_live_price(currency_row)
# #         else:
# #             live_prices[currency_name] = None

# #     return live_prices

# # def calculate_aed_rates(prices):
# #     aed_price = prices.get("AED (UAE Dirham)")
# #     if aed_price is None:
# #         logging.error("AED price not found. Cannot calculate rates.")
# #         return {}

# #     aed_rates = {}
# #     for currency, price in prices.items():
# #         if price is not None and currency != "AED (UAE Dirham)":
# #             aed_rates[currency] = aed_price / price

# #     aed_rates["IRR (Iranian Rial)"] = aed_price
# #     return aed_rates

# # if __name__ == "__main__":
# #     prices = fetch_currency_prices()

# #     for currency, price in prices.items():
# #         logging.info(f"{currency}: {price:,} Toman")

# #     aed_rates = calculate_aed_rates(prices)

# #     for currency, rate in aed_rates.items():
# #         if currency == "IRR (Iranian Rial)":
# #             logging.info(f"AED/Toman: {rate:,}")
# #         else:
# #             logging.info(f"AED/{currency.split(' ')[0]}: {rate:.4f}")

# #     logging.info("-" * 30)




# import requests
# from bs4 import BeautifulSoup
# import logging

# logging.basicConfig(level=logging.INFO)

# currencies = {
#     "USD (US Dollar)": "price_dollar_rl",
#     "AED (UAE Dirham)": "price_aed",
#     "EUR (Euro)": "price_eur",
#     "GBP (British Pound)": "price_gbp",
#     "TRY (Turkish Lira)": "price_try",
#     "CHF (Swiss Franc)": "price_chf",
#     "CAD (Canadian Dollar)": "price_cad",
#     "PKR (Pakistani Rupee)": "price_pkr",
#     "SAR (Saudi Riyal)": "price_sar",
#     "OMR (Omani Rial)": "price_omr",
#     "KWD (Kuwaiti Dinar)": "price_kwd",
#     "RUB (Russian Ruble)": "price_rub"
# }

# def get_live_price(currency_row):
#     live_price = currency_row.find('td', {'class': 'nf'}).text.strip()
#     return float(live_price.replace(',', '')) / 10

# def fetch_currency_prices():
#     url = "https://www.tgju.org/currency"
#     headers = {
#         'Cache-Control': 'no-cache',
#         'Pragma': 'no-cache'
#     }

#     try:
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()
#     except requests.exceptions.RequestException as e:
#         logging.error(f"Error fetching data: {e}")
#         return {}

#     soup = BeautifulSoup(response.text, 'html.parser')
#     live_prices = {}

#     for currency_name, market_row in currencies.items():
#         currency_row = soup.find('tr', {'data-market-row': market_row})
#         if currency_row:
#             live_prices[currency_name] = get_live_price(currency_row)
#         else:
#             live_prices[currency_name] = None

#     return live_prices

# def calculate_aed_rates(prices):
#     aed_price = prices.get("AED (UAE Dirham)")
#     if aed_price is None:
#         logging.error("AED price not found. Cannot calculate rates.")
#         return {}

#     aed_rates = {}
#     for currency, price in prices.items():
#         if price is not None and currency != "AED (UAE Dirham)":
#             aed_rates[currency] = aed_price / price

#     aed_rates["IRR (Iranian Rial)"] = aed_price
#     return aed_rates

# def display_currency_options():
#     print("Select the target currency:")
#     for i, currency in enumerate(currencies.keys(), start=1):
#         print(f"{i}. {currency}")
#     print(f"{len(currencies) + 1}. Iran (Toman)")

# def get_user_input():
#     try:
#         amount = float(input("Enter the amount in AED: "))
#         if amount <= 0:
#             raise ValueError("Amount must be greater than 0.")
#         return amount
#     except ValueError as e:
#         print(f"Invalid input: {e}")
#         return None

# def convert_currency(amount, target_currency, aed_rates):
#     if target_currency == "AED (UAE Dirham)":
#         return amount
#     elif target_currency == "Iran (Toman)":
#         return amount * aed_rates["IRR (Iranian Rial)"]
#     else:
#         return amount * aed_rates.get(target_currency, 0)

# if __name__ == "__main__":
#     prices = fetch_currency_prices()

#     for currency, price in prices.items():
#         logging.info(f"{currency}: {price:,} Toman")

#     aed_rates = calculate_aed_rates(prices)

#     for currency, rate in aed_rates.items():
#         if currency == "IRR (Iranian Rial)":
#             logging.info(f"AED/Toman: {rate:,}")
#         else:
#             logging.info(f"AED/{currency.split(' ')[0]}: {rate:.4f}")

#     logging.info("-" * 30)

#     amount = get_user_input()
#     if amount is not None:
#         display_currency_options()
#         try:
#             choice = int(input("Enter the number of the target currency: "))
#             if 1 <= choice <= len(currencies) + 1:
#                 if choice == len(currencies) + 1:
#                     target_currency = "Iran (Toman)"
#                 else:
#                     target_currency = list(currencies.keys())[choice - 1]

#                 result = convert_currency(amount, target_currency, aed_rates)
#                 print(f"{amount} AED is equal to {result:.2f} {target_currency}")
#             else:
#                 print("Invalid choice. Please select a valid number.")
#         except ValueError:
#             print("Invalid input. Please enter a number.")



import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

currencies = {
    "USD (US Dollar)": "price_dollar_rl",
    "AED (UAE Dirham)": "price_aed",
    "EUR (Euro)": "price_eur",
    "GBP (British Pound)": "price_gbp",
    "TRY (Turkish Lira)": "price_try",
    "CHF (Swiss Franc)": "price_chf",
    "CAD (Canadian Dollar)": "price_cad",
    "PKR (Pakistani Rupee)": "price_pkr",
    "SAR (Saudi Riyal)": "price_sar",
    "OMR (Omani Rial)": "price_omr",
    "KWD (Kuwaiti Dinar)": "price_kwd",
    "RUB (Russian Ruble)": "price_rub"
}

def get_live_price(currency_row):
    live_price = currency_row.find('td', {'class': 'nf'}).text.strip()
    return float(live_price.replace(',', '')) / 10

def fetch_currency_prices():
    url = "https://www.tgju.org/currency"
    headers = {
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data: {e}")
        return {}

    soup = BeautifulSoup(response.text, 'html.parser')
    live_prices = {}

    for currency_name, market_row in currencies.items():
        currency_row = soup.find('tr', {'data-market-row': market_row})
        if currency_row:
            live_prices[currency_name] = get_live_price(currency_row)
        else:
            live_prices[currency_name] = None

    return live_prices

def calculate_aed_rates(prices):
    aed_price = prices.get("AED (UAE Dirham)")
    if aed_price is None:
        logging.error("AED price not found. Cannot calculate rates.")
        return {}

    aed_rates = {}
    for currency, price in prices.items():
        if price is not None and currency != "AED (UAE Dirham)":
            aed_rates[currency] = aed_price / price

    aed_rates["IRR (Iranian Rial)"] = aed_price
    return aed_rates

def display_currency_options():
    print("Select the target currency:")
    for i, currency in enumerate(currencies.keys(), start=1):
        print(f"{i}. {currency}")
    print(f"{len(currencies) + 1}. Iran (Toman)")

def get_user_input():
    try:
        amount = float(input("Enter the amount in AED: "))
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        return amount
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None

def convert_currency(amount, target_currency, aed_rates):
    if target_currency == "AED (UAE Dirham)":
        return amount
    elif target_currency == "Iran (Toman)":
        return amount * aed_rates["IRR (Iranian Rial)"]
    else:
        return amount * aed_rates.get(target_currency, 0)

if __name__ == "__main__":
    prices = fetch_currency_prices()

    for currency, price in prices.items():
        logging.info(f"{currency}: {price:,.2f} Toman")

    aed_rates = calculate_aed_rates(prices)

    for currency, rate in aed_rates.items():
        if currency == "IRR (Iranian Rial)":
            logging.info(f"AED/Toman: {rate:,.2f}")
        else:
            logging.info(f"AED/{currency.split(' ')[0]}: {rate:.4f}")

    logging.info("-" * 30)

    amount = get_user_input()
    if amount is not None:
        display_currency_options()
        try:
            choice = int(input("Enter the number of the target currency: "))
            if 1 <= choice <= len(currencies) + 1:
                if choice == len(currencies) + 1:
                    target_currency = "Iran (Toman)"
                else:
                    target_currency = list(currencies.keys())[choice - 1]

                result = convert_currency(amount, target_currency, aed_rates)
                print(f"{amount:,.2f} AED is equal to {result:,.2f} {target_currency}")
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")