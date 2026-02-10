import pandas as pd
from src.imaging_preprocessing import load_images, normalize_image, resize_image
from src.radiomics_features import extract_features
from src.models import train_model
import numpy as np

# Load synthetic images
images = load_images()
images = [normalize_image(resize_image(img)) for img in images]

# Extract radiomics features
radiomics_df = extract_features(images)

# Load synthetic gene-expression data
gene_df = pd.read_csv("data/tabular/gene_expression.csv")

# Combine features (simple concat)
X = pd.concat([radiomics_df.reset_index(drop=True), gene_df], axis=1)

# Generate random labels for demonstration
y = np.random.randint(0, 2, size=X.shape[0])

# Train model
model, acc = train_model(X, y)

print(f"Trained RandomForest on synthetic data. Accuracy: {acc:.2f}")
