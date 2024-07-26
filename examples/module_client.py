import neospace

# will default to `os.environ['NEOSPACE_API_KEY']` if not explicitly set
neospace.api_key = "..."

# all client options can be configured just like the `NeoSpace` instantiation counterpart
neospace.base_url = "https://..."
neospace.default_headers = {"x-foo": "true"}

# all API calls work in the exact same fashion as well
stream = neospace.chat.completions.create(
    model="7b-r16_lora_full_constrained",
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
    stream=True,
)

for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="", flush=True)

print()
