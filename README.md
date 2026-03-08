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

---

## 📝 Version History (Changelog)

### v0.0.3 (Continuous Update)
- **UI/UX**: Redesigned the main chat panel to look like a standalone mobile app with phone mockup styling (rounded corners, shadow, and notch).
- **Feature**: Added dynamic font size controls (A-, A, A+) which correctly scales both message bubbles and the chat input area. The controls were relocated to a neat settings modal activated via the sidebar user profile.
- **Maintenance**: Renamed default template literals from "UI Framework Test" to "AI Chat" across languages for a sleeker identity.
- **Bug Fix**: Implemented cache-busting queries (`?v=...`) on static assets to prevent browser caching issues during updates.
- **Enhancement**: Changed the overall satisfaction survey question (Likert scale) from 5-point to 7-point scale in `index.html`.

### v0.0.2
- **Feature**: Added comprehensive Google Forms-style survey UI components to the bottom-right panel.
- **UI/UX**: Implemented independent vertical scrolling for the survey panel.

### v0.0.1
- **Initial Release**: Basic 2-column layout AI Chat UI framework with multi-language (ko, en, zh) support.
