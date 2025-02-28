import random

def simulate_llm_ocr(image_filename: str, document_type: str) -> dict:

    # Randomized values for better simulation
    dummy_response_examples = [
        "06/02/2024 Fee Collected Wendy Granone 10467.01 Fee: Online payments for Trust Request #67412 - -$14.60 -$14.60", 
        "10/24/24* CHUKWUEMEKA EZEUME AMAZON SHOP WITH POINTS CREDIT -$307.91",
        "Dec 02 Deposit ACH MERCHANT BANKCD 217.25 12,013.52 TYPE: DEPOSIT ID: G592126793 DATA: PPI BANKCARD DEP CO: MERCHANT BANKCD",
        "12/02 Recurring Card Purchase 11/30 Desklog.lo Kozhikode Card 8928 $9.60"
        ]
    dummy_response_example = random.choice(dummy_response_examples)

    return {"text": dummy_response_example, "image_filename": image_filename, "document_type": document_type}

# Example usage
# dummy_ocr_result = simulate_llm_ocr("Online payments deposits OPEX-1187 (June 2024) (1).pdf", "bank_statement")
# print(dummy_ocr_result)
