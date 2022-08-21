import numpy as np
import pandas as pd

from sklearn import model_selection


def create_folds(data):
    data["kfold"] = -1
    # Randomise the rows of the data
    data = data.sample(frac=1).reset_index(drop=True)

    # Calculate the number of bins by using Sturge's rule
    num_bins = int(np.floor(1 + np.log2(len(data))))

    # bin targets
    data.loc[:, "bins"] = pd.cut(
        data["output"], bins=num_bins, labels=False
    )

    # Initialise the kfold class from model_selection module,
    # n defines how many folds we are using
    kf = model_selection.StratifiedKFold(n_splits=5)

    # Fill in the new kfold column, instead of targets we use bins
    for f, (t_,v_) in enumerate(kf.split(X=data, y=data.bins.values)):
        data.loc[v_, 'kfold'] = f

    # Drop the bins column
    data = data.drop("bins", axis=1)

    return data

if __name__ == "__main__":
    df = pd.read_csv("../input/heart.csv")
    df = create_folds(df)
    df.to_csv(path_or_buf="../input/heart_folds.csv", index=None)
