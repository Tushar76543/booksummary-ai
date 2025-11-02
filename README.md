# 📚 BookSummary-AI  
> *“Turning long reads into smart summaries — powered by AI & automation.”*  


---

### 🧠 Overview  
**BookSummary-AI** is an intelligent automation project that uses **Google Gemini**, **Flask**, and **n8n** to automatically **summarize books chapter-by-chapter**.  

From uploading your book to storing the final summaries in **Google Drive**, everything is handled seamlessly — no manual effort required.  

---

## 🧩 Tech Stack  
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)  
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey?logo=flask)  
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-AI%20Model-orange?logo=google)  
![n8n](https://img.shields.io/badge/n8n-Automation%20Tool-green?logo=n8n)  
![Google Drive API](https://img.shields.io/badge/Google%20Drive-API-yellow?logo=googledrive)  
![GitHub](https://img.shields.io/badge/GitHub-Version%20Control-black?logo=github)  

---

## ⚙️ Features  
✅ Upload your book from the Flask web interface  
✅ Automatically split and summarize chapters using **Google Gemini**  
✅ Save summaries back to **Google Drive**  
✅ Automated with **n8n workflows**  
✅ Secure environment management with **dotenv**  

---

## 📁 Project Structure  
```
booksummary-ai/
├── app.py                     # Flask backend
├── templates/                 # HTML templates
├── static/                    # CSS, JS, Images
├── .env.example               # Example env variables
├── n8n_workflows/
│   └── My workflow 3.json     # n8n workflow JSON
├── requirements.txt           # Dependencies
└── README.md
```

---

## 🚀 Setup Instructions  

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Tushar76543/booksummary-ai.git
cd booksummary-ai
```

### 2️⃣ Set Up Environment
```bash
python -m venv venv
venv\Scripts\activate   # (on Windows)
pip install -r requirements.txt
```

Create a `.env` file and add:
```
GEMINI_API_KEY=your_gemini_api_key
GOOGLE_CREDENTIALS_PATH=credentials.json
```

### 3️⃣ Run Flask App
```bash
python app.py
```
Then open 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🔄 n8n Workflow
📄 File: `n8n_workflows/My workflow 3.json`

This workflow automates the entire process:
1. Fetch book files from **Google Drive**  
2. Pass them through **Google Gemini API** for summarization  
3. Upload summarized output back to Drive  

To use it:
- Open your **n8n dashboard**
- Click **Import Workflow**
- Upload the `.json` file  
- Add your credentials and run it 🚀  

---

## 💡 Key Learnings  
- Integrating **Gemini AI** into real-world workflows  
- Using **n8n** for multi-step automation  
- Handling **OAuth credentials** securely  
- Flask + Google APIs = powerful automation combo  

---

## 🌟 Demo (Optional)
If you’d like, you can add a small screen-recording GIF or image here later —  
`/static/demo.gif`  
👉 Shows how the file upload and summary generation works in action.  

---

## 🔗 Project Links  
📘 **GitHub Repository:** [BookSummary-AI](https://github.com/Tushar76543/booksummary-ai)  
💬 **Connect on LinkedIn:** [Tushar (https://www.linkedin.com/in/tushar-ranjan-sahoo-3b642a2b6/)](#)  

---

## 🧑‍💻 Author  
**Tushar**  
> AI & Automation Enthusiast | Exploring Gemini + n8n + Flask  

