import csv
from collections import defaultdict


PROTOCOL_MAP = {
    "6": "tcp",
    "17": "udp",
    "1": "icmp"
}

def load_lookup_table(filepath):
    lookup = dict()
    with open(filepath, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            port = row['dstport'].strip()
            protocol = row['protocol'].strip().lower()
            tag = row['tag'].strip()
            lookup[(port, protocol)] = tag
    return lookup

def parse_flow_log(filepath, lookup):
    tag_counts = defaultdict(int)
    combo_counts = defaultdict(int)

    with open(filepath, mode='r') as f:
        for line in f:
            if not line.strip():
                continue  # skip empty lines

            parts = line.strip().split()
            if len(parts) < 14:
                continue  # not a valid flow log line

            dst_port = parts[5].strip().lower()
            protocol = PROTOCOL_MAP.get(parts[7].strip().lower(), "unknown")


            
            combo_counts[(dst_port, protocol)] += 1

            
            tag = lookup.get((dst_port, protocol))
            if tag:
                tag_counts[tag] += 1
            else:
                tag_counts["Untagged"] += 1

    return tag_counts, combo_counts

def write_tag_counts(tag_counts, filepath="tag_counts.csv"):
    with open(filepath, 'w') as f:
        f.write("Tag,Count\n")
        for tag, count in tag_counts.items():
            if count > 0:
                f.write(f"{tag},{count}\n")

def write_combo_counts(combo_counts, filepath="port_protocol_counts.csv"):
    with open(filepath, 'w') as f:
        f.write("Port,Protocol,Count\n")
        for (port, protocol), count in combo_counts.items():
            f.write(f"{port},{protocol},{count}\n")

def main():
    lookup_file = "lookup.csv"
    log_file = "flow_logs.txt"

    lookup = load_lookup_table(lookup_file)
    tag_counts, combo_counts = parse_flow_log(log_file, lookup)

    write_tag_counts(tag_counts)
    write_combo_counts(combo_counts)

    print("Processing complete. Output files:")
    print(" - tag_counts.csv")
    print(" - port_protocol_counts.csv")

if __name__ == "__main__":
    main()
