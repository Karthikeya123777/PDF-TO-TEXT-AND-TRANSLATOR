# AI Landing Page Generator

## Overview
The AI Landing Page Generator is a web application designed to help eCommerce businesses create visually appealing landing pages using artificial intelligence. The tool leverages AI models to generate HTML and CSS layouts based on user inputs, such as product images and design prompts.

## Features
- Upload product images for use in landing pages.
- Enter design prompts to guide the AI in generating layouts.
- Select brand colors and fonts to customize the landing page.
- Preview generated landing pages before finalizing.

## Tech Stack
- **Frontend:** HTML, CSS (Bootstrap), JavaScript
- **Backend:** Python (Flask)
- **AI Integration:** Custom AI models for generating design layouts

## Project Structure
```
ai-landing-page-generator
├── backend
│   ├── app.py                # Main entry point for the Flask application
│   ├── models
│   │   └── ai_model.py       # AI model logic for generating layouts
│   ├── routes
│   │   └── api.py            # API endpoints for handling requests
│   ├── static
│   │   ├── css
│   │   │   └── styles.css     # CSS styles for the frontend
│   │   ├── js
│   │   │   └── scripts.js      # JavaScript for user interactions
│   │   └── images             # Directory for storing uploaded images
│   └── templates
│       └── index.html        # Main HTML template for the frontend
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd ai-landing-page-generator
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```
   python backend/app.py
   ```

4. Open your web browser and navigate to `http://127.0.0.1:5000` to access the application.

## Usage Guidelines
- Use the upload feature to add product images.
- Fill in the design prompt to guide the AI in generating the landing page.
- Customize the design by selecting your brand colors and fonts.
- Preview the generated landing page and make adjustments as needed.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.