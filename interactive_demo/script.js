const roles = document.querySelectorAll('.role');
const panels = document.querySelectorAll('.panel');
const navItems = document.querySelectorAll('.nav-item');
const toast = document.getElementById('toast');
let progress = 38;
let steps = 3;

function refreshIcons() {
  if (window.lucide) window.lucide.createIcons();
}

function showToast(message) {
  toast.textContent = message;
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 2200);
}

roles.forEach(role => {
  role.addEventListener('click', () => {
    roles.forEach(r => r.classList.remove('active'));
    role.classList.add('active');
    panels.forEach(panel => panel.classList.remove('active-panel'));
    document.getElementById(role.dataset.panel).classList.add('active-panel');
    refreshIcons();
  });
});

navItems.forEach(item => {
  item.addEventListener('click', () => {
    navItems.forEach(i => i.classList.remove('active'));
    item.classList.add('active');
    showToast(`${item.textContent.trim()} selected`);
  });
});

document.getElementById('startStep').addEventListener('click', () => {
  document.getElementById('chatInput').value = 'How do I submit my tax forms?';
  showToast('Ready to ask AI Companion.');
});

document.getElementById('completeTask').addEventListener('click', () => {
  progress = 50;
  steps = 4;
  document.querySelector('.progress-ring').style.background = `conic-gradient(#6732d9 ${progress}%, #e8ddff 0)`;
  document.getElementById('progressNumber').textContent = `${progress}%`;
  document.getElementById('managerProgress').textContent = `${progress}%`;
  document.getElementById('stepCount').textContent = `${steps} of 8`;
  document.getElementById('progressText').textContent = 'You completed a real first-day milestone.';
  addMessage("I finished today's tasks. Did I actually make progress?", 'user');
  addMessage('Yes. You submitted an important first-day task, which shows preparedness and helps your team move faster. This is more than a checklist item; it is your first step toward becoming part of the team.', 'ai');
  showToast('Progress updated to 50%.');
});

document.getElementById('messageBuddy').addEventListener('click', () => {
  addMessage("I don't know who I should ask.", 'user');
  addMessage("For general onboarding or team questions, Maya Chen is your best contact. You could send: Hi Maya, I'm Safi, a new hire. Could I ask you a few quick questions about how the team usually works?", 'ai');
});

document.getElementById('scheduleOneOnOne').addEventListener('click', () => showToast('Suggested 1:1 check-in created.'));

document.querySelectorAll('.quick-prompts button').forEach(button => button.addEventListener('click', () => handlePrompt(button.dataset.prompt)));

document.getElementById('chatForm').addEventListener('submit', event => {
  event.preventDefault();
  const input = document.getElementById('chatInput');
  const text = input.value.trim();
  if (!text) return;
  handlePrompt(text);
  input.value = '';
});

function handlePrompt(text) {
  addMessage(text, 'user');
  setTimeout(() => addMessage(getAIResponse(text), 'ai'), 350);
}

function addMessage(text, type) {
  const log = document.getElementById('chatLog');
  const bubble = document.createElement('div');
  bubble.className = `bubble ${type}`;
  bubble.textContent = text;
  log.appendChild(bubble);
  log.scrollTop = log.scrollHeight;
}

function getAIResponse(text) {
  const lower = text.toLowerCase();
  if (lower.includes('focus') || lower.includes('today')) return 'Today, focus on three things: submit your tax forms, set up your work device, and meet your buddy. These steps give you clarity, access, and a first human connection.';
  if (lower.includes('it') || lower.includes('kevin')) return "For IT setup, contact Kevin Wu on Slack at @kevin.wu. You can send: Hi Kevin, I'm Safi, a new hire. Could you help me coordinate laptop pickup and setup?";
  if (lower.includes('too many questions') || lower.includes('worried')) return 'It is normal to ask many questions on Day 1. Asking early prevents bigger blockers later. A good rule: ask when the answer affects your next action.';
  if (lower.includes('progress') || lower.includes('make progress')) return 'Yes. You completed meaningful setup work, clarified who can help you, and reduced uncertainty. That shows you are not just finishing tasks; you are building the foundation to contribute.';
  if (lower.includes('nda')) return 'An NDA is a Non-Disclosure Agreement. It helps protect confidential company information. If anything is unclear, Mina Lee from People Operations is the right person to ask.';
  return 'I can help you turn that into one clear next step. If it is about tools, ask IT. If it is about policies, ask HR. If it is about priorities, ask your manager.';
}

window.addEventListener('DOMContentLoaded', refreshIcons);
