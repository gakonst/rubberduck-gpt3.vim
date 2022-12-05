#!/usr/bin/env python

import argparse
import json
import os
import requests


def query(args):
    # Read the chatgpt API key from the environment, if provided
    api_key = args["api_key"]
    env_api_key = os.environ.get("PAIR_API_KEY")
    if env_api_key:
        api_key = env_api_key

    # Construct the post request to the chatgpt API
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    data = {
        "model": args["model"],
        "prompt": args["query"],
        "temperature": 0.5,
        "max_tokens": 2048,
        "top_p": 1,
        "num_return_sequences": 1,
    }
    response = requests.post(
        "https://api.openai.com/v1/completions", headers=headers, json=data
    )

    return response


def main():
    # Parse the command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--start-line",
        type=int,
        required=True,
        help="The start line number of the selected text",
    )
    parser.add_argument(
        "--end-line",
        type=int,
        required=True,
        help="The end line number of the selected text",
    )
    parser.add_argument(
        "--filename", type=str, required=True, help="The active buffer's filename"
    )
    parser.add_argument(
        "--query", type=str, required=True, help="The user-specified query string"
    )
    parser.add_argument(
        "--api-key", type=str, required=True, help="The chatgpt API key"
    )
    parser.add_argument(
        "--model", type=str, default="text-davinci-002", help="The chatgpt model to use"
    )
    args = parser.parse_args()

    # Read the file's content
    with open(args.filename) as f:
        file_contents = f.read()

    # Get the selected lines
    selected_lines = file_contents.split("\n")[args.start_line - 1 : args.end_line]

    # Put the arguments, file contents, and selected lines in a dictionary
    args_dict = vars(args)
    args_dict["file_contents"] = file_contents
    args_dict["selected_lines"] = selected_lines

    try:
        # Make the chatgpt API request
        response = query(args)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the chatgpt API request: {e}")
        exit(1)
    except Exception as e:
        print(f"An error occurred while processing the chatgpt response: {e}")
        exit(1)
    print(response.json())


if __name__ == "__main__":
    main()
