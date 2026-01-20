import os
import asyncio
from dotenv import load_dotenv
from droidrun import DroidAgent, load_llm, DroidrunConfig
from droidrun.config_manager import AgentConfig

# Load environment variables from .env file
load_dotenv()

# Simple test goal
TEST_GOAL = """
Open the Settings app.
Navigate to About Phone.
Read the Android version.
Report what you found.
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
            max_steps=15,  # Reduced for quick test
            reasoning=True
        )
    )

    print("🤖 Initializing Test Agent...")
    agent = DroidAgent(
        goal=TEST_GOAL,
        llms=llm,
        config=config
    )
    print("✅ Agent initialized")

    print("\n" + "="*60)
    print("🚀 STARTING TEST AGENT")
    print("="*60)
    print("📱 Watch BlueStacks for actions...")
    print("="*60 + "\n")
    
    handler = agent.run()
    
    async for event in handler.stream_events():
        pass

    result = await handler
    
    print("\n" + "="*60)
    print("🏁 TEST FINISHED")
    print("="*60)
    print(f"✅ Success: {result.success}")
    print(f"📝 Reason: {result.reason}")
    print("="*60)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n⚠️ Agent stopped by user (Ctrl+C)")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        import traceback
        traceback.print_exc()
