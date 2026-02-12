import requests
from bs4 import BeautifulSoup
import csv

# Fetch the Wikipedia page
url = "https://en.wikipedia.org/wiki/Machine_learning"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the main content area
main_content = soup.find('div', {'id': 'mw-content-text'})

if main_content:
    # Find all tables in the main content area
    tables = main_content.find_all('table')

    target_table = None

    # Search for the first table with at least 3 data rows
    for table in tables:
        # Get all rows
        rows = table.find_all('tr')

        # Count rows that have td elements (actual data rows)
        data_rows = [row for row in rows if row.find('td')]

        if len(data_rows) >= 3:
            target_table = table
            break

    if target_table:
        # Extract all rows
        all_rows = target_table.find_all('tr')

        # Try to find header row with th tags
        header_row = None
        th_tags = []
        for row in all_rows:
            th_tags = row.find_all('th')
            if th_tags:
                header_row = row
                break

        headers = []
        if th_tags:
            # Extract headers from th tags
            headers = [th.get_text(strip=True) for th in th_tags]
        else:
            # Create default headers based on first row's column count
            first_row = all_rows[0] if all_rows else None
            if first_row:
                cells = first_row.find_all(['td', 'th'])
                num_cols = len(cells)
                headers = [f'col{i + 1}' for i in range(num_cols)]

        # Determine max columns
        max_cols = len(headers) if headers else 0
        if max_cols == 0:
            # Scan all rows to find max columns
            for row in all_rows:
                cells = row.find_all(['td', 'th'])
                max_cols = max(max_cols, len(cells))
            headers = [f'col{i + 1}' for i in range(max_cols)]

        # Extract data rows
        data = []
        for row in all_rows:
            cells = row.find_all(['td', 'th'])
            if cells:  # Only process rows with cells
                row_data = [cell.get_text(strip=True) for cell in cells]

                # Pad with empty strings if needed
                while len(row_data) < max_cols:
                    row_data.append('')

                data.append(row_data)

        # Write to CSV
        with open('wiki_table.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)

            # Write headers
            if headers:
                writer.writerow(headers)

            # Write data rows
            for row in data:
                writer.writerow(row)

        print(f"Success! Extracted table with {len(data)} rows")
        print(f"Saved to wiki_table.csv")
    else:
        print("No table with at least 3 data rows found.")
else:
    print("Main content area not found.")
