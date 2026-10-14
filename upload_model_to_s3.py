import argparse

import boto3


def upload_model_to_s3(model_path: str, bucket_name: str, s3_key: str) -> str:
    s3 = boto3.client("s3")
    s3.upload_file(model_path, bucket_name, s3_key)
    s3_uri = f"s3://{bucket_name}/{s3_key}"
    print(f"Uploaded to S3: {s3_uri}")
    return s3_uri


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload a trained model to S3.")
    parser.add_argument("--model-path", default="iris-model.pkl", help="Local path to the model file")
    parser.add_argument("--bucket", default="my-sagemaker-demo-bucket-abhishek", help="S3 bucket name")
    parser.add_argument("--key", default="model-artifacts/iris-model.pkl", help="Destination S3 key")
    args = parser.parse_args()

    upload_model_to_s3(args.model_path, args.bucket, args.key)
