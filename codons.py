def create_codon_dict(file_path):
    codon_dict = {}

    with open(file_path, 'r') as f:
        rows = f.readlines()

    for row in rows:
        parts = row.strip().split('\t') 

        if len(parts) < 3:
            continue

        codon = parts[0].strip()
        amino_acid = parts[2].strip()

        codon_dict[codon] = amino_acid

    return codon_dict



