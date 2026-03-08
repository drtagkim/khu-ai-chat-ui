# KHU AI Chat UI Framework

> 🎓 **Designed & Developed by:** Prof. Taekyung Kim & Research Assistant Yoon Ina (Department of Big Data Analytics, School of Management, Kyung Hee University)

This project is a customized UI framework for Large Language Model (LLM) chatbot experiments. It provides a clean, premium design using Kyung Hee University's signature colors (Burgundy/White).

## 🚀 Key Features
1. **2-Column, 2-Row Split Layout**
   - **Main Panel (Left, 60%)**: Chat area with the AI assistant.
   - **Split Panel (Right, 40%)**:
     - **Top Row**: Additional questions, experiment controls, and metadata (e.g., related literature PDFs).
     - **Bottom Row**: Pre/post-experiment surveys and user input forms.
2. **LLM Scalability & Integration**
   - The UI logic is highly decoupled and pluggable, making it easy to integrate with various LLMs such as Qwen, Gemini, and OpenAI.
3. **Built-in Multi-language (i18n) Support**
   - UI literals are managed via `ui_config.py` in Korean (`ko`), English (`en`), and Chinese (`zh`). A language selector allows instant UI switching.
4. **Lightweight & Fast Stack (Vanilla JS/CSS, FastAPI)**
   - Built with pure HTML/JS/CSS and a FastAPI backend. Easy to customize with basic Python knowledge, without heavy frontend frameworks.

## 🛠 Installation & Quick Start

1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

2. **Run Backend Server**
```bash
python main.py
```

3. **Access via Browser**
Open `http://localhost:8000` to interact with the UI.

## 📂 Project Structure
- `main.py`: FastAPI backend entry point
- `templates/index.html`: Main HTML template layout
- `static/style.css`: Stylesheet for theming and split-layout rendering
- `static/app.js`: Client-side script handling typing effects and bot communication
- `ui_config.py`: Dictionary containing multi-language UI literals
