import pandas as pd


def load_data(file_path):
    """
    Load data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pandas.DataFrame: The loaded data.
    """
    data = pd.read_csv(file_path)
    return data


def preprocess_data(data):
    """
    Preprocess the data for model training.

    This function extracts molecular weights from the columns,
    formats the data, and combines it into a single DataFrame.
    It then separates the features (X) and target (y) variables.

    Parameters:
    data (pandas.DataFrame): The raw data.

    Returns:
    tuple: A tuple containing the feature matrix (X) and target array (y).
    """
    # Extract molecular weights from the columns
    molecular_weights = [col.split(" ")[0] for col in data.columns if " (Å)" in col]

    # Create a DataFrame to hold the preprocessed data
    preprocessed_data = []

    for mw in molecular_weights:
        mw_data = data[["Concentration", f"{mw} (Å)", f"{mw} Err (Å)"]]
        mw_data["Molecular Weight"] = (
            int(mw[:-1]) * 1000
        )  # Convert to integer and multiply by 1000
        mw_data.rename(
            columns={f"{mw} (Å)": "Thickness", f"{mw} Err (Å)": "Error"}, inplace=True
        )

        # Convert thickness from Å to nm
        mw_data["Thickness"] = mw_data["Thickness"] / 10.0
        mw_data["Error"] = mw_data["Error"] / 10.0

        preprocessed_data.append(mw_data)

    preprocessed_data = pd.concat(preprocessed_data, ignore_index=True)
    X = preprocessed_data[["Molecular Weight", "Concentration"]].values
    y = preprocessed_data["Thickness"].values

    return X, y
