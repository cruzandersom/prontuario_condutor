import requests


class GPT4Chat:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        self.endpoint = "https://api.openai.com/v1/chat/completions"

    def generate_response(self, prompt, max_tokens=150, n=1, temperature=0.7, top_p=1):
        data = {
            "prompt": prompt,
            "max_tokens": max_tokens,
            "n": n,
            "temperature": temperature,
            "top_p": top_p,
            "model": "gpt-3.5-turbo"
        }
        response = requests.post(self.endpoint, json=data, headers=self.headers)
        if response.status_code == 200:
            return response.json()["choices"][0]["text"].strip()
        else:
            raise ValueError(f"Error {response.status_code}: {response.text}")


# Exemplo de uso
if __name__ == "__main__":
    API_KEY = "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"
    gpt4_chat = GPT4Chat(API_KEY)
    prompt = "Qual é a capital da França?"
    response = gpt4_chat.generate_response(prompt)
    print(response)
