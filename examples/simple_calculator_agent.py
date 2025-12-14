"""
Simple Calculator Agent Example
This demonstrates a basic agent with a single tool for calculations.

Requirements:
    pip install langchain openai langchain-openai python-dotenv

Usage:
    1. Set OPENAI_API_KEY in .env file
    2. Run: python examples/simple_calculator_agent.py
"""

import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain.llms import OpenAI
from langchain.tools import Tool

# Load environment variables
load_dotenv()

def calculate(expression: str) -> str:
    """
    Safely evaluate a mathematical expression.
    
    Args:
        expression: A mathematical expression as a string
        
    Returns:
        The result of the calculation or an error message
    """
    try:
        # Simple safety check - only allow numbers and basic operators
        allowed_chars = set('0123456789+-*/(). ')
        if not all(c in allowed_chars for c in expression):
            return "Error: Invalid characters in expression"
        
        result = eval(expression)
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    """Main function to run the calculator agent."""
    
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found in environment variables")
        print("Please set it in your .env file or export it:")
        print("  export OPENAI_API_KEY='your-key-here'")
        return
    
    print("🤖 Simple Calculator Agent")
    print("=" * 50)
    
    # Create calculator tool
    calc_tool = Tool(
        name="Calculator",
        func=calculate,
        description="Evaluates mathematical expressions. Input should be a valid expression like '2 + 2' or '10 * 5 / 2'"
    )
    
    # Initialize LLM (using older OpenAI class for compatibility)
    # For newer versions, use: from langchain_openai import ChatOpenAI
    llm = OpenAI(temperature=0)  # temperature=0 for deterministic results
    
    # Initialize agent
    agent = initialize_agent(
        tools=[calc_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True  # Set to False to hide reasoning process
    )
    
    # Example queries
    test_queries = [
        "What is 25 * 37?",
        "Calculate 100 divided by 4",
        "What's 15 plus 23 minus 8?",
        "Compute 2 to the power of 10"
    ]
    
    print("\n📝 Running example queries:\n")
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n{'='*50}")
        print(f"Example {i}: {query}")
        print('-'*50)
        try:
            response = agent.run(query)
            print(f"\n✅ Answer: {response}\n")
        except Exception as e:
            print(f"❌ Error: {str(e)}\n")
    
    # Interactive mode
    print("\n" + "="*50)
    print("💬 Interactive Mode")
    print("Type 'quit' or 'exit' to stop")
    print("="*50 + "\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Goodbye!")
                break
            
            if not user_input:
                continue
            
            print()
            response = agent.run(user_input)
            print(f"\n🤖 Agent: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}\n")

if __name__ == "__main__":
    main()


