import os

def clean_entry(line, ignore_case_and_spaces):
    """Cleans and formats a line based on the matching mode."""
    if ignore_case_and_spaces:
        return line.strip().lower()
    return line.rstrip('\n')

def process_duplicate_finder():
    filename = input("Enter the file name (e.g., data.txt): ").strip()
    
    if not os.path.exists(filename):
        print(f"File '{filename}' not found. Please enter a valid file name.")
        return
        
    if os.stat(filename).st_size == 0:
        print("File is empty. Nothing to check.")
        return

    print("\nMenu Options:")
    print("1. Exact match")
    print("2. Ignore case and extra spaces")
    option = input("Select an option (1 or 2): ").strip()
    
    ignore_case_and_spaces = (option == "2")

    raw_entries = []
    with open(filename, 'r') as file:
        for line in file:
            raw_entries.append(line)

    processed_entries = [clean_entry(line, ignore_case_and_spaces) for line in raw_entries if line.strip() or not ignore_case_and_spaces]

    if ignore_case_and_spaces:
        processed_entries = [entry for entry in processed_entries if entry != ""]

    unique_set = set(processed_entries)
    
    total_items = len(processed_entries)
    unique_items_count = len(unique_set)

    counts = {}
    for entry in processed_entries:
        counts[entry] = counts.get(entry, 0) + 1

    duplicates_list = []
    for item, count in counts.items():
        if count > 1:
            duplicates_list.append(f"{item} ({count} times)")

    print("\n--- OUTPUT ---")
    print(f"Total items: {total_items} | Unique items: {unique_items_count}")
    
    if duplicates_list:
        print("Duplicates: " + " | ".join(duplicates_list))
    else:
        print("No duplicates found.")

    try:
        with open("unique.txt", "w") as out_file:
            for item in sorted(unique_set):
                out_file.write(item + "\n")
        print("Unique list saved to unique.txt")
    except Exception as e:
        print(f"Error saving unique file: {e}")

if __name__ == "__main__":
    process_duplicate_finder()