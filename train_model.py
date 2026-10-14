import os

from joblib import dump
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier


def train_and_save_model(output_path: str = "iris-model.pkl") -> str:
    iris = load_iris()
    X, y = iris.data, iris.target

    model = DecisionTreeClassifier()
    model.fit(X, y)

    dump(model, output_path)
    print(f"Model saved as {output_path}")
    return output_path


if __name__ == "__main__":
    train_and_save_model()
