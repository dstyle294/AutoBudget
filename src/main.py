import argparse
import ingest

def main():
    parser = argparse.ArgumentParser(
        prog='Automatic Budgeter',
        description='Pass in a CSV file, get categorized transactions'
    )
    parser.add_argument('csv_file')

    args = parser.parse_args()
    csv_path = args.csv_file

    df = ingest.parse(csv_path)
       

if __name__ == "__main__":
    main()