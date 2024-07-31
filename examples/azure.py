from neospace import AzureNeoSpace

# may change in the future
# https://learn.microsoft.com/en-us/azure/ai-services/neospace/reference#rest-api-versioning
api_version = "2023-07-01-preview"

# gets the API Key from environment variable AZURE_NEOSPACE_API_KEY
client = AzureNeoSpace(
    api_version=api_version,
    # https://learn.microsoft.com/en-us/azure/cognitive-services/neospace/how-to/create-resource?pivots=web-portal#create-a-resource
    azure_endpoint="https://example-endpoint.neospace.azure.com",
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


deployment_client = AzureNeoSpace(
    api_version=api_version,
    # https://learn.microsoft.com/en-us/azure/cognitive-services/neospace/how-to/create-resource?pivots=web-portal#create-a-resource
    azure_endpoint="https://example-resource.azure.neospace.com/",
    # Navigate to the Azure NeoSpace Studio to deploy a model.
    azure_deployment="deployment-name",  # e.g. 7b-r16_lora_full_constrained-instant
)

completion = deployment_client.chat.completions.create(
    model="<ignored>",
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion.to_json())
