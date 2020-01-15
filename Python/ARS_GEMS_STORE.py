# ARS Gems Store sells different varieties of gems to its customers.

# Write a Python program to calculate the bill amount to be paid by a customer based on the
# list of gems and quantity purchased. Any purchase with a total bill amount above
# Rs.30000 is entitled for 5% discount. If any gem required by the customer is not available in the
# store, then consider total bill amount to be -1.

# Assume that quantity required by the customer for any gem will always be greater than 0.

# Perform case-sensitive comparison wherever applicable.


def calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity):
    bill_amount = 0
    # Write your logic here
    # Validate if Gems required by the customer are available in the store.
    for gems in reqd_gems:
        if(gems not in gems_list):
            bill_amount = -1
            return bill_amount

    quantity_dict = dict(zip(reqd_gems, reqd_quantity))
    price_dict = dict(zip(gems_list, price_list))
    # for k, v in quantity_dict.items():
    #     print(k, v, price_dict[k] * v)
    Grand_total = sum([price_dict[k] * v for k, v in quantity_dict.items()])
    if(Grand_total > 30000):
        bill_amount = Grand_total - (Grand_total*0.05)
    else:
        bill_amount = Grand_total

    return bill_amount


# List of gems available in the store
# ["Emerald", "Ivory", "Jasper", "Ruby", "Garnet"]
# ['Moonstone', 'Sapphire', 'Quartz']
gems_list = ['Beryl', 'Garnet', 'Quartz']

# Price of gems available in the store. gems_list and price_list have one-to-one correspondence
# [4392, 1342, 8734, 6421]  # [1760, 2119, 1599, 3920, 3999]
price_list = [8723, 2346, 7532]

# List of gems required by the customer
reqd_gems = ['Beryl']  # ['Ivory']  # ["Ivory", "Emerald", "Garnet"]

# Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity = [2]  # [10]  # [3, 10, 12]

bill_amount = calculate_bill_amount(
    gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)
