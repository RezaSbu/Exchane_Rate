import math

# Constants
FIXED_AED_TO_USD = 3.6732 
FIXED_AED_TO_KWD = 0.082   
AED_TO_IRR_RANGE = (21751, 22339)  
AED_TO_RUB_RANGE = (18.5, 19.5)      

def my_proposed_formula(aed_amount, target_currency):
    if target_currency == "IRR":
        return (aed_amount * AED_TO_IRR_RANGE[0], aed_amount * AED_TO_IRR_RANGE[1])
    elif target_currency == "RUB":
        return (aed_amount * AED_TO_RUB_RANGE[0], aed_amount * AED_TO_RUB_RANGE[1])
    else:
        return None


def cirp_formula(aed_amount, target_currency):
    if target_currency == "IRR":
        forward_rate = 25142  
        return (aed_amount * 22000, aed_amount * forward_rate)
    elif target_currency == "RUB":
        forward_rate = 19.8  
        return (aed_amount * 18.5, aed_amount * forward_rate)
    else:
        return None

def ppp_formula(aed_amount, target_currency):
    if target_currency == "IRR":
        ppp_rate_low = 16029  
        ppp_rate_high = 27971  
        return (aed_amount * ppp_rate_low, aed_amount * ppp_rate_high)
    elif target_currency == "RUB":
        ppp_rate_low = 17.5 
        ppp_rate_high = 20.5
        return (aed_amount * ppp_rate_low, aed_amount * ppp_rate_high)
    else:
        return None

def mundell_fleming_formula(aed_amount, target_currency):
    if target_currency == "IRR":
        depreciation_rate = 0.90 
        return (aed_amount * 19800, aed_amount * 22000)
    elif target_currency == "RUB":
        depreciation_rate = 0.90  
        return (aed_amount * 17.0, aed_amount * 19.0)
    else:
        return None

def main():
    aed_amount = float(input("Enter the amount in AED: "))

    print("Select target currency:")
    print("1. USD (Dollar)")
    print("2. IRR (Toman)")
    print("3. RUB (Russian Ruble)")
    print("4. KWD (Kuwaiti Dinar)")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        target_currency = "USD"
        usd_amount = aed_amount / FIXED_AED_TO_USD
        print(f"\nConverted amount: {usd_amount:.2f} USD")
        return
    elif choice == "2":
        target_currency = "IRR"
    elif choice == "3":
        target_currency = "RUB"
    elif choice == "4":
        target_currency = "KWD"
        kwd_amount = aed_amount * FIXED_AED_TO_KWD
        print(f"\nConverted amount: {kwd_amount:.2f} KWD")
        return
    else:
        print("Invalid choice!")
        return

    result1 = my_proposed_formula(aed_amount, target_currency)
    result2 = cirp_formula(aed_amount, target_currency)
    result3 = ppp_formula(aed_amount, target_currency)
    result4 = mundell_fleming_formula(aed_amount, target_currency)

    print("\nResults:")
    print(f"My Proposed Formula: {result1[0]:,.2f} to {result1[1]:,.2f} {target_currency}")
    print(f"Covered Interest Rate Parity (CIRP): {result2[0]:,.2f} to {result2[1]:,.2f} {target_currency}")
    print(f"Purchasing Power Parity (PPP): {result3[0]:,.2f} to {result3[1]:,.2f} {target_currency}")
    print(f"Mundell-Fleming Model: {result4[0]:,.2f} to {result4[1]:,.2f} {target_currency}")

if __name__ == "__main__":
    main()