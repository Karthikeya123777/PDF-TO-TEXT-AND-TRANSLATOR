from flask import Blueprint, request, jsonify
from models.ai_model import generate_landing_page

api = Blueprint('api', __name__)

@api.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt')
    image = data.get('image')

    if not prompt or not image:
        return jsonify({'error': 'Prompt and image are required'}), 400

    try:
        layout = generate_landing_page(prompt, image)
        return jsonify({'layout': layout}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500