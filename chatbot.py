import os
from dotenv import load_dotenv

load_dotenv()
import json
from groq import Groq

# Initialize Groq client with your API key
client = Groq(api_key=os.getenv('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'))

class RoadSafetyChatbot:
    """Road Safety Intervention Chatbot using FREE Groq AI"""
    
    def __init__(self, data_file='data/interventions.json'):
        # Load interventions database
        with open(data_file, 'r', encoding='utf-8') as f:
            self.interventions = json.load(f)
        
        print(f"✅ Loaded {len(self.interventions)} interventions")
    
    def search_interventions(self, query):
        """Search for relevant interventions"""
        query_lower = query.lower()
        results = []
        
        for intervention in self.interventions:
            score = 0
            text = f"{intervention.get('intervention', '')} {intervention.get('description', '')} {intervention.get('problem_type', '')}".lower()
            
            words = query_lower.split()
            for word in words:
                if len(word) > 3:
                    score += text.count(word)
            
            if score > 0:
                results.append((score, intervention))
        
        results.sort(reverse=True, key=lambda x: x[0])
        return [item[1] for item in results[:5]]
    
    def generate_response(self, query):
        """Generate AI response using FREE Groq"""
        
        # Search database
        relevant = self.search_interventions(query)
        
        if not relevant:
            return "I couldn't find specific interventions. Please provide more details."
        
        # Prepare context
        context = "Based on IRC standards, relevant interventions:\n\n"
        for i, intervention in enumerate(relevant, 1):
            context += f"{i}. {intervention['intervention']}\n"
            context += f"   Description: {intervention['description']}\n"
            context += f"   Source: {intervention['source']} - {intervention['clause']}\n"
            context += f"   Road Type: {intervention['road_type']}\n\n"
        
        # Create prompt
        prompt = f"""You are a road safety expert. A user described this issue:

"{query}"

{context}

Provide professional recommendations:
1. List top 3 most relevant interventions
2. Explain WHY each suits this problem
3. Include IRC source citation
4. Keep concise (200-250 words)

Format with clear numbering."""

        try:
            # Call FREE Groq API
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",  # FREE model!
                messages=[
                    {"role": "system", "content": "You are a road safety expert."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=500
            )
            
            return response.choices[0].message.content
        
        except Exception as e:
            return f"Error: {str(e)}\nPlease check your Groq API key."
    
    def chat(self):
        """Interactive chat"""
        print("\n" + "="*60)
        print("🚗 ROAD SAFETY INTERVENTION GPT CHATBOT")
        print("   (Powered by FREE Groq AI)")
        print("="*60)
        print("\nType your road safety issue and get recommendations!")
        print("Type 'exit' to quit\n")
        
        while True:
            query = input("You: ").strip()
            
            if query.lower() in ['exit', 'quit', 'bye']:
                print("\n👋 Thank you for using Road Safety GPT!")
                break
            
            if not query:
                continue
            
            print("\n🤖 AI: Analyzing... ")
            response = self.generate_response(query)
            print("\n" + response)
            print("\n" + "-"*60 + "\n")

if __name__ == "__main__":
    bot = RoadSafetyChatbot()
    bot.chat()