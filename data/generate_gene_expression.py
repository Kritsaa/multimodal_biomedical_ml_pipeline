
import numpy as np
import pandas as pd
import os

# Create folder to save CSV
os.makedirs("data/tabular", exist_ok=True)

num_samples = 50     # number of patients/samples
num_genes = 500      # number of gene-like features

# Generate random gene expression data
data = np.random.rand(num_samples, num_genes)

# Column names like Gene_1, Gene_2, etc.
columns = [f"Gene_{i+1}" for i in range(num_genes)]

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Save CSV
df.to_csv("data/tabular/gene_expression.csv", index=False)

print(f"Synthetic gene-expression data saved in data/tabular/gene_expression.csv")
