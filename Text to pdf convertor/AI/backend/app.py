import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import openai

openai.api_key = 'your_openai_api_key'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['UPLOAD_FOLDER'] = 'static/images'

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Debug: Log incoming request
    print("Form data received:", request.form)
    print("Files received:", request.files)

    # Handle uploaded images
    images = request.files.getlist('images')
    for image in images:
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(f"Saved image: {filename}")  # Debug: Log saved images

    # Get user input
    prompt = request.form['prompt']
    colors = request.form.get('colors', '')

    # Debug: Log user input
    print(f"Prompt: {prompt}, Colors: {colors}")

    # Call OpenAI API
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Generate an HTML landing page for: {prompt} with colors: {colors}",
            max_tokens=500
        )
        generated_code = response['choices'][0]['text']
        print("Generated HTML:", generated_code)  # Debug: Log AI response
    except Exception as e:
        print("Error calling OpenAI API:", e)
        return jsonify({'error': 'Failed to generate HTML. Check server logs.'}), 500

    return jsonify({'html': generated_code})

if __name__ == '__main__':
    app.run(debug=True)