def filter_proteins(unique_genes_file, input_proteins_file, output_file):
    # Считываем уникальные гены
    with open(unique_genes_file, "r") as unique_genes_file:
        unique_genes = set(line.split()[0] for line in unique_genes_file if line.startswith("g"))

    # Отфильтровываем белки
    with open(input_proteins_file, "r") as input_file, open(output_file, "w") as output_file:
        writing = False
        for line in input_file:
            if line.startswith(">"):
                protein_name = line.split()[0][1:]
                writing = protein_name in unique_genes
            if writing:
                output_file.write(line)

# Задаем пути к файлам
unique_genes_file_path = "output_protein_type.txt"
input_proteins_file_path = "augustus.whole.aa"
output_file_path = "filtered_augustus.whole.aa"

# Фильтруем белки
filter_proteins(unique_genes_file_path, input_proteins_file_path, output_file_path)
