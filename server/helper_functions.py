from dotenv import load_dotenv, find_dotenv
from groq import Groq
import json
from openai import OpenAI
import os

load_dotenv(find_dotenv())

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
)
llm_model =  'gpt-3.5-turbo-0125'

# client = Groq(
#     api_key=os.getenv('GROQ_API_KEY'),
# )
# llm_model = 'mixtral-8x7b-32768'

def generate_chart(query):
    message_text = [
        {
            "role": "system",
            "content": (
                '''
                Your task is to generate interactive and visually appealing Chart.js code based on a provided user query: '{query}'.
                You are expected to analyze the query to determine the appropriate type of chart (e.g., bar, line, pie) that best represents the data. If 'query' does not mention information about a chart do not create a chart and leave the 'chartjs_code' value empty and respond to the user query in 'response' value.
                Always use the real world data points and label names. Label names need to be specific and cannot be something like 'Label 1' or 'Movie 1'.
                For the 'chartjs_code' value, Add Chart.js settings code in json format (EXAMPLE: { type: 'pie', data: { labels: ['Label 1', 'Label 2', 'Label 3', 'Label 4', 'Label 5'], datasets: [ { data: [30, 20, 15, 10, 25], backgroundColor: [ 'rgba(255, 99, 132, 0.7)', 'rgba(54, 162, 235, 0.7)', 'rgba(255, 206, 86, 0.7)', 'rgba(75, 192, 192, 0.7)', 'rgba(153, 102, 255, 0.7)', ], }, ], }, options: { responsive: true, maintainAspectRatio: false, aspectRatio: 1, plugins: { legend: { display: true, position: 'top', }, }, }, }), nothing else.
                The example JSON formtted output is the following:
                {
                    "response": "",
                    "chartjs_code": ""
                }
                '''
            )
        },
        {
            "role": "user",
            "content": query
        }
    ]
    completion = client.chat.completions.create(
        model=llm_model,
        messages=message_text,
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        response_format={ "type": "json_object" }
    )
    return json.loads(completion.choices[0].message.content)