📊 ExcelURLScan

ExcelURLScan is a simple Python utility to automatically scan URLs listed in an Excel file to check their availability (HTTP status codes, server errors, etc.).
Perfect for quick audits, broken link checks, or verifying accessibility of government or business websites.

🚀 Features

🧠 Reads URLs from Excel files (.xlsx)
🌐 Sends HTTP GET requests to each URL
✅ Saves results with status code and response details
📦 Lightweight and easy to use
🔧 Installation

Make sure you have Python 3 installed, then install the required libraries:

pip install pandas openpyxl requests

🛠️ Usage

Set the correct path to your Excel file in the script:
file_path = "C:/Users/Name/Downloads/your_file.xlsx"
Run the script:
python excel_url_scan.py