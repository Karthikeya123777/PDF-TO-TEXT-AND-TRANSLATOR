from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
import openai

openai.api_key = 'your_openai_api_key'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['UPLOAD_FOLDER'] = 'static/images'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Handle uploaded images
    images = request.files.getlist('images')
    for image in images:
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    # Get user input
    prompt = request.form['prompt']
    colors = request.form.get('colors', '')

    # Call OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate an HTML landing page for: {prompt} with colors: {colors}",
        max_tokens=500
    )
    generated_code = response['choices'][0]['text']

    return jsonify({'html': generated_code})

if __name__ == '__main__':
    app.run(debug=True)