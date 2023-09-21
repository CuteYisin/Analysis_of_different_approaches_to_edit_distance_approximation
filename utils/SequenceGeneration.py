import random

# Defining the amino acid alphabet
amino_acids = "ACDEFGHIKLMNPQRSTVWY"

# Generate an initial sequence containing 50 amino acids
initial_sequence = ''.join(random.choice(amino_acids) for _ in range(50))

# Generate .fa file
with open('/data/cabins/yxxiang/QB/protein_50.fa', 'w') as fasta_file:
    for j in range(30): # A total of 30 sequences were generated
        seq = initial_sequence
        for i in range(50):  # Random walks for 50 steps
            # Random selection of add, delete or change operations
            operation = random.choice(["insert", "delete", "mutate"])

            if operation == "insert":
                # Random selection of insertion locations and amino acids
                insert_position = random.randint(0, len(seq))
                inserted_aa = random.choice(amino_acids)
                seq = (
                    seq[:insert_position]
                    + inserted_aa
                    + seq[insert_position:]
                )
            elif operation == "delete":
                # Random selection of deletion locations
                delete_position = random.randint(0, len(seq) - 1)
                seq = (
                    seq[:delete_position]
                    + seq[delete_position + 1:]
                )
            elif operation == "mutate":
                # Randomly select the position to be replaced and the new amino acid
                mutate_position = random.randint(0, len(seq) - 1)
                mutated_aa = random.choice(amino_acids.replace(seq[mutate_position], ""))
                seq = (
                    seq[:mutate_position]
                    + mutated_aa
                    + seq[mutate_position + 1:]
                )
        sequence_id = f">{j}\n"
        fasta_file.write(sequence_id)
        fasta_file.write(seq + "\n")