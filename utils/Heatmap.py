import numpy as np
import matplotlib.pyplot as plt

t=5

# List of file paths files contains multiple file paths to be processed
file_paths = [
    f'/data/cabins/yxxiang/QB/protein_{t}/EditDistance.txt',
    f'/data/cabins/yxxiang/QB/protein_{t}/4-4/CosineDistance.txt',
    f'/data/cabins/yxxiang/QB/protein_{t}/4-4/JaccardDistance.txt',
    f'/data/cabins/yxxiang/QB/protein_{t}/4-4/L1Distance.txt',
    f'/data/cabins/yxxiang/QB/protein_{t}/4-4/L2Distance.txt',
    f'/data/cabins/yxxiang/QB/protein_{t}/5-4/CosineDistance.txt',
    f'/data/cabins/yxxiang/QB/protein_{t}/5-4/JaccardDistance.txt',
    f'/data/cabins/yxxiang/QB/protein_{t}/5-4/L1Distance.txt',
    f'/data/cabins/yxxiang/QB/protein_{t}/5-4/L2Distance.txt'
]

# Calculate the number of columns to display (how many heat maps to display per row)
columns = 5

total_files = len(file_paths)
rows = (total_files + columns - 1) // columns

fig = plt.figure(figsize=(21, 7))

for i, file_path in enumerate(file_paths, 1):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    n = len(lines)
    matrix = np.zeros((n, n))

    for k, line in enumerate(lines):
        values = line.strip().split('\t')
        row = k
        matrix[row, row] = 0
        for j, value in enumerate(values):
            col = j + k + 1
            if value != '':
                matrix[row, col] = float(value)
                matrix[col, row] = float(value)

    lower_triangle = np.tril(np.rot90(matrix))
    mask = np.tri(matrix.shape[0], matrix.shape[1], k=-1).T
    matrix_with_transparency = np.ma.masked_where(mask, matrix)

    # Create subgraphs, horizontally
    if i>5:
        fig = plt.subplot(rows, columns, i+1)
    else:
        fig = plt.subplot(rows, columns, i)
    
    title_parts = file_path.split('/')
    title = title_parts[-1].split('D')[0]

    plt.imshow(matrix_with_transparency, cmap="YlGnBu")
    plt.colorbar()
    plt.axis('off')
    if i<6:
        plt.title(f'{title}', fontsize=20)

plt.tight_layout()
plt.savefig(f'/data/cabins/yxxiang/QB/protein_{t}/heatmap.png', dpi=1000)
plt.show()