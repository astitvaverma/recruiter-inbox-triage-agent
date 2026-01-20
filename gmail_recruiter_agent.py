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
You are a recruiter's AI assistant.

Open Gmail.
Find unread emails.
For each unread email:
- Classify it based on these rules:
{CLASSIFICATION_RULES}
- Apply the correct Gmail label (New Candidate, Follow-up, Interview Response, or Spam).
- Star emails that are urgent or time-sensitive.
- Draft a short professional reply if required.

Do NOT send emails automatically.
Stop when all unread emails are processed.
"""

async def main():
    print("✅ Using Ollama (Free, runs locally, no API key needed!)")
    
    # Configure LLM (Ollama - completely free and local!)
    print("🔄 Loading LLM (Llama 3.2 via Ollama)...")
    print("   Make sure Ollama is running in the background...")
    
    try:
        llm = load_llm(
            "Ollama", 
            model="llama3.2:3b",
            base_url="http://localhost:11434",
            temperature=0.2,
            request_timeout=120.0,
            context_window=4096,  # Reduce memory usage to fit in 8GB RAM
            additional_kwargs={
                "num_ctx": 4096,  # Context window size
                "num_gpu": 0,     # Use CPU only to save memory
            }
        )
        print("✅ LLM loaded successfully")
    except Exception as e:
        print(f"❌ ERROR: Could not connect to Ollama!")
        print(f"   Error: {e}")
        print("\nTo fix:")
        print("1. Download Ollama from: https://ollama.com/download")
        print("2. Install and run Ollama")
        print("3. Run: ollama pull llama3.2:3b")
        print("4. Make sure Ollama is running (check system tray)")
        return

    # Configure the Agent
    config = DroidrunConfig(
        agent=AgentConfig(
            max_steps=30,
            reasoning=True  # Manager/Executor loop for better planning
        )
    )

    print("🤖 Initializing Recruiter Inbox Triage Agent...")
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
