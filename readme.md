# Portfolio Resume Website 🎯

A personal portfolio and resume website built using **Django**, designed to showcase projects, skills, resume, and enable contact through a form with email integration.

---

## 📌 Features

- Responsive home, about, projects, and contact pages
- Contact form that sends an acknowledgment email to the user
- Resume download option
- Organized static and media file management
- Modular Django app structure ready for deployment (Azure/Heroku)

---

## 🚀 Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML5, CSS3, Bootstrap
- **Database**: SQLite (default Django DB)
- **Email**: SMTP (Gmail setup)
- **Version Control**: Git, GitHub

---

## 🗂️ Project Structure

Portfolio_Resume_Website/
│
├── manage.py
├── requirements.txt
├── Procfile (for deployment)
├── db.sqlite3
│
├── Portfolio_Resume_Website/ # Django project config (settings, urls, wsgi)
├── ResumeWebsite/ # Main Django app (views, models, forms, etc.)
├── static/ # Custom static files (CSS, JS, images)
├── staticfiles/ # Collected static files (post collectstatic)
├── templates/ # All HTML templates


---

## 💡 Getting Started Locally

### 1. Clone the repository
```bash
git clone https://github.com/your-username/Portfolio_Resume_Website.git
cd Portfolio_Resume_Website

### 2. Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt

### 4. Run migrations
bash
Copy
Edit
python manage.py migrate

### 5. Run the development server
bash
Copy
Edit
python manage.py runserver
Then open http://127.0.0.1:8000/ in your browser.

---

### Author
Rudraksh Sachdeva
👨‍💻 B.Tech CSE Student @ IILM
📍 Delhi, India
🔗 https://github.com/Rudrakshsachdev
📧 rudraksh.sachdeva.19work@gmail.com