# Flow Log Parser and Tagging System

## Project Overview

This program parses flow log data from AWS VPC flow logs, maps each log entry to a tag based on a lookup table, and generates two summary CSV files:

- **Tag Counts**: Counts how many times each tag appears.
- **Port/Protocol Counts**: Counts how many times each port/protocol combination appears.

The lookup table contains mappings of destination ports and protocols to tags, and the program uses this table to classify flow logs based on the destination port and protocol.

## Features

### Input Files:
- **Flow log file**: A plain text file (typically in `.txt` format) containing flow log data.
- **Lookup file**: A CSV file (typically in `.csv` format) containing port, protocol, and corresponding tag mappings.

### Output Files:
- **tag_counts.csv**: Shows how many times each tag appears in the flow logs.
- **port_protocol_counts.csv**: Displays the count of each port/protocol combination.

## Assumptions

- **Log Format**: The program expects flow logs to be in the default AWS VPC flow log format (version 2), as described in the AWS documentation.
- **Case Sensitivity**: The program performs case-insensitive matching for the port, protocol, and tag values.
- **Valid Flow Log Lines**: Only lines containing at least 14 fields are considered valid flow log entries.
- **Lookup Table Format**: The lookup table file must have the following columns: `dstport`, `protocol`, and `tag`, and it is assumed that these mappings are case-insensitive.

## Installation and Running the Program

### Requirements
- Python 3.x
- No external libraries are required (the program uses standard Python libraries only).

### Files Required
- **Flow Log File**: A plain text file containing flow log data. Example: `flow_logs.txt`.
- **Lookup Table File**: A CSV file that maps destination ports and protocols to tags. Example: `lookup.csv`.

### Steps to Run
1. Clone or download this repository to your local machine.
2. Place the `flow_logs.txt` and `lookup.csv` files in the same directory as the script.
3. Open a terminal or command prompt.
4. Run the script by executing:

    ```bash
    python parser.py
    ```

## Expected Output
- **tag_counts.csv**: A CSV file with counts for each tag.
- **port_protocol_counts.csv**: A CSV file with counts for each port/protocol combination.

## Example Output Files

### `tag_counts.csv`
```csv
Tag,Count
sv_P2,1
sv_P1,2
sv_P4,1
email,3
Untagged,9
