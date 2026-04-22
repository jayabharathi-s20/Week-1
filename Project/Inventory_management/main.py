import csv
import logging
from datetime import datetime
from validator import Item

logging.basicConfig(
    filename="errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def read_inventory(file_path):
    items = []

    with open(file_path, "r") as file:
        reader = csv.DictReader(file) #Converts each row into a dictionary

        for row in reader:
            try:
                item = Item(                          #Item(...) creates, validates, and cleans one inventory record--raw CSV data becomes a structured object
                    item_id=int(row["item_id"]),
                    name=row["name"],
                    quantity=int(row["quantity"]),
                    threshold=int(row["threshold"]),
                    price=float(row["price"]),
                    category=row["category"],
                    supplier=row["supplier"],
                    expiry_date=datetime.strptime(row["expiry_date"], "%Y-%m-%d").date()#strptime = "String Parse Time" --It converts a string into a datetime object
                )

                items.append(item)

            except Exception as e:
                logging.error(f"Error in row {row}: {e}")

    return items


def low_stock_report(items):
    print("\nLOW STOCK ITEMS")
    # print("-" * 40)

    for item in items:
        if item.quantity <= item.threshold:
            print(f"{item.name} | Qty: {item.quantity} | Min: {item.threshold} | Price: {item.price} | Category: {item.category}")

if __name__ == "__main__":
    """
    Entry point of the program.

    This block runs only when the script is executed directly.
    It:
        1. Reads inventory data from CSV
        2. Generates a low stock report
    """
    inventory = read_inventory("inventory.csv")
    low_stock_report(inventory)