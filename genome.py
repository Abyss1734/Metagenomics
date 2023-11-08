import argparse

def read_fasta(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    sequence = ''
    for line in lines[1:]:
        sequence += line.strip()

    return sequence

def predict_genes(dna_sequence):
    genes = []
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]

    start_positions = [i for i in range(len(dna_sequence) - 2) if dna_sequence[i:i+3] == start_codon]

    for start_pos in start_positions:
        for stop_codon in stop_codons:
            stop_pos = dna_sequence.find(stop_codon, start_pos)
            if stop_pos != -1 and (stop_pos - start_pos) % 3 == 0:
                genes.append((start_pos, stop_pos + 2))

    return genes

def write_bed_file(genes, output_file):
    with open(output_file, 'w') as file:
        for i, gene in enumerate(genes, start=1):
            file.write(f"seq\t{gene[0]}\t{gene[1]}\tgene{i}\t0\t+\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Predict genes from a DNA sequence in a FASTA file and create a BED file.")
    parser.add_argument("input_file", help="Path to the input FASTA file")
    parser.add_argument("output_file", help="Path to the output BED file")

    args = parser.parse_args()

    fasta_file_path = args.input_file
    bed_file_path = args.output_file

    dna_sequence = read_fasta(fasta_file_path)
    predicted_genes = predict_genes(dna_sequence)
    write_bed_file(predicted_genes, bed_file_path)
