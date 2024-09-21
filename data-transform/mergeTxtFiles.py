import argparse
import os
import re


def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s

def merge_txt_files(folder_path):
    output_file = os.path.join(folder_path, 'output.txt')
    
    with open(output_file, 'w') as outfile:
        # Sort files to ensure consistent ordering
        files = sorted([f for f in os.listdir(folder_path) if f.endswith(".txt") and f != 'output.txt'])
        
        for index, filename in enumerate(files, start=1):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as infile:
                for line in infile:
                    # Extract timestamp
                    match = re.match(r'\[(\d{2}:\d{2}:\d{2})\](.*)', line)
                    if match:
                        time_str, content = match.groups()
                        seconds = time_to_seconds(time_str)
                        # Write the modified line
                        outfile.write(f"{index}-[{seconds}]{content.strip()}\n")
    
    print(f"All text files merged into {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge all text files in the folder into output.txt")
    parser.add_argument('folder_path', type=str, help='Path to the folder containing the text files')
    
    args = parser.parse_args()
    merge_txt_files(args.folder_path)