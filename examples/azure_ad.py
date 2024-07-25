from azure.identity import DefaultAzureCredential, get_bearer_token_provider

from neospace import AzureNeoSpace

token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default")


# may change in the future
# https://learn.microsoft.com/en-us/azure/ai-services/neospace/reference#rest-api-versioning
api_version = "2023-07-01-preview"

# https://learn.microsoft.com/en-us/azure/cognitive-services/neospace/how-to/create-resource?pivots=web-portal#create-a-resource
endpoint = "https://my-resource.neospace.azure.com"

client = AzureNeoSpace(
    api_version=api_version,
    azure_endpoint=endpoint,
    azure_ad_token_provider=token_provider,
)

completion = client.chat.completions.create(
    model="deployment-name",  # e.g. 7b-r16_lora_full_constrained-instant
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion.to_json())
