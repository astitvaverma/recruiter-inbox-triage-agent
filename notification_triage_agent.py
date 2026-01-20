import os
import asyncio
from dotenv import load_dotenv
from droidrun import DroidAgent, load_llm, DroidrunConfig
from droidrun.config_manager import AgentConfig

# Load environment variables from .env file
load_dotenv()

NOTIFICATION_TRIAGE_GOAL = """
You are an AI assistant that helps organize notifications.

Open the notification panel.
Read all notifications.
For each notification:
- Determine if it's work-related, personal, promotional, or spam
- Clear spam notifications
- Star or mark important work notifications
- Organize by priority

Provide a summary of:
- Total notifications processed
- How many were important
- How many were spam/cleared
- Any urgent items that need immediate attention
"""

async def main():
    # Check if API Key is set
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("❌ ERROR: OPENAI_API_KEY not found!")
        print("Please set it in .env file or environment variable.")
        return
    
    print("✅ OpenAI API Key found")
    print("🔄 Loading LLM (GPT-4o-mini)...")
    llm = load_llm("OpenAI", model="gpt-4o-mini", temperature=0.2)
    print("✅ LLM loaded successfully")

    config = DroidrunConfig(
        agent=AgentConfig(
            max_steps=25,
            reasoning=True
        )
    )

    print("🤖 Initializing Notification Triage Agent...")
    agent = DroidAgent(
        goal=NOTIFICATION_TRIAGE_GOAL,
        llms=llm,
        config=config
    )
    print("✅ Agent initialized")

    print("\n" + "="*60)
    print("🚀 STARTING NOTIFICATION TRIAGE")
    print("="*60)
    print("📱 Watch BlueStacks for actions...")
    print("="*60 + "\n")
    
    handler = agent.run()
    
    async for event in handler.stream_events():
        pass

    result = await handler
    
    print("\n" + "="*60)
    print("🏁 TRIAGE COMPLETE")
    print("="*60)
    print(f"✅ Success: {result.success}")
    print(f"📝 Result: {result.reason}")
    print("="*60)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n⚠️ Agent stopped by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
