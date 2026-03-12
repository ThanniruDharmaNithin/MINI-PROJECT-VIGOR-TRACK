<div align="center">

# 🩺 VigorTrack: Proactive Health Monitoring & Guidance
### *Your health, our mission.*

![React Native](https://img.shields.io/badge/React_Native-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

**MINI PROJECT By:** [Thanniru Dharma Nithin](https://github.com/ThanniruDharmaNithin)

---

</div>

## 🗂️ Agenda
A brief outline of this project:  
1. **Project Overview:** Introduction to VigorTrack’s purpose  
2. **Implementation Goals:** Key objectives during development  
3. **Work Completed:** Features developed and functionalities implemented  
4. **Challenges:** Technical and non-technical obstacles  
5. **Results & Achievements:** Outcome metrics and success  
6. **Future Plans:** Enhancements and next steps  
7. **How to Run Locally:** Setup instructions for backend and frontend  

---

## 🏥 Project Overview

**Objective:**  
- Detect health risks early for patients.  
- Log symptoms using machine learning.  
- Provide personalized health assessments.  

**Scope:**  
- Prevent illnesses by early detection.  
- Help people notice mild symptoms.  
- Avoid serious health problems through early action.  

**Problem Statement:**  
Many people ignore mild symptoms due to busy schedules, which can lead to long-term health problems.  
**VigorTrack** provides quick risk assessments and encourages early medical attention.

---

## 🔬 Project Plan (High-Level Overview)

**Team Roles:**  
- **Thanniru Dharma Nithin:** Research, documentation, front-end development & design.  
- **Simhadri Harshitha:** Back-end, full-stack integration, research.  

**Timeline & Key Phases:**  

| Phase | Duration | Description |
|---|---|---|
| **Research & Planning** | 1-2 weeks | Understanding problem, target users, existing solutions |
| **Design** | 2 weeks | UI/UX design with Canva, focus on accessibility |
| **Development** | 4-5 weeks | Front-end in React Native, back-end with Flask/Firebase |
| **ML Integration** | 3 weeks | Naive Bayes, Random Forest, Decision Tree for predictions |
| **Testing & Deployment** | 2-3 weeks | User testing, validation, deployment |

---

## 🎯 Goals of Implementation Phase

**Primary Objective:**  
Create a seamless healthcare platform providing **real-time risk assessments** based on symptom input.  

**Success Criteria:**  
- ✅ Integrate machine learning models with high prediction accuracy.  
- ✅ Intuitive UX for easy symptom logging & feedback.  
- ✅ Real-time performance (<3 seconds for results).  

**Key Features Achieved:**  
- Cross-platform (iOS & Android).  
- Secure login system.  
- Instant health risk assessments.  

---

## 🏗️ Implementation Architecture / System Design

- **Front-End:** React Native for responsive UI.  
- **Back-End:** Flask, Postman, Scikit-learn for API, testing, and models.  
- **Machine Learning Models:** Naive Bayes, Random Forest, KNN, Decision Tree trained on symptoms.  

**Agile Workflow:**  
- **Sprint 1:** Initial research & prototype.  
- **Sprint 2:** Front-end UI development.  
- **Sprint 3:** Backend integration & ML training.  
- **Sprint 4:** Testing & feature adjustments.  

---

## 💻 Workflow / Methodology
1. Requirement analysis.  
2. Prototyping.  
3. Development iterations & testing.  
4. Deployment & feedback loop.  

---

## ✅ Work Completed / Tasks Accomplished

**Module Breakdown:**  
- **Module 1:** Symptom Logging – Users log symptoms for system analysis.  
- **Module 2:** ML Model Integration – Predicts health risks based on symptoms.  
- **Module 3:** Doctor Consultation Suggestion – Recommends consultation for high-risk users.  

**Technical Challenges & Solutions:**  

| Challenge | Solution |
|---|---|
| **Memory Usage** | Optimized symptom datasets and algorithms to prevent overflows. |
| **Real-Time Processing** | Used optimized models and lightweight APIs. |
| **Cross-Platform Bugs** | Platform-specific fixes in React Native for UI consistency. |

---

## 🛠️ Tech Stack & Tools

VigorTrack leverages a combination of **mobile development, machine learning, and cloud technologies**:

| Component | Tools / Libraries | Purpose |
|---|---|---|
| **Programming Language** | Python, JavaScript, CSS | Core programming for ML and app logic |
| **Frontend / Mobile App** | React Native | Cross-platform mobile app |
| **Backend / API** | Flask | REST API for ML model predictions |
| **Machine Learning** | Naive Bayes, Random Forest, KNN | Predicting health risks |
| **Data Processing** | Scikit-learn, Pandas, NumPy | Data cleaning and model training |
| **Development Tools** | Postman, Jupyter Notebook | API testing and prototyping |
| **UI/UX Design** | Canva | Mobile interface design |
| **Version Control** | Git & GitHub | Project management |
| **Deployment / Testing** | VS Code, Android Studio | App deployment and testing |

---

## 🌟 Key Achievements
- **Cross-Platform Functionality:** Works smoothly on iOS & Android.  
- **High Prediction Accuracy:** ML models achieved >98% accuracy.  
- **User Engagement:** Intuitive interface encourages regular symptom tracking.  

---

## 📊 Data Preprocessing & Visualization
- Handled missing values before training ML models.  
- Visualized key features for model input to improve classification.  

---

## 📱 Example Prediction
**Prediction:** Bronchial Asthma  
- **Description:** Airway swelling causes excess mucus → difficulty breathing, coughing, wheezing.  
- **Precautions:** Wear loose clothing, practice deep breathing, avoid triggers, seek help.  

---

## 📈 Results & Metrics

| Model | Accuracy |
|---|---|
| **Naive Bayes** | 87.80% |
| **Decision Tree** | 95.93% |
| **Random Forest** | 98.78% |
| **KNN** | 98.98% |

- **Response Time:** <2 seconds per prediction.  
- **User Testing:** 90% found the app easy to use with high satisfaction.  

---

## 🔮 Future Improvements & Next Steps

**Future Enhancements:**  
- 🤖 Chatbot for interactive symptom consultation.  
- 📹 Video/audio doctor consultations.  
- 🗄️ Expand the symptom database.  

**Next Steps:**  
- Further optimize ML models.  
- Implement a doctor rating system.  
- Add multi-language support.  

---

## ▶️ How to Run Locally

Follow these steps to run both the **Flask Backend** and **React Native Frontend** on your local machine.

### Prerequisites
Before starting, make sure you have installed:
- [Node.js](https://nodejs.org/) (v16 or higher)
- [Python 3.10+](https://www.python.org/downloads/)
- [Android Studio](https://developer.android.com/studio) (for running the Android Emulator)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ThanniruDharmaNithin/VigorTrack.git
cd VigorTrack
```

---

### 2️⃣ Start the Flask Backend (Machine Learning API)
Open a terminal and navigate to the backend folder:
```bash
# 1. Navigate to the backend directory
cd backend

# 2. Create a virtual environment (Recommended)
python -m venv venv

# 3. Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# 4. Install required Python packages
pip install -r requirements.txt

# 5. Run the Flask server
python app.py
```
*The API will start running at `http://127.0.0.1:5000`.*

---

### 3️⃣ Start the React Native Frontend (Mobile App)
Open a **new terminal window** (keep the Flask terminal running), and navigate to the frontend folder:

```bash
# 1. Navigate to the frontend directory
cd frontend

# 2. Install Node dependencies
npm install

# 3. Start the Metro Bundler
npx react-native start
```

### 4️⃣ Launch the App on an Emulator
Open Android Studio, launch your **Virtual Device (Emulator)**, and in a **third terminal** inside the `frontend` folder, run:

```bash
npx react-native run-android
```
*(If you are on a Mac and testing for iOS, run `npx react-native run-ios` instead).*

---

## 🏁 Conclusion
**VigorTrack** empowers users to **monitor their health** using symptom analysis and real-time risk assessment via machine learning. The app guides users on when to seek medical attention, promoting early action and better outcomes. Its **user-friendly design** makes health tracking simple, accessible, and reliable.

<div align="center">

*If you like this project, please consider giving it a ⭐ on GitHub!*

</div>
