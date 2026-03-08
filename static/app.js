document.addEventListener('DOMContentLoaded', () => {
    const chatInput = document.getElementById('chat-input');
    const sendBtn = document.getElementById('send-btn');
    const chatForm = document.getElementById('chat-form');
    const chatMessages = document.getElementById('chat-messages');
    const modelSelect = document.getElementById('model-select');

    // Auto-resize textarea
    chatInput.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
        
        // Enable/disable send button
        if (this.value.trim().length > 0) {
            sendBtn.removeAttribute('disabled');
        } else {
            sendBtn.setAttribute('disabled', 'true');
        }
    });

    // Handle Enter to send (Shift+Enter for newline)
    chatInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            if (this.value.trim().length > 0) {
                chatForm.dispatchEvent(new Event('submit'));
            }
        }
    });

    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const message = chatInput.value.trim();
        if (!message) return;

        const currentModel = modelSelect.value;
        
        // 1. Add User Message
        addUserMessage(message);
        
        // Reset Input
        chatInput.value = '';
        chatInput.style.height = 'auto';
        sendBtn.setAttribute('disabled', 'true');
        
        // 2. Add AI Loading Indicator
        const typingIndicator = addTypingIndicator();
        scrollToBottom();

        try {
            // 3. Send to API
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    message: message,
                    model: currentModel
                })
            });

            const data = await response.json();
            
            // 4. Remove typing indicator and show AI response
            typingIndicator.remove();
            addAiMessage(data.reply);
            
        } catch (error) {
            typingIndicator.remove();
            addAiMessage("❌ 시스템 오류가 발생했습니다. 백엔드 서버 연결을 확인해주세요.");
            console.error("Chat API Error:", error);
        }
        
        scrollToBottom();
    });

    function addUserMessage(text) {
        const msgDiv = document.createElement('div');
        msgDiv.className = 'message user-message';
        msgDiv.innerHTML = `
            <div class="message-content">
                ${escapeHtml(text).replace(/\n/g, '<br>')}
            </div>
        `;
        chatMessages.appendChild(msgDiv);
    }

    function addAiMessage(text) {
        const msgDiv = document.createElement('div');
        msgDiv.className = 'message ai-message';
        // HTML 허용 (백엔드에서 마크다운 파싱해서 보낼 수도 있음)
        // 현재는 1차 초안이므로 단순 텍스트로 삽입
        msgDiv.innerHTML = `
            <div class="message-avatar"><i class="fa-solid fa-robot"></i></div>
            <div class="message-content">
                ${text.replace(/\n/g, '<br>')}
            </div>
        `;
        chatMessages.appendChild(msgDiv);
    }

    function addTypingIndicator() {
        const msgDiv = document.createElement('div');
        msgDiv.className = 'message ai-message typing-container';
        msgDiv.innerHTML = `
            <div class="message-avatar"><i class="fa-solid fa-robot"></i></div>
            <div class="message-content">
                <div class="typing-indicator">
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                </div>
            </div>
        `;
        chatMessages.appendChild(msgDiv);
        return msgDiv;
    }

    function scrollToBottom() {
        chatMessages.scrollTo({
            top: chatMessages.scrollHeight,
            behavior: 'smooth'
        });
    }

    function escapeHtml(unsafe) {
        return unsafe
             .replace(/&/g, "&amp;")
             .replace(/</g, "&lt;")
             .replace(/>/g, "&gt;")
             .replace(/"/g, "&quot;")
             .replace(/'/g, "&#039;");
    }
});
