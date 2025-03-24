from scripts.preprocess import preprocess_text
from scripts.drift_generator import simulate_drift
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scripts.enums import WordErrorType
from sklearn.metrics.pairwise import cosine_similarity


def generate_drifted_text(
    df: pd.DataFrame,
    error_type: WordErrorType = WordErrorType.TYPOGRAPHICAL,
    level: float = 0.1,
    print_info: bool = False,
) -> pd.DataFrame:
    """Generate drifted text data based on the error type and level.
    Input object must be a pandas dataframe containing data and target columns.

    Returns:
        pd.Dataframe: Dataframe containing original_data, original_preprocessed_data, drifted_data, drifted_preprocessed_data, and target columns.
    """
    if print_info:
        print(f"Simulating {error_type} errors at level {level}:")

    s_time = time.time()

    # Preprocess text data and remove empty samples
    original_texts = []
    original_preprocessed_texts = []
    drifted_texts = []
    drifted_preprocessed_texts = []
    targets = []

    for text, target in zip(df.data, df.target):
        # Aplly drift to data
        drifted_text = simulate_drift(text, error_type, level=level)
        if drifted_text:  # Check if text is not empty after preprocessing
            original_preprocessed_text = preprocess_text(text)
            drifted_preprocessed_text = preprocess_text(drifted_text)

            if (
                original_preprocessed_text and drifted_preprocessed_text
            ):  # Check if text is not empty after preprocessing
                original_texts.append(text)
                original_preprocessed_texts.append(original_preprocessed_text)
                drifted_texts.append(drifted_text)
                drifted_preprocessed_texts.append(drifted_preprocessed_text)
                targets.append(target)

    # Create a new DataFrame with preprocessed data
    full_df = pd.DataFrame(
        {
            "original_data": original_texts,
            "original_preprocessed_data": original_preprocessed_texts,
            "drifted_data": drifted_texts,
            "drifted_preprocessed_data": drifted_preprocessed_texts,
            "target": targets,
        }
    )
    e_time = time.time()

    if print_info:
        print(f"Done in {e_time-s_time} s\n")

    return full_df


def plot_cosine_similarity_box_plots(
    levels: list[float],
    error_type: str,
    X_list: list[np.ndarray],
    X_drifted_list: list[np.ndarray],
) -> None:
    # Assuming X is your reference dataset and X_drifted is a list of drifted datasets
    cosine_similarities_list = []  # List to store cosine similarities for each drifted dataset
    labels = []  # Labels for the boxplots

    for idx in range(len(levels)):  # Loop through each drifted dataset
        cosine_similarities = [
            cosine_similarity([X_list[idx][i]], [X_drifted_list[idx][i]])[0][0]
            for i in range(len(X_list[idx]))
        ]
        cosine_similarities_list.append(cosine_similarities)
        labels.append(f"Drift level {levels[idx]}")  # Label each drifted dataset
        average_similarity = np.mean(cosine_similarities)
        print(
            f"Average Cosine Similarity at level {levels[idx]}: {average_similarity:.4f}"
        )

    # Plot the boxplots for each drifted dataset
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=cosine_similarities_list)
    plt.xticks(ticks=range(len(labels)), labels=labels)
    plt.title(f"Cosine Similarity Distribution for {error_type} drift")
    plt.ylabel("Cosine Similarity")
    plt.xlabel("Drifted Datasets")
    plt.show()
