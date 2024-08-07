#!/usr/bin/env -S poetry run python

import uuid
from neospace import NeoSpace

# gets API Key from environment variable NEOSPACE_API_KEY
client = NeoSpace()

# Non-streaming:
# print("----- standard request -----")
# completion = client.chat.completions.create(
#     model="7b-r16_lora_full_constrained",
#     messages=[
#         {
#             "role": "user",
#             "content": "Say this is a test",
#         },
#     ],
#     extra_body={
#         "metadata": {
#             "session_id": uuid.uuid4(),
#         }
#     }
# )
# print(completion.choices[0].message.content)

# Streaming:
print("----- streaming request -----")
stream = client.chat.completions.create(
    model="personal-loan-lora-1",
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
    extra_body={
        "metadata": {
            "session_id": f"session_{uuid.uuid4()}",
        }
    },
    stream=True,
)
for chunk in stream:
    # print(chunk)
    if not chunk.choices or not chunk.choices[0].delta.content:
        continue

    print(chunk.choices[0].delta.content, end="")
print()

# Response headers:
# print("----- custom response headers test -----")
# response = client.chat.completions.with_raw_response.create(
#     model="7b-r16_lora_full_constrained",
#     messages=[
#         {
#             "role": "user",
#             "content": "Say this is a test",
#         }
#     ],
#     extra_body={
#         "metadata": {
#             "session_id": f"session_{uuid.uuid4()}",
#         }
#     },
# )
# completion = response.parse()
# print(response.request_id)
# print(completion.choices[0].message.content)
