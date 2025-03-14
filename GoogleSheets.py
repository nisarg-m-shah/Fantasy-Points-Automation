import gspread
import pandas as pd
import time

# Authenticate using your service account JSON file
gc = gspread.service_account(filename="reliable-proton-449504-g2-d77e329f347c.json")

spreadsheet_name = "CFC Fantasy League"
try:
    spreadsheet = gc.open(spreadsheet_name)  # Try to open existing spreadsheet
except gspread.exceptions.SpreadsheetNotFound:
    spreadsheet = gc.create(spreadsheet_name)  # Create new spreadsheet if not found

# Load Excel file and its sheets
excel_file = "CFC Fantasy League.xlsx"
sheets = pd.ExcelFile(excel_file).sheet_names  # Get all sheet names

# Get existing sheet names in Google Sheets
existing_sheets = [ws.title for ws in spreadsheet.worksheets()]

for sheet_name in sheets:
    if sheet_name in existing_sheets:
        print(f"⏩ Skipping existing sheet: {sheet_name}")
        continue  # Skip updating this sheet

    # Read each sheet into a DataFrame (ignore index column to fix "Unnamed: 0" issue)
    df = pd.read_excel(excel_file, sheet_name=sheet_name, index_col=None)
    df.columns = [" " if col.startswith("Unnamed") else col for col in df.columns]  # Rename Unnamed columns to blank

    # Convert DataFrame to list of lists
    data = df.values.tolist()
    data.insert(0, df.columns.tolist())  # Add headers

    # Create new sheet and update data
    print(f"🆕 Creating new sheet: {sheet_name}")
    worksheet = spreadsheet.add_worksheet(title=sheet_name, rows="100", cols="20")

    # Batch update in **one API request** to avoid rate limits
    try:
        worksheet.update(range_name="A1", values=data)
        print(f"✅ Uploaded new sheet: {sheet_name}")  # Print confirmation
    except gspread.exceptions.APIError:
        print(f"⏳ Rate limit exceeded. Retrying {sheet_name} in 10 seconds...")
        time.sleep(10)  # Wait and retry once
        worksheet.update(range_name="A1", values=data)
        print(f"✅ Uploaded new sheet: {sheet_name} (after retry)")

    # Delay to prevent hitting API rate limits
    time.sleep(2)

print("🎉 All new sheets successfully uploaded to Google Sheets!")
