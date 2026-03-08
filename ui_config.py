# ui_config.py
# UI 렌더링에 필요한 각종 텍스트 및 리터럴을 국가별로 관리합니다.

UI_LITERALS = {
    "ko": {
        "page_title": "KHU AI Assistant",
        
        # Sidebar
        "sidebar_brand": "KHU AI Lab",
        "btn_new_chat": "새로운 대화",
        "history_title": "최근 대화",
        "history_items": [
            "UI 프레임워크 테스트",
            "Qwen 모델 실험 #1",
            "프롬프트 엔지니어링"
        ],
        "llm_select_label": "현재 LLM 엔진",
        "llm_options": {
            "qwen": "Qwen-2.5-VL (Local)",
            "gemini": "Google Gemini 2.0",
            "openai": "OpenAI GPT-4o"
        },
        
        # User Profile
        "user_name": "김태경 교수님",
        "user_role": "연구 디렉터",
        
        # Main Chat Area
        "chat_header_title": "UI 프레임워크 테스트",
        "welcome_message": "안녕하세요, 교수님! 윤이나 조교입니다. 😉<br>여러 실험에 편하게 사용하실 수 있도록 경희대 시그니처 컬러를 적용한 **AI 챗봇 UI 프레임워크 1차 초안**을 띄웠습니다!<br>좌측 하단에서 향후 연동할 LLM(Qwen, Gemini 등)을 선택하는 파라미터 콤보박스도 준비해 두었습니다. 편하게 테스트해보세요!",
        
        # Chat Input
        "input_placeholder": "메시지를 입력하세요 (Shift + Enter로 줄바꿈)",
        "input_footer_warning": "AI는 실수할 수 있습니다. 중요한 정보는 항상 교차 검증을 권장합니다.",
        
        # Right Panels (Top) - Survey
        "survey_title": "설문조사",
        "survey_desc": "실험 사전/사후 설문지나 사용자 입력 폼을 배치하는 영역입니다.",
        "survey_form_label": "참여 전 기대치 평가",
        "btn_submit": "제출하기",
        
        # Right Panels (Bottom) - Additional Questions
        "extra_panel_title": "추가 질문 / 실험 컨트롤",
        "extra_panel_desc": "실험 중 부가적인 질문, PDF 문헌 정보, 기타 메타데이터를 표시하는 용도로 사용됩니다.",
        "extra_files": [
            "관련 논문 자료 1.pdf",
            "실험 가이드라인.pdf"
        ]
    },
    "en": {
        "page_title": "KHU AI Assistant",
        
        # Sidebar
        "sidebar_brand": "KHU AI Lab",
        "btn_new_chat": "New Chat",
        "history_title": "Recent Chats",
        "history_items": [
            "UI Framework Test",
            "Qwen Model Experiment #1",
            "Prompt Engineering"
        ],
        "llm_select_label": "Current LLM Engine",
        "llm_options": {
            "qwen": "Qwen-2.5-VL (Local)",
            "gemini": "Google Gemini 2.0",
            "openai": "OpenAI GPT-4o"
        },
        
        # User Profile
        "user_name": "Prof. Kim Taekyung",
        "user_role": "Research Director",
        
        # Main Chat Area
        "chat_header_title": "UI Framework Test",
        "welcome_message": "Hello, Professor! I am your TA, Yoon Ina. 😉<br>I've deployed the **1st Draft of the AI Chatbot UI Framework**, styled with KHU signature colors for your various experiments!<br>At the bottom left, there's a parameter combo box to select the LLM (Qwen, Gemini, etc.) to be integrated later. Feel free to test it out!",
        
        # Chat Input
        "input_placeholder": "Type a message (Shift + Enter for new line)",
        "input_footer_warning": "AI can make mistakes. Cross-verification of important information is always recommended.",
        
        # Right Panels (Top) - Survey
        "survey_title": "Survey",
        "survey_desc": "This area is for placing pre/post-experiment questionnaires or user input forms.",
        "survey_form_label": "Pre-participation Expectation Rating",
        "btn_submit": "Submit",
        
        # Right Panels (Bottom) - Additional Questions
        "extra_panel_title": "Additional Questions / Experiment Control",
        "extra_panel_desc": "Used for displaying additional questions, PDF literature info, and other metadata during the experiment.",
        "extra_files": [
            "Related Literature 1.pdf",
            "Experiment Guidelines.pdf"
        ]
    },
    "zh": {
        "page_title": "KHU AI 助手",
        
        # Sidebar
        "sidebar_brand": "KHU AI 实验室",
        "btn_new_chat": "新对话",
        "history_title": "最近对话",
        "history_items": [
            "UI 框架测试",
            "Qwen 模型实验 #1",
            "提示词工程"
        ],
        "llm_select_label": "当前 LLM 引擎",
        "llm_options": {
            "qwen": "Qwen-2.5-VL (Local)",
            "gemini": "Google Gemini 2.0",
            "openai": "OpenAI GPT-4o"
        },
        
        # User Profile
        "user_name": "金泰炅 教授",
        "user_role": "研究总监",
        
        # Main Chat Area
        "chat_header_title": "UI 框架测试",
        "welcome_message": "您好，教授！我是助教尹伊娜。😉<br>我已经部署了带有庆熙大学标志颜色的 **AI 聊天机器人 UI 框架初稿**，供您进行各种实验！<br>在左下方，有一个参数组合框可选择稍后要集成的 LLM (Qwen, Gemini等)。请随时测试！",
        
        # Chat Input
        "input_placeholder": "输入消息 (Shift + Enter 换行)",
        "input_footer_warning": "AI 可能会犯错。建议务必交叉验证重要信息。",
        
        # Right Panels (Top) - Survey
        "survey_title": "问卷调查",
        "survey_desc": "此区域用于放置实验前/后问卷或用户输入表单。",
        "survey_form_label": "参与前预期评分",
        "btn_submit": "提交",
        
        # Right Panels (Bottom) - Additional Questions
        "extra_panel_title": "附加问题 / 实验控制",
        "extra_panel_desc": "用于在实验期间显示附加问题、PDF 文献信息和其他元数据。",
        "extra_files": [
            "相关文献资料 1.pdf",
            "实验指南.pdf"
        ]
    }
}
