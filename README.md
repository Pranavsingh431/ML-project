# Student Exam Performance Indicator

The **Student Exam Performance Indicator** is a web-based application that predicts a student's mathematics score based on their demographics, parental education level, and performance in other subjects (reading and writing). The application uses Flask for backend development and machine learning for predictions.

---

## Features

- **Input Form**: Users can input various attributes, such as gender, ethnicity, parental education, lunch type, test preparation, reading score, and writing score.
- **Prediction**: The application predicts the mathematics score based on the provided inputs.
- **Dynamic Routing**: The app includes an index page and a home page for ease of navigation.
- **Responsive UI**: Simple and clean user interface for seamless user experience.

---

## Technologies Used

- **Backend**: Flask
- **Frontend**: HTML, CSS
- **Machine Learning**: Scikit-learn
- **Other Libraries**: Pandas, NumPy
- **Environment**: Python 3.12+

---

## Installation Guide

### Prerequisites
- Python 3.12+
- Pip (Python Package Manager)

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/student-performance-indicator.git
   cd student-performance-indicator
2. **Creating Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
4. **Run the Application:**:
   ```bash
   python app.py
5. Access the Application: Open your browser and navigate to http://127.0.0.1:5000/.
