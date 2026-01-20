import os
import asyncio
from dotenv import load_dotenv
from droidrun import DroidAgent, load_llm, DroidrunConfig
from droidrun.config_manager import AgentConfig

# Load environment variables from .env file
load_dotenv()

# Classification rules from external file
with open("prompts/classification_rules.txt", "r") as f:
    CLASSIFICATION_RULES = f.read()

RECRUITER_GOAL = f"""
You are a recruiter's AI assistant for WhatsApp Business.

Open WhatsApp Business.
Read unread messages.
For each unread message:
- Classify the sender based on these rules:
{CLASSIFICATION_RULES}
- Star important conversations (urgent candidates, interview confirmations)
- Draft a professional reply message
- Add appropriate labels (New Candidate, Follow-up, Interview, Spam)

Do NOT send messages automatically.
Stop when all unread messages are processed.
"""

async def main():
    # Check if API Key is set
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("❌ ERROR: OPENAI_API_KEY not found!")
        print("Please set it in .env file or environment variable.")
        print("\nTo fix:")
        print("1. Create a .env file in this directory")
        print("2. Add: OPENAI_API_KEY=sk-your-key-here")
        print("3. Or run: $env:OPENAI_API_KEY=\"sk-your-key-here\"")
        return
    
    print("✅ OpenAI API Key found")
    
    # Configure LLM (gpt-4o-mini with low temperature for consistency)
    print("🔄 Loading LLM (GPT-4o-mini)...")
    llm = load_llm("OpenAI", model="gpt-4o-mini", temperature=0.2)
    print("✅ LLM loaded successfully")

    # Configure the Agent
    config = DroidrunConfig(
        agent=AgentConfig(
            max_steps=30,
            reasoning=True  # Manager/Executor loop for better planning
        )
    )

    print("🤖 Initializing Recruiter WhatsApp Triage Agent...")
    agent = DroidAgent(
        goal=RECRUITER_GOAL,
        llms=llm,
        config=config
    )
    print("✅ Agent initialized")

    print("\n" + "="*60)
    print("🚀 STARTING AGENT EXECUTION")
    print("="*60)
    print("📱 Watch your Android device screen for actions...")
    print("="*60 + "\n")
    
    handler = agent.run()
    
    # Stream events and show progress
    async for event in handler.stream_events():
        # Events will be logged automatically by the agent
        pass

    result = await handler
    
    print("\n" + "="*60)
    print("🏁 AGENT EXECUTION FINISHED")
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
