import os
import google.generativeai as genai

    
def answer(ask):
    api_key = os.getenv("MAKERSUITE_API_TOKEN")
    genai.configure(api_key=api_key)
    
   
   
    generation_config = {
  "temperature": 0.1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 1024,
}

    safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]
   
    


    model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                                  
                              generation_config=generation_config,
                              safety_settings=safety_settings)

    prompt_parts = [
  "input: credit card types",
"output: 3 types i.e. FirstMilesCard, PrestigeCard, and CashBackCard",
"input: credit card for miles",
"output: FirstMilesCard offer 5 miles per dollar spend. Standard Exclusion apply. 3 years expiry for accumulated miles. ",
"input: credit card for luxury and fine dining experience",
"output: PrestigeCard offer 1 for 1 in major hotel like Fairmont Market Café, Marriott Wan He Chinese Restaurant. There is also special S$100 dining credit during card member birthday month ",
"input: credit card for cash back reward",
"output: CashBackCard provide 1.5% cashback for all transaction with no minimum spend. Standard Exclusion apply.",
"input: exclusion transaction for miles accumulation or cash back reward",
"output: Bank finance charges are excluded from miles accumulation or cash back reward.",
  
  "input: " + ask,
  "output: ",
]
    
    response = model.generate_content(prompt_parts)

    return response.text.replace("\n", "</br>")

    
