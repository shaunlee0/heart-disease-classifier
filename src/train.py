import osimport argparseimport joblib as jlimport pandas as pdimport numpy as npimport configimport model_dispatcherfrom sklearn import metricsdef run(fold, model):    df = pd.read_csv(config.TRAINING_FILE)    # All columns are features except id, target and kfold columns    features = [        f for f in df.columns if f not in ("output", "kfold")    ]    df_train = df[df.kfold != fold].reset_index(drop=True)    df_valid = df[df.kfold == fold].reset_index(drop=True)    # Transform training data    x_train = df_train[features]    x_valid = df_valid[features]    clf = model_dispatcher.models[model]    clf.fit(x_train, df_train["output"].values)    # Predict on validation data, we need probability values as we are calculating AUC    valid_preds = clf.predict_proba(x_valid)[:, 1]    # Get ROC AUC score    auc = metrics.roc_auc_score(df_valid["output"].values, valid_preds)    print(f"For fold {fold}, ROC AUC: {auc}, Model: {model}")    # Save the model    jl.dump(clf, os.path.join(config.MODEL_OUTPUT, f'model_{fold}.bin'))    # Initialise from previously dumped model    clf = jl.load(os.path.join(config.MODEL_OUTPUT, f'model_{fold}.bin'))    return aucdef train_final_model(top_fold):    df = pd.read_csv(config.TRAINING_FILE)    # All columns are features except id, target and kfold columns    features = [        f for f in df.columns if f not in ("output", "kfold")    ]    # Transform training data    x_train = df[features]    # Initialise from previously dumped model    clf = jl.load(os.path.join(config.MODEL_OUTPUT, f'model_{top_fold}.bin'))    clf.fit(x_train, df["output"].values)    # Save the model    jl.dump(clf, os.path.join(config.MODEL_OUTPUT, 'model_final.bin'))    # Test use of dumped model to predict on a row from dataframe    # output class [1: heart disease, 0: Normal]    print(x_train.iloc[:1].to_json())    print(f"Predict using saved model: {clf.predict(x_train.iloc[:1])}")if __name__ == "__main__":    parser = argparse.ArgumentParser()    parser.add_argument(        '--model',        type=str    )    args = parser.parse_args()    auc_scores = []    for i in range(5):        auc_score = run(fold=i, model=args.model)        auc_scores.append(auc_score)    top_scoring_fold = str(auc_scores.index(np.max(auc_scores)))    train_final_model(top_scoring_fold)