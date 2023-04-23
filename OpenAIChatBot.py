# import os
import openai


openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

while True :
    ques = input("Enter Your Question : ")

    if ques == "break":

        break
    else:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt= ques,            
            temperature=0.9,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )
        print(response["choices"][0]["text"])