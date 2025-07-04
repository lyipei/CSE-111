#Yipei Lin
#CSE111-08

import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    
    try:
        with open(filename, 'r', newline= '') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                key = row[key_column_index]
                dictionary[key] = row
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

    return dictionary


def main():
    store_name = "Inkom Emporium"
    products_dict = read_dictionary('W9_products.csv', 0)

    if not products_dict:
        return

    requested_items = {}

    try:

        with open('W9_request.csv', 'r', newline= '') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                product_number = row[0]
                quantity = int(row[1])

                if product_number in products_dict:
                    product_info = products_dict[product_number]
                    product_name = product_info[1]
                    product_price = float(product_info[2])

                    if datetime.now().strftime('%A') in ['Tuesday', 'Wednesday']:
                        product_price = product_price * 0.9

                    if product_name in requested_items:
                        requested_items[product_name][0] += quantity
                    else:
                        requested_items[product_name] = [quantity, product_price]
                else:
                    print(f"Error: Product with ID {product_number} not found.")
    except FileNotFoundError:
        print("Error: Request file not found.")

    print(f"{store_name}")
    
    total_items = 0

    print("\nRequested Items:")
    subtotal = 0
    for product_name, info in requested_items.items():
        quantity = info[0]
        price = info[1]
        total_items += quantity
        subtotal += quantity * price
        print(f"{product_name} {quantity} @ {price:.2f}")

    if total_items > 0:
        sales_tax_rate = 0.06
        sales_tax_amount = subtotal * sales_tax_rate
        total_amount_due = subtotal +sales_tax_amount

        print(f"\nTotal items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: ${sales_tax_amount:.2f}")
        print(f"Total: ${total_amount_due:.2f}")

        current_datetime = datetime.now()
        print(f"Thank you for shopping at the Inkom Emporium.")
        print(f"{current_datetime}")


            
if __name__ == "__main__":
    main()