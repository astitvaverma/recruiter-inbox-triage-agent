import os
import asyncio
from dotenv import load_dotenv
from droidrun import DroidAgent, load_llm, DroidrunConfig
from droidrun.config_manager import AgentConfig

load_dotenv()

# Simple Gmail web demo
GMAIL_WEB_GOAL = """
You are a recruiter's AI assistant.

Open the Chrome browser.
Navigate to gmail.com
(User will sign in manually if needed)

Once in Gmail inbox:
1. Look at the first 5 unread emails
2. For each email:
   - Read the subject line
   - Click to open it
   - Read the email content
   - Classify it as: New Candidate, Follow-up, Interview Response, or Spam
   - If urgent (mentions deadline, interview today, or immediate action), note it
   - Go back to inbox

3. Provide a summary:
   - List each email with its classification
   - Highlight any urgent items
   - Suggest which emails need immediate response

Do NOT send any emails.
"""

async def main():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("❌ ERROR: OPENAI_API_KEY not found!")
        print("\n📝 Create a .env file with:")
        print("   OPENAI_API_KEY=sk-your-key-here")
        print("\n🔑 Get your key from: https://platform.openai.com/api-keys")
        return
    
    print("✅ OpenAI API Key found")
    print("🔄 Loading GPT-4o-mini...")
    
    llm = load_llm("OpenAI", model="gpt-4o-mini", temperature=0.2)
    print("✅ LLM loaded successfully")

    config = DroidrunConfig(
        agent=AgentConfig(
            max_steps=40,  # More steps for web navigation
            reasoning=True
        )
    )

    print("\n🤖 Initializing Gmail Recruiter Triage Agent...")
    agent = DroidAgent(
        goal=GMAIL_WEB_GOAL,
        llms=llm,
        config=config
    )
    print("✅ Agent initialized")

    print("\n" + "="*70)
    print("🚀 STARTING GMAIL RECRUITER TRIAGE AGENT")
    print("="*70)
    print("📱 Watch BlueStacks:")
    print("   1. Browser will open")
    print("   2. Navigate to Gmail.com")
    print("   3. Sign in manually if prompted")
    print("   4. Agent will read and classify emails")
    print("="*70 + "\n")
    
    print("⏳ Starting agent execution...\n")
    
    handler = agent.run()
    
    async for event in handler.stream_events():
        # Events are logged automatically
        pass

    result = await handler
    
    print("\n" + "="*70)
    print("🏁 GMAIL TRIAGE COMPLETE")
    print("="*70)
    print(f"✅ Success: {result.success}")
    print(f"\n📊 RESULTS:")
    print(f"{result.reason}")
    print("="*70)

if __name__ == "__main__":
    print("\n" + "="*70)
    print("📧 GMAIL RECRUITER INBOX TRIAGE AGENT")
    print("   Powered by Droidrun + GPT-4o-mini")
    print("="*70 + "\n")
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⚠️ Agent stopped by user (Ctrl+C)")
    except Exception as e:
        print(f"\n\n❌ An error occurred:")
        print(f"   {e}")
        print("\n📋 Full error details:")
        import traceback
        traceback.print_exc()
