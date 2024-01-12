import csv

def import_csv(file_path):
    data = []
    with open(file_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            name, date, price, currency, location = row
            data.append({
                'name': name,
                'date': int(date),
                'price': float(price),
                'currency': currency,
                'location': location
            })
    return data
