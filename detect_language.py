import asyncio
from typing import Annotated
from genai_session.session import GenAISession
from genai_session.utils.context import GenAIContext
from langdetect import detect, DetectorFactory

AGENT_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMDQ3MDAyNS1mYjhjLTQyNDUtOWZkMS1iZGViOTNmNTYxMmYiLCJleHAiOjI1MzQwMjMwMDc5OSwidXNlcl9pZCI6IjliZGFkY2U0LTkyZmItNDA2Yi1iOThiLTgzNDgwZDAzMzFkZSJ9.o543YBKLtOGsV9xFvwCy6t2njx7siuMeCdyoWK0D8qU" # noqa: E501
session = GenAISession(jwt_token=AGENT_JWT)


@session.bind(
    name="detect_language",
    description="This agent detects language"
)
async def detect_language(
    agent_context: GenAIContext,
    test_arg: Annotated[
        str,
        "This is a test argument. Your agent can have as many parameters as you want. Feel free to rename or adjust it to your needs.",  # noqa: E501
    ],
):
    """This agent detects language"""
    return "Hello, World!"


async def main():
    print(f"Agent with token '{AGENT_JWT}' started")
    await session.process_events()

if __name__ == "__main__":
    asyncio.run(main())
