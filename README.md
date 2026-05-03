# Rishi-Notes: Simple Personal Knowledge Base

## Project Overview
This is a Full-Stack Product Management application built for the 1st Semester Capstone Project at Rishihood University. The app allows users to create, view, and manage digital notes through a clean, responsive interface.

**Contributors:** Aaryan Singh & Tushar Das

---

## Project Plan & Workflow
As per the project non-negotiables, this plan outlines the product architecture.

### 1. Feature Roadmap
* **Create Note:** A frontend form to capture title and content.
* **Dynamic Gallery:** Fetching and rendering all notes from the database automatically on page load.
* **Data Validation:** Ensures no empty notes are sent to the server.
* **Responsive Design:** Mobile-first CSS to ensure the app works on all screen sizes.

### 2. Technical Architecture (OSI Layer 7)
The application follows a standard Request-Response cycle:
1. **Frontend:** HTML5, CSS3, and Vanilla JavaScript (DOM Manipulation & Promises).
2. **Backend:** Python Flask API handling GET and POST requests.
3. **Database:** Supabase (PostgreSQL) for persistent data storage.

### 3. Logic Flowchart
[User Input] -> [JS Validation] -> [Fetch API (POST)] -> [Flask Route] -> [Supabase SQL]
      ^                                                                    |
      |_______________________[Fetch API (GET)] <--------------------------|

---

## Evaluation Criteria Checklist
- [x] Frontend UI (HTML/CSS/Responsive)
- [x] JS Logic (Dynamic Rendering)
- [x] Working APIs (Flask GET/POST)
- [x] Database Integration (Supabase)
- [x] CRUD Operations & Data Validation

---

## How to Run
1. Clone the repository: `git clone [https://github.com/tushard4s/capstone-project]`
2. Install dependencies: `pip install flask requests`
3. Run the backend: `python app.py`
4. Open `index.html` in your browser.