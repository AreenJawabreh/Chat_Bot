# 🤖 ChatGPT-like App with Streamlit (No LLM)

A simple ChatGPT-style chatbot built using Python and Streamlit without using any external APIs or Large Language Models (LLMs).

The app demonstrates:
- Streamlit chat UI
- Local response generation
- Session state management
- Simple chatbot interaction

---

# 📌 Features

- Chat-style interface using `st.chat_message`
- User input with `st.chat_input`
- Conversation history stored using `st.session_state`
- Locally simulated assistant replies
- No internet connection required
- No external AI or API usage

---

# 🛠 Technologies Used

- Python
- Streamlit

---

# 📂 Project Structure

```bash
project_folder/
│
├── chat_app.py
├── requirements.txt
└── README.md
```

---

# 🚀 Installation & Setup

## 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

## 2. Navigate to the Project Folder

```bash
cd project_folder
```

## 3. Create Virtual Environment (Optional)

### Windows

```bash
python -m venv env
env\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv env
source env/bin/activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
streamlit run chat_app.py
```

The app will open automatically in your browser.

---

# 🧠 How It Works

The chatbot does not use AI or external APIs.

Instead, responses are generated locally using a simple Python function with:
- `if/elif` conditions
- predefined responses
- random reply selection

Conversation history is stored inside:

```python
st.session_state.messages
```

This allows the chat to behave like a real messaging application.

---

# 💬 Example Interactions

| User Message | Assistant Reply |
|---|---|
| Hello | Hi there! 👋 |
| How are you? | I'm just a local Python function, but I'm doing great! |
| Bye | Goodbye! Have a nice day. |

---

# 🎥 Demo Video

A short demo video explains:
- How the application runs
- How users interact with the chatbot
- How local responses are generated
- Streamlit chat components used in the project

---

# 📸 Streamlit Components Used

- `st.chat_message()`
- `st.chat_input()`
- `st.session_state`

---

# ✅ Requirements

```txt
streamlit
```

---

# 👩‍💻 Author

Your Name Here