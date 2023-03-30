import openai
openai.api_key = "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"
question = None

while(question != "end"):

    print("\n")
    question = input("Ask: ")

    if question != "end":

        res = openai.Completion.create(
            engine='text-davinci-002',
            prompt = question,
            temperature = 0.4,
            max_tokens = 2048,
        )

        response = res.choices[0]['text']

        print(f"{response}\n")