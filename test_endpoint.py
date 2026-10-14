import argparse
import json

import boto3


def invoke_endpoint(endpoint_name: str, payload: list[list[float]], region_name: str = "us-east-1") -> dict:
    client = boto3.client("sagemaker-runtime", region_name=region_name)
    request_body = json.dumps({"instances": payload})

    response = client.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType="application/json",
        Body=request_body,
    )

    result = json.loads(response["Body"].read().decode("utf-8"))
    print(json.dumps(result, indent=2))
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Invoke a deployed SageMaker endpoint for inference.")
    parser.add_argument("--endpoint-name", default="iris-demo-endpoint", help="Name of your SageMaker endpoint")
    parser.add_argument("--region", default="us-east-1", help="AWS region for the endpoint")
    parser.add_argument(
        "--sample",
        nargs="+",
        type=float,
        default=[5.1, 3.5, 1.4, 0.2],
        help="Feature vector to send to the endpoint",
    )
    args = parser.parse_args()

    invoke_endpoint(args.endpoint_name, [args.sample], args.region)
