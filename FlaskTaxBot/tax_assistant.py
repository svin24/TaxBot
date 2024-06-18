from flask import Flask, jsonify, render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    income = request.form['income']
    expenses = request.form['expenses']
    prompt = request.form['prompt']

    # AI not integrated yet
    ai_response = "Not Integrated SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE"

    return jsonify({
        'income': income,
        'expenses': expenses,
        'prompt': prompt,
        'ai_response': ai_response
    })

if __name__ == '__main__':
    app.run(debug=True)
