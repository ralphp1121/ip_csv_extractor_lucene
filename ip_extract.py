import csv
import re
import argparse

# Function to detect delimiter and extract IPs from CSV content
def detect_delimiter_and_extract_ips(csv_file_path):
    with open(csv_file_path, 'r') as file:
        csv_file_content = file.read()
    
    # Sniffer class to detect delimiter
    sniffer = csv.Sniffer()
    sample = csv_file_content[:1024]  # Take first 1024 chars to guess
    
    try:
        # Try detecting the delimiter
        dialect = sniffer.sniff(sample)
        delimiter = dialect.delimiter
    except csv.Error:
        # If detection fails, fallback to a default delimiter (comma)
        print("Could not determine delimiter, defaulting to comma.")
        print("Sample data being analyzed:\n", sample)
        delimiter = ','
    
    # Read the CSV
    rows = csv.reader(csv_file_content.splitlines(), delimiter=delimiter)
    
    # IP address regex patterns
    ipv4_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ipv6_pattern = r'\b(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}\b'
    
    # List to store identified IP addresses
    ip_addresses = []
    
    # Iterate over rows to find the IP address column
    for row in rows:
        for col in row:
            # Search for both IPv4 and IPv6 patterns in each column
            if re.search(ipv4_pattern, col):
                ip_addresses.append(col)
            elif re.search(ipv6_pattern, col):
                ip_addresses.append('"'+col+'"')
    
    return delimiter, ip_addresses

# Function to format IPs in Lucene format
def format_ips_lucene(ip_list):
    # Join all IP addresses with ' OR '
    return ' OR '.join(ip_list)

# Main function to handle the script logic
def main():
    # Setup argument parser
    parser = argparse.ArgumentParser(description='Extract IP addresses from CSV file and format in Lucene format.')
    parser.add_argument('csv_file', help='Path to the CSV file')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Extract IPs from the CSV file
    delimiter, ip_addresses = detect_delimiter_and_extract_ips(args.csv_file)
    
    # Format the IPs in Lucene format
    lucene_ip_list = format_ips_lucene(ip_addresses)
    
    # Output the formatted result
    print(delimiter)
    print(lucene_ip_list)
    

if __name__ == "__main__":
    main()
