import matplotlib.pyplot as plt
from datetime import datetime
from csv_importer import import_csv

def visualize_data(file_path):
    data = import_csv(file_path)

    plt.figure(figsize=(10, 6))

    for security in set(record['name'] for record in data):
        security_data = [record for record in data if record['name'] == security]
        timestamps = [record['date'] for record in security_data]
        dates = [datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S') for timestamp in timestamps]
        prices = [record['price'] for record in security_data]

        plt.plot(dates, prices, label=security, marker='o', linestyle='-')  

    plt.title('Preisentwicklung der Wertpapiere')
    plt.xlabel('Datum')
    plt.ylabel('Preis')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

