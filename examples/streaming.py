#!/usr/bin/env -S poetry run python

from neospace import NeoSpace

# This script assumes you have the NEOSPACE_API_KEY environment variable set to a valid NeoSpace API key.
#
# You can run this script from the root directory like so:
# `python examples/streaming.py`


def sync_main() -> None:
    client = NeoSpace()
    response = client.completions.create(
        model="7b-r16_lora_full_constrained-instruct",
        prompt="1,2,3,",
        max_tokens=5,
        temperature=0,
        stream=True,
    )

    # You can manually control iteration over the response
    first = next(response)
    print(f"got response data: {first.to_json()}")

    # Or you could automatically iterate through all of data.
    # Note that the for loop will not exit until *all* of the data has been processed.
    for data in response:
        print(data.to_json())



sync_main()
