import re

def parse_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    motif_ids_and_motifs = re.findall(r'\s+(\d+)\s+(\d+)\s+(.*?)\s+(\d+)\s+(.*?)$', content, re.MULTILINE)
    motif_dict = {motif: alt_id for motif, id, alt_id, width, match in motif_ids_and_motifs}
    numbers_in_brackets = re.findall(r'\[(\d+)\]', content)

    for number in numbers_in_brackets:
        if number in motif_dict:
            alt_id = motif_dict[number]
            print(f"Number: {number}, MOTIF: {number}, ALT ID: {alt_id}")
        else:
            print(f"Number {number} not found in the dictionary.")

parse_file('mast.txt')

