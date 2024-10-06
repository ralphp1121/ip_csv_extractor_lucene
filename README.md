# IP Address Extractor and Lucene Formatter

## Description

This Python script is designed to extract IP addresses (both IPv4 and IPv6) from a `.csv` file and format them into a **Lucene query format** for use in tools like **Kibana** or **databases** that require search filters based on IP addresses.

The script:
1. Automatically detects the delimiter used in the CSV file (or defaults to a comma if the detection fails).
2. Identifies and extracts IP addresses from any column in the CSV, using regular expressions to match both IPv4 and IPv6 formats.
3. Outputs the extracted IPs as a single Lucene query string, with IPs separated by `" OR "`.

This tool can be useful when you need to filter data in visualization tools like **Kibana** or when performing searches in a database using IPs as part of the query.

## How to Use

### Prerequisites

- You need **Python 3.x** installed on your system.
- Ensure your `.csv` file is well-formed and contains rows with IP addresses.

### Running the Script

1. **Download the script** and save it as `ip_extract.py`.

2. Open your terminal and navigate to the directory where the script is saved.

3. Run the script by providing the path to your `.csv` file as an argument. For example:

   ```bash
   python3 ip_extract.py /path/to/your/file.csv

Replace /path/to/your/file.csv with the actual path to your CSV file.

4. The script will:
- Print the detected delimiter (e.g., ,).
- Output the IP addresses in Lucene query format, which looks like this:

### Example
If you have a CSV file with the following content:

  ```bash
  id,username,ip_address
  1,user1,123.114.141.231
  2,user2,51.42.152.243
  3,user3,152.214.34.15
  4,user4,2001:0db8:85a3:0000:0000:8a2e:0370:7334
  ```

Running the command:
```
python3 ip_extract.py /path/to/your/file.csv
```

Will output:
```
,
123.114.141.231 OR 51.42.152.243 OR 152.214.34.15 OR "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
```

### Notes
- The script can handle both IPv4 and IPv6 addresses.
- If the delimiter in the CSV file cannot be automatically detected, the script will fall back to using a comma as the default delimiter.

##### Feel free to contribute to further improve this tool if it helps you too


