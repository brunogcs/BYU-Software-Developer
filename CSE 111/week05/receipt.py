# Creativity: Added a "return by" date 30 days in the future at 9:00 PM to exceed project requirements.

import os 
import csv
import datetime

abs_path = os.path.dirname(os.path.abspath(__file__))
fileProducts = "products.csv"
fileRequest  = "request.csv"

def read_dictionary(filename, key_column_index):
    dictProducts = {}
    with open(filename, "rt", encoding="utf-8") as openedFile:
        reader = csv.reader(openedFile)
        next(reader)
        for line in reader:
            qtdColumns = len(line)
            dictProducts[line[0]] = line[1:qtdColumns]
    return dictProducts

def main():
    try:
        #return product dictionary
        filename = os.path.join(abs_path, fileProducts)
        dictProducts = read_dictionary(filename, 0)

        #return request dictionary
        filename = os.path.join(abs_path, fileRequest)
        dictRequest = read_dictionary(filename, 0)

        #print(dictProducts.get('2'))
        #print(dictRequest)

        print("Welcome to the candy shop \n\n")

        priceIndex = 1
        total_items_ordered = 0
        amount_due = 0
        total_due = 0
        sales_tax_rate = 0.06
        for item_code, request_details in dictRequest.items(): 
            product_details = dictProducts.get(item_code)
            if product_details is not None:
                item_name = product_details[priceIndex - 1]
                price_per_item = float(product_details[priceIndex]) 
                quantity_ordered = int(request_details[0]) 
                total_price = price_per_item * quantity_ordered

                total_items_ordered += quantity_ordered
                amount_due += total_price

                # print JOIN result
                print(f"name: {item_name} | price per item: {price_per_item} | quantity ordered: {quantity_ordered} | total price: {total_price:.2f}")

            else:
                print(f" Item {item_code} not found 404!")

        print(f"\nTotal items ordered: {total_items_ordered}")
        print(f"Amount due: {amount_due:.2f}")
        print(f"Tax rate: {sales_tax_rate*100:.2f}%")
        sales_tax = amount_due * sales_tax_rate
        total_due = amount_due + sales_tax
        print(f"Total amount due: {total_due:.2f}")

        print(f"\nThank you for your purchase on {datetime.datetime.now():%Y-%m-%d %H:%M:%S}!")
        return_date = datetime.datetime.now() + datetime.timedelta(days=30)
        print(f"Return date until: {return_date.strftime('%d/%m/%Y at 9PM')}\n\n")

    except FileNotFoundError as error:
        print(error)
    except PermissionError as error:
        print(error)
    except KeyError as error:
        print(error)
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()