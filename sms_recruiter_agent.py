import os
import asyncio
from dotenv import load_dotenv
from droidrun import DroidAgent, load_llm, DroidrunConfig
from droidrun.config_manager import AgentConfig

# Load environment variables
load_dotenv()

# Classification rules
with open("prompts/classification_rules.txt", "r") as f:
    CLASSIFICATION_RULES = f.read()

SMS_RECRUITER_GOAL = f"""
You are a recruiter's AI assistant for SMS/text messages.

Open the Messages app (SMS).
Read unread text messages.
For each unread message:
- Classify it based on these rules:
{CLASSIFICATION_RULES}
- Determine if it's from a candidate, client, or spam
- Star important messages (urgent candidates, interview confirmations)
- Draft a professional SMS reply

Do NOT send messages automatically.
Provide a summary of all messages processed.
"""

async def main():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("❌ ERROR: OPENAI_API_KEY not found!")
        print("Set it in .env file: OPENAI_API_KEY=sk-your-key")
        return
    
    print("✅ OpenAI API Key found")
    print("🔄 Loading LLM...")
    llm = load_llm("OpenAI", model="gpt-4o-mini", temperature=0.2)
    print("✅ LLM loaded")

    config = DroidrunConfig(
        agent=AgentConfig(
            max_steps=30,
            reasoning=True
        )
    )

    print("🤖 Initializing SMS Recruiter Triage Agent...")
    agent = DroidAgent(
        goal=SMS_RECRUITER_GOAL,
        llms=llm,
        config=config
    )
    print("✅ Agent initialized\n")

    print("="*60)
    print("🚀 STARTING SMS TRIAGE")
    print("="*60)
    print("📱 Watch BlueStacks - Messages app will open")
    print("="*60 + "\n")
    
    handler = agent.run()
    async for event in handler.stream_events():
        pass

    result = await handler
    
    print("\n" + "="*60)
    print("🏁 SMS TRIAGE COMPLETE")
    print("="*60)
    print(f"✅ Success: {result.success}")
    print(f"📝 Summary: {result.reason}")
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
