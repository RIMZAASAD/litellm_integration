import os
from litellm import completion
from dotenv import load_dotenv

load_dotenv()

def main():
    api_key = os.getenv("GEMINI_API_KEY")
    response = completion(
        model="gemini/gemini-2.0-flash",  # spelling "gimini" bhi galat ho sakta hai
        messages=[
            {
                "role": "user",
                "content":"ans me all exercise posture and all exercise name with description"
            }
        ],
        
      # required if using OpenRouter
    )
    print(response.choices[0].message["content"])

main()
