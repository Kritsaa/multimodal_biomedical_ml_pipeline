import pandas as pd
from radiomics import featureextractor

def extract_features(images, labels=None):
    # Initialize default PyRadiomics extractor
    extractor = featureextractor.RadiomicsFeatureExtractor()
    features_list = []

    for i, img in enumerate(images):
        # Save temp image to file (PyRadiomics works with files)
        temp_file = f"temp_{i}.png"
        cv2.imwrite(temp_file, img)
        result = extractor.execute(temp_file)
        features_list.append(result)
        os.remove(temp_file)

    # Convert list of dicts to DataFrame
    features_df = pd.DataFrame(features_list)
    return features_df
