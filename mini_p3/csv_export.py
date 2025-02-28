import csv
from ocr_simulation import simulate_llm_ocr
from parsing_module import extract_from_texts, extract_transaction_details

def export_parsed_data_to_csv(parsed_data: list, filename: str) -> None:
    """
    Converts a list of structured JSON objects into a CSV file.

    Args:
        parsed_data (list of dict): List of structured data dictionaries.
        filename (str): Output CSV filename.

    Returns:
        None
    """
    if not parsed_data or not isinstance(parsed_data, list) or not all(isinstance(item, dict) for item in parsed_data):
        raise ValueError("Invalid input: parsed_data must be a list of dictionaries.")

    fieldnames = parsed_data[0].keys()  # Extract column names from the first item

    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()  # Write column headers
        writer.writerows(parsed_data)  # Write data rows

    print(f"CSV file '{filename}' generated successfully!")


# Example usage
# parsed_data_list = []
# for i in range (3):
#     parsed_data = extract_from_texts(simulate_llm_ocr("image.png", "receipt"))
#     parsed_data_list.append(parsed_data)
# print(parsed_data_list)
# export_parsed_data_to_csv(parsed_data_list, "output.csv")
