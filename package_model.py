import argparse
import tarfile


def package_model(model_file: str, inference_file: str, output_tar: str = "model.tar.gz") -> str:
    with tarfile.open(output_tar, "w:gz") as tar:
        tar.add(model_file)
        tar.add(inference_file)

    print(f"Created package: {output_tar}")
    return output_tar


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Package the model and inference script for SageMaker.")
    parser.add_argument("--model", default="iris-model.pkl", help="Model file to include in the tarball")
    parser.add_argument("--inference", default="inference.py", help="Inference script to include in the tarball")
    parser.add_argument("--output", default="model.tar.gz", help="Output tar.gz file")
    args = parser.parse_args()

    package_model(args.model, args.inference, args.output)
