

def generate_js(query):
    message_text = [
        {
            "role": "system",
            "content": (
                "Your task is to generate interactive and visually appealing Chart.js code based on a provided dataset. "
                "The dataset will be given to you in the form of a dictionary containing three keys: 'query', which holds "
                "the user's original query; 'sql_cmd', which contains the SQL command used to retrieve the data; and 'result', "
                "which includes the SQL command's output data which you will use to create the chart.js code. You are expected to: \n"
                "Analyze the 'result' and 'query' to determine the appropriate type of chart (e.g., bar, line, pie) that best represents the data, if 'query' does not mention information about a chart do not create a chart and just respond no chart needed. \n"
                "ONLY RETURN Chart.js settings code in json format (EXAMPLE: { type: 'pie', data: { labels: ['Label 1', 'Label 2', 'Label 3', 'Label 4', 'Label 5'], datasets: [ { data: [30, 20, 15, 10, 25], backgroundColor: [ 'rgba(255, 99, 132, 0.7)', 'rgba(54, 162, 235, 0.7)', 'rgba(255, 206, 86, 0.7)', 'rgba(75, 192, 192, 0.7)', 'rgba(153, 102, 255, 0.7)', ], }, ], }, options: { responsive: true, maintainAspectRatio: false, aspectRatio: 1, plugins: { legend: { display: true, position: 'top', }, }, }, }), nothing else. YOU ARE TO ONLY RETURN CHART.JS CODE formatted correctly"
            )
        },
        {
            "role": "user",
            "content": query
        }
    ]
    completion = client.chat.completions.create(
        model="gpt35t",
        messages=message_text,
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    return completion.choices[0].message.content