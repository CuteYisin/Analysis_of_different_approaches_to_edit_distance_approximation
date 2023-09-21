import numpy as np
from scipy.stats import pearsonr
from scipy.stats import spearmanr

txt1=[]
valid_values1=[]
t=50

file_paths = [
    f'/data/cabins/yxxiang/QB/protein_{t}/4-4/CosineDistance.txt',
    f'/data/cabins/yxxiang/QB/protein_{t}/4-4/JaccardDistance.txt',
    f'/data/cabins/yxxiang/QB/protein_{t}/4-4/L1Distance.txt',
    f'/data/cabins/yxxiang/QB/protein_{t}/4-4/L2Distance.txt',
    f'/data/cabins/yxxiang/QB/protein_{t}/5-4/CosineDistance.txt',
    f'/data/cabins/yxxiang/QB/protein_{t}/5-4/JaccardDistance.txt',
    f'/data/cabins/yxxiang/QB/protein_{t}/5-4/L1Distance.txt',
    f'/data/cabins/yxxiang/QB/protein_{t}/5-4/L2Distance.txt'
]

with open(f'/data/cabins/yxxiang/QB/protein_{t}/EditDistance.txt', 'r') as file:
    lines = file.readlines()
for i, line in enumerate(lines):
    values = line.strip().split('\t')
    for value in values:
        txt1.append(value)
for value in txt1:
    if value.strip():
        valid_values1.append(float(value))
float_array1 = np.array(valid_values1)
        
for j, file_path in enumerate(file_paths, 1):
    txt2=[]
    valid_values2=[]
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for i, line in enumerate(lines):
        values = line.strip().split('\t')
        for value in values:
            txt2.append(value)
    for value in txt2:
        if value.strip():
            valid_values2.append(float(value))

    float_array2 = np.array(valid_values2)

    if len(float_array1) != len(float_array2):
        print("File data shape mismatch.")
    else:
        correlation_coefficient, _ = spearmanr(float_array1, float_array2)
        
        title_parts = file_path.split('/')
        title = title_parts[-1].split('D')[0]
        print(f"Pearson's coefficient of {title}:", correlation_coefficient)