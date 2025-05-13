from flask import Flask, request

app = Flask(__name__)

def chatbot_logic(user_input):
    user_input = user_input.lower()

    if "revenue" in user_input and "microsoft" in user_input and "2022" in user_input:
        return "Microsoft's 2022 revenue was $198,270 billion."
    elif "revenue" in user_input and "microsoft" in user_input and "2023" in user_input:
        return "Microsoft's 2023 revenue was $211,915 billion."
    elif "revenue" in user_input and "microsoft" in user_input and "2024" in user_input:
        return "Microsoft's 2024 revenue was $245,122 billion."
    elif "revenue" in user_input and "apple" in user_input and "2022" in user_input:
        return "Apple's 2022 revenue was $394,328 billion."
    elif "revenue" in user_input and "apple" in user_input and "2023" in user_input:
        return "Apple's 2023 revenue was $383,285 billion."
    elif "revenue" in user_input and "apple" in user_input and "2024" in user_input:
        return "Apple's 2024 revenue was $391,035 billion."
    elif "revenue" in user_input and "tesla" in user_input and "2022" in user_input:
        return "Tesla's 2022 revenue was $81,462 billion."
    elif "revenue" in user_input and "tesla" in user_input and "2023" in user_input:
        return "Tesla's 2023 revenue was $96,773 billion."
    elif "revenue" in user_input and "tesla" in user_input and "2024" in user_input:
        return "Tesla's 2024 revenue was $97,960 billion."
    elif "net income" in user_input and "microsoft" in user_input and "2022" in user_input:
        return "Microsoft's 2022 net income was $72,738 billion."
    elif "net income" in user_input and "microsoft" in user_input and "2023" in user_input:
        return "Microsoft's 2023 net income was $72,361 billion."
    elif "net income" in user_input and "microsoft" in user_input and "2024" in user_input:
        return "Microsoft's 2024 net income was $88,136 billion."
    elif "net income" in user_input and "apple" in user_input and "2022" in user_input:
        return "Apple's 2022 net income was $394,328 billion."
    elif "net income" in user_input and "apple" in user_input and "2023" in user_input:
        return "Apple's 2023 net income was $383,285 billion."
    elif "net income" in user_input and "apple" in user_input and "2024" in user_input:
        return "Apple's 2024 net income was $391,035 billion."
    elif "net income" in user_input and "tesla" in user_input and "2022" in user_input:
        return "Tesla's 2022 net income was $12,587 billion."
    elif "net income" in user_input and "tesla" in user_input and "2023" in user_input:
        return "Tesla's 2023 net income was $14,974 billion."
    elif "net income" in user_input and "tesla" in user_input and "2024" in user_input:
        return "Tesla's 2024 net income was $7,153 billion."
    else:
        return "Sorry, I don't understand the question. Make sure to specify the company, metric, and year correctly!"

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>Financial Chatbot</title>
        </head>
        <body>
            <h1>Ask a financial question:</h1>
            <form action="/chat">
                <input name="q" type="text">
                <input type="submit" value="Ask">
            </form>
        </body>
    </html>
    '''

@app.route('/chat')
def chat():
    query = request.args.get('q', '')
    response = chatbot_logic(query)
    return f"<p><strong>Your question:</strong> {query}</p><p><strong>Chatbot:</strong> {response}</p><a href='/'>Ask another</a>"

if __name__ == '__main__':
    app.run(debug=True)

