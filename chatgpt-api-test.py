import openai

openai.api_key = "YOUR OPENAI API-KEY HERE"

def is_bigger_than_phone(prompt):

    answer = openai.ChatCompletion.create(
        model= "gpt-3.5-turbo",
        messages = [
                {"role":"user", "content": "I will name something. You will respond 'True' it is physically larger than a cellphone, 'False' if it is physically smaller than a cellphone"},
                {"role": "assistant", "content": "Ok, I'm ready."},
                {"role": "user", "content": "a coin"},
                {"role": "assistant", "content": "False"},
                {"role": "user", "content": "a computer"},
                {"role": "assistant", "content": "True"},
                {"role": "user", "content": "a door"},
                {"role": "assistant", "content": "True"},
                {"role": "user", "content": "a clip"},
                {"role": "assistant", "content": "False"},
                {"role": "user", "content": prompt}
        ]
    )

    answer = completion.choices[0].message.content
    print(answer)

    is_bigger_than_phone("a bed")