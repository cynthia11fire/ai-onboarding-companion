const initialTasks = [
  { id: "personal", title: "Complete personal information", note: "Completed · 9:05 AM", done: true },
  { id: "handbook", title: "Read employee handbook", note: "Completed · 9:20 AM", done: true },
  { id: "tax", title: "Submit tax forms", note: "Due today", done: false },
  { id: "device", title: "Set up work device", note: "In progress", done: false },
  { id: "slack", title: "Join Slack workspace", note: "Pending", done: false },
  { id: "manager", title: "Schedule 1:1 with manager", note: "Pending", done: false }
];

const initialSignals = [
  { id: "progress", title: "Onboarding progress behind schedule", note: "Tax forms and device setup still open", level: "high", resolved: false },
  { id: "team", title: "Limited team interaction detected", note: "No informal buddy interaction logged yet", level: "medium", resolved: false },
  { id: "manager", title: "Manager check-in not logged", note: "Suggested before end of Day 3", level: "medium", resolved: false },
  { id: "escalation", title: "No manager escalation", note: "No urgent escalation needed", level: "low", resolved: true }
];

let tasks = [];
let signals = [];
const state = { progress: 38, messages: [] };

const $ = (id) => document.getElementById(id);
const pageTitles = {
  home: "AI is guiding Safi through her Day 1 onboarding",
  guidance: "AI Guidance is turning onboarding into a clear workflow",
  hr: "HR can see who needs support before disengagement grows",
  journey: "Safi's 90-day journey tracks integration, not just tasks"
};

function cloneData() {
  tasks = initialTasks.map(item => ({ ...item }));
  signals = initialSignals.map(item => ({ ...item }));
}

function renderProgress() {
  $("scoreValue").textContent = `${state.progress}%`;
  $("scoreBar").style.width = `${state.progress}%`;\n  const orb = document.querySelector(".progress-orb");\n  if (orb) orb.style.setProperty("--progress", `${state.progress}%`);
  const remaining = tasks.filter(task => !task.done).length;
  $("scoreTrend").textContent = `${remaining} priorities remaining`;
}

function renderTasks() {
  const complete = tasks.filter(task => task.done).length;
  $("taskCount").textContent = `${complete} / ${tasks.length} completed`;
  $("taskBar").style.width = `${Math.round((complete / tasks.length) * 100)}%`;
  $("taskList").innerHTML = tasks.map(task => `
    <li class="${task.done ? "done" : ""}">
      <span class="check">${task.done ? "✓" : ""}</span>
      <div><p>${task.title}</p><span>${task.note}</span></div>
    </li>
  `).join("");
}

function renderSignals() {
  const open = signals.filter(signal => !signal.resolved).length;
  $("riskBadge").textContent = `${open} support signals`;
  $("riskList").innerHTML = signals.map(signal => `
    <li class="${signal.level} ${signal.resolved ? "resolved" : ""}">
      <span class="signal-icon">${signal.resolved ? "✓" : "!"}</span>
      <div><p>${signal.title}</p><span>${signal.note}</span></div>
    </li>
  `).join("");
}

function addMessage(role, html) {
  state.messages.push({ role, html });
  $("chatLog").innerHTML = state.messages.map(message => `
    <div class="msg ${message.role}">${message.html}</div>
  `).join("");
  $("chatLog").scrollTop = $("chatLog").scrollHeight;
}

function setProgress(value) {
  state.progress = Math.max(0, Math.min(100, value));
  renderProgress();
}

function markDone(id, note) {
  const task = tasks.find(item => item.id === id);
  if (task) {
    task.done = true;
    if (note) task.note = note;
  }
  renderTasks();
}

function resolveSignal(id, note) {
  const signal = signals.find(item => item.id === id);
  if (signal) {
    signal.resolved = true;
    if (note) signal.note = note;
  }
  renderSignals();
}

function intro() {
  addMessage("user", "Hi, I am Safi Tseng. It is my first day as a Human Resources Manager.");
  addMessage("agent", "<strong>Proactive morning check-in</strong>I already checked your Day 1 onboarding state. Today we will focus on three things: submit tax forms, set up your work device, and create one low-pressure team connection.");
}

function priorityGuide() {
  addMessage("agent", "<strong>Step 1 is ready</strong>We will start with tax forms because payroll cannot begin until this is submitted. Estimated time: 5 minutes. I will keep the next step hidden until this one is clear, so you do not have to manage the whole onboarding list at once.");
  $("nextActionTitle").textContent = "Submit tax forms first";
  $("nextActionText").textContent = "This keeps onboarding progress on track and lets the rest of the Day 1 journey continue without administrative friction.";
  const guidance = document.querySelector(".soft-guidance");
  if (guidance) guidance.scrollIntoView({ behavior: "smooth", block: "start" });
}

function completeDevice() {
  addMessage("user", "I finished setting up my work device.");
  markDone("device", "Completed · 10:10 AM");
  setProgress(52);
  addMessage("agent", "<strong>Meaning Skill</strong>You completed device setup before asking for more assignments. That means you are removing blockers early, which helps you join the team rhythm instead of waiting for access later.");
  resolveSignal("progress", "Device setup completed; tax forms remain open");
}

function connectionHelp() {
  addMessage("user", "I need help joining the right Slack channels. Who should I ask?");
  addMessage("agent", "<strong>Connection Skill</strong>Ask Maya Chen, your onboarding buddy. Copy-paste message: Hi Maya, I am setting up Slack for the People Team. Could you point me to the essential HR and team channels for my first week?");
  markDone("slack", "Buddy guidance requested");
  resolveSignal("team", "Buddy interaction suggested and logged");
  setProgress(Math.max(state.progress, 61));
}

function score() {
  addMessage("user", "How am I doing so far?");
  addMessage("agent", `<strong>Integration Health</strong>You are at ${state.progress}%. Your administrative blockers are shrinking. The next support action is not more paperwork; it is a short manager or buddy check-in so you do not have to guess the team rhythm alone.`);
}

function hitl() {
  $("hitlState").textContent = "Human review requested from Grace Lin before granting sensitive team context. This protects Safi and the company.";
  $("hitlState").classList.add("approved");
  addMessage("agent", "<strong>HITL Safety</strong>I requested human approval before sharing sensitive team context. In enterprise onboarding, AI can prepare the request, but people approve sensitive access.");
}

function reset() {
  cloneData();
  state.progress = 38;
  state.messages = [];
  $("nextActionTitle").textContent = "Submit tax forms first";
  $("nextActionText").textContent = "This keeps onboarding progress on track and prevents HR follow-up work later today.";
  $("hitlState").textContent = "Human review not requested";
  $("hitlState").classList.remove("approved");
  renderTasks();
  renderSignals();
  renderProgress();
  addMessage("agent", "<strong>Good morning, Safi.</strong>I prepared your Day 1 path so you do not have to guess what matters first.");
}

function runFlow() {
  reset();
  [intro, priorityGuide, completeDevice, connectionHelp, score].forEach((step, index) => {
    setTimeout(step, 650 * (index + 1));
  });
}

function switchScreen(screen) {
  document.querySelectorAll(".nav-list a").forEach(link => {
    link.classList.toggle("active", link.dataset.screen === screen);
  });
  document.querySelectorAll(".screen").forEach(section => {
    section.classList.toggle("active-screen", section.id === `screen-${screen}`);
  });
  $("pageTitle").textContent = pageTitles[screen] || pageTitles.home;
}

function bindEvents() {
  document.querySelectorAll(".nav-list a").forEach(link => {
    link.addEventListener("click", event => {
      event.preventDefault();
      switchScreen(link.dataset.screen);
    });
  });
  $("priorityBtn").addEventListener("click", priorityGuide);
  $("sendIntroBtn").addEventListener("click", intro);
  $("completeLaptopBtn").addEventListener("click", completeDevice);
  $("askConnectionBtn").addEventListener("click", connectionHelp);
  $("askScoreBtn").addEventListener("click", score);
  $("hitlBtn").addEventListener("click", hitl);
  $("resetBtn").addEventListener("click", reset);
  $("runFlowBtn").addEventListener("click", runFlow);
}

bindEvents();
reset();


