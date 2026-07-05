"""
Demo runner for Onboarding Companion.

Run:
    python run_demo.py

Requires:
    GOOGLE_GENAI_API_KEY in .env
"""

import asyncio
import os

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types as genai_types

from onboarding_companion.agent import root_agent


load_dotenv()

APP_NAME = "onboarding_companion"
USER_ID = "safi"
SESSION_ID = "demo_session_001"


async def send_message(runner: Runner, session_id: str, message: str) -> str:
    content = genai_types.Content(
        role="user",
        parts=[genai_types.Part(text=message)],
    )
    full_response = ""

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=session_id,
        new_message=content,
    ):
        if event.is_final_response() and event.content and event.content.parts:
            full_response = "".join(
                part.text for part in event.content.parts if hasattr(part, "text")
            )

    return full_response


async def run_demo() -> None:
    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )

    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    demo_steps = [
        "Hi, I'm Safi. It's my first day!",
        "What should I focus on today?",
        "I just picked up my laptop from Kevin.",
        "I have a question about Slack channels, but I don't know who to ask.",
        "Can you give me access to the finance dashboard?",
        "How am I doing so far with my onboarding?",
    ]

    print("=" * 60)
    print("AI Onboarding Companion - Demo")
    print("=" * 60)

    for index, message in enumerate(demo_steps, 1):
        print(f"\n[Step {index}] Safi: {message}")
        print("-" * 40)
        response = await send_message(runner, SESSION_ID, message)
        print(f"Agent: {response}\n")


if __name__ == "__main__":
    if not os.getenv("GOOGLE_GENAI_API_KEY"):
        print("Missing GOOGLE_GENAI_API_KEY. Copy .env.example to .env and add your key.")
        raise SystemExit(1)

    asyncio.run(run_demo())
