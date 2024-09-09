import ollama
import requests

# Create a new instance of the OLLAMA class

class local_llm_interface:

    model = 'llama3.1'
    options = {
        'num_predict':-1,
        'num_ctx':4096,
        'temperature':0.2,
        'top_k':40,
        'top_p':0.9
    }

    endpoint = '127.0.0.1:11434'

    def __init__(self):
        pass

    def stream_single_questions(self, question):
        stream = ollama.generate(self.model, 
                               prompt=question, 
                               options=self.options, 
                               stream=True)
        for chunk in stream:
            yield chunk['response']
    
    def shoot_single_questions(self, question):
        return ollama.generate(self.model, 
                               prompt=question, 
                               options=self.options)['response']
    
    def stream_chat(self, question):
        stream = ollama.chat(self.model, 
                           messages=question,
                           options=self.options,
                           stream=True)
        for chunk in stream:
            yield chunk['message']['content']
    
