from ocr_simulation import simulate_llm_ocr
from parsing_module import extract_from_texts, extract_transaction_details
from csv_export import export_parsed_data_to_csv

def main():
    parsed_data_list = []
    for i in range (10):
        parsed_data = extract_from_texts(simulate_llm_ocr("image.png", "receipt"))
        parsed_data_list.append(parsed_data)
    # print(parsed_data_list)
    export_parsed_data_to_csv(parsed_data_list, "output.csv")

if __name__ == "__main__":
    main()
