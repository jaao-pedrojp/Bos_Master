const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');
const themeToggle = document.getElementById('theme-toggle');
const themeIcon = document.getElementById('theme-icon');

// função para formatar a resposta do chatbot
function formatResponse(text) {
  const formattedText = text
    .replace(/(\*\*.*?\*\*)/g, '<strong>$1</strong>') // negrito
    .replace(/(\* )/g, '<li>') // listas
    .replace(/(\n)/g, '<br>'); // quebras de linha

  return formattedText;
}

// enviar mensagem do usuário
function sendMessage() {
  const userMessage = userInput.value.trim();
  if (userMessage) {
    appendMessage(userMessage, 'user');
    userInput.value = '';
    fetchChatbotReply(userMessage);
  }
}

function appendMessage(message, sender) {
  const messageDiv = document.createElement('div');
  messageDiv.classList.add('message', sender);

  // adicionar a mensagem formatada
  messageDiv.innerHTML = formatResponse(message);

  chatBox.appendChild(messageDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}

// buscar resposta do chatbot
function fetchChatbotReply(message) {
  fetch('/chat', {  // Alterado para URL relativa
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.reply) {
        appendMessage(data.reply, 'bot');
      }
    })
    .catch((error) => {
      console.error('Erro ao se comunicar com o backend:', error);
      appendMessage('Erro ao se comunicar com o servidor.', 'bot');
    });
}

// evento de clique no botão de enviar
sendButton.addEventListener('click', sendMessage);

// evento de pressionar a tecla Enter
userInput.addEventListener('keypress', (event) => {
  if (event.key === 'Enter') {
    sendMessage();
  }
});

// alternar tema claro/escuro
themeToggle.addEventListener('click', () => {
  const body = document.body;
  if (body.dataset.tema === 'claro') {
    body.dataset.tema = 'escuro';
    themeIcon.textContent = 'dark_mode';
  } else {
    body.dataset.tema = 'claro';
    themeIcon.textContent = 'light_mode';
  }
});
