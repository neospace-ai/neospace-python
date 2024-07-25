#!/usr/bin/env -S poetry run python

import asyncio

from neospace import AsyncNeoSpace

# gets API Key from environment variable NEOSPACE_API_KEY
client = AsyncNeoSpace()


async def main() -> None:
    stream = await client.completions.create(
        model="7b-r16_lora_full_constrained-instruct",
        prompt="Say this is a test",
        stream=True,
    )
    async for completion in stream:
        print(completion.choices[0].text, end="")
    print()


asyncio.run(main())
