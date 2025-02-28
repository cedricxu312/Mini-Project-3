import re
import json
from typing import List, Dict, Optional
from ocr_simulation import simulate_llm_ocr

def extract_transaction_details(text: str) -> Optional[Dict]:
    patterns = [
        # Pattern for "06/02/2024 Fee Collected... -$14.60"
        re.compile(r"(?P<date>\d{2}/\d{2}/\d{4})\s+(?P<description>.+?)\s+(?P<status>Collected|Completed|Incompleted)\s+.*?(?P<amount>-?\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?)"),
        
        # Pattern for transactions with asterisks like "10/24/24* CHUKWUEMEKA EZEUME AMAZON ... -$307.91"
        re.compile(r"(?P<date>\d{2}/\d{2}/\d{2})\*?\s+(?P<description>.+?)\s+(?P<amount>-?\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?)"),
        
        # Pattern for "Dec 02 Deposit ACH ... 217.25 12,013.52 TYPE: DEPOSIT"
        re.compile(r"(?P<date>[A-Za-z]{3}\s\d{2})\s+(?P<description>.+?)\s+(?P<amount>-?\d{1,3}(?:,\d{3})*(?:\.\d{2})?)"),
        
        # Pattern for "12/02 Recurring Card Purchase 11/30 Desklog.lo Kozhikode Card 8928 $9.60"
        re.compile(r"(?P<date>\d{2}/\d{2})\s+(?P<description>.+?)\s+Card\s+\d{4}\s+(?P<amount>-?\$?\d{1,3}(?:,\d{3})*(?:\.\d{2})?)"),
    ]
    
    for pattern in patterns:
        match = pattern.search(text)
        if match:
            return {
                "date": match.group("date"),
                "description": match.group("description"),
                "amount": match.group("amount"),
                "status": match.group("status") if "status" in match.groupdict() else "Unknown"
            }
    return None

def extract_from_texts(dummy_output: dict) -> dict:
    texts = [dummy_output['text']]
    for text in texts:
        result = extract_transaction_details(text)
        if result:
            return result
    return

# Example usage
# dummy_ocr_result = simulate_llm_ocr("Online payments deposits OPEX-1187 (June 2024) (1).pdf", "bank_statement")
# r = extract_from_texts(dummy_ocr_result)
# print(r)



