import os
import asyncio
from dotenv import load_dotenv
from droidrun import DroidAgent, load_llm, DroidrunConfig
from droidrun.config_manager import AgentConfig, DeviceConfig

load_dotenv()

# Simple test goal
TEST_GOAL = """
Open the Settings app.
Navigate to About Phone or About Device.
Read the Android version.
Report what you found.
"""

async def main():
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("❌ ERROR: GOOGLE_API_KEY not found!")
        return
    
    print("✅ Google Gemini API Key found")
    print("🔄 Loading LLM...")
    
    llm = load_llm("GoogleGenAI", model="gemini-2.0-flash-exp", api_key=api_key, temperature=0.2)
    print("✅ LLM loaded")

    # Configure with device settings
    config = DroidrunConfig(
        agent=AgentConfig(
            max_steps=10,
            reasoning=False  # Use direct mode for simpler execution
        ),
        device=DeviceConfig(
            platform="android"
        )
    )

    print("🤖 Initializing Test Agent...")
    agent = DroidAgent(
        goal=TEST_GOAL,
        llms=llm,
        config=config
    )
    print("✅ Agent initialized\n")

    print("="*60)
    print("🚀 STARTING TEST")
    print("="*60)
    print("📱 Watch the emulator...")
    print("="*60 + "\n")
    
    handler = agent.run()
    result = await handler
    
    print("\n" + "="*60)
    print("🏁 TEST COMPLETE")
    print("="*60)
    print(f"✅ Success: {result.success}")
    print(f"📝 Result: {result.reason}")
    print("="*60)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n⚠️ Stopped by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
