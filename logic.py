#import google.generativeai as palm

import google.generativeai as genai

    
def answer(ask):

    genai.configure(api_key="AIzaSyDV1E5CltzYfoXoUFMgh8ziYxnFypEO9yc")
    
   
   
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
  "input: IT Support",
  "output: The number of IT support is 123455",
  "input: bank card",
  "output: call bank hotline 1234",
  "input: bank address",
  "output: Tampines",
  "input: bank in charge",
  "output: Mr He",
  "input: " + ask,
  "output: ",
]
    
    response = model.generate_content(prompt_parts)

    return response.text.replace("\n", "</br>")

    
