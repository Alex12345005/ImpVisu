from csv_importer import import_csv
from data_visualizer import visualize_data

def main():
    file_path = 'CSV/example.csv'

    import_csv(file_path)

    visualize_data(file_path)

if __name__ == "__main__":
    main()
