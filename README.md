# 🚀 Candidate Fusion Hub

A Python-based **Multi-Source Candidate Data Transformer** that consolidates candidate information from multiple data sources into a single standardized JSON profile. The application extracts, normalizes, merges, validates, and exports candidate data while maintaining consistency and reducing duplicate information.

---

## 📌 Problem Statement

Recruitment data is often collected from multiple platforms such as Recruiter CSVs, ATS systems, LinkedIn profiles, and GitHub profiles. Since these sources use different formats and may contain duplicate or inconsistent information, maintaining a unified candidate profile becomes challenging.

Candidate Fusion Hub addresses this problem by transforming heterogeneous candidate data into a single clean and standardized JSON profile.

---

## 🎯 Project Objective

The primary objective of this project is to:

- Extract candidate information from multiple sources.
- Normalize inconsistent data formats.
- Merge duplicate candidate records.
- Validate mandatory fields.
- Generate a unified candidate profile in JSON format.

---

## ✨ Features

- Multi-source candidate data extraction
- CSV and JSON file processing
- Data normalization
- Duplicate data removal
- Source priority-based merging
- Required field validation
- Standardized JSON profile generation
- Configurable application using `config.json`
- Modular and clean project architecture

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core Programming Language |
| Pandas | CSV Processing |
| JSON | Data Storage & Processing |
| Pydantic | Data Modeling |
| JSON Schema | Output Validation |
| RapidFuzz | Skill Matching & Deduplication |
| Phonenumbers | Phone Number Normalization |
| VS Code | Development Environment |
| Git & GitHub | Version Control |

---

## 📂 Project Structure

```text
candidate-fusion-hub/
│
├── data/
│   ├── recruiter.csv
│   ├── ats.json
│   ├── linkedin.json
│   ├── github.json
│
├── output/
│   └── candidate_profile.json
│
├── src/
│   ├── extract.py
│   ├── normalize.py
│   ├── merge.py
│   ├── validate.py
│   └── utils.py
│
├── config.json
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Workflow

```text
Input Files
     │
     ▼
Data Extraction
     │
     ▼
Data Normalization
     │
     ▼
Data Merging
     │
     ▼
Validation
     │
     ▼
Candidate Profile (JSON)
```

---

## 📥 Input Sources

The application accepts candidate information from:

- Recruiter CSV
- ATS JSON
- LinkedIn JSON
- GitHub JSON

---

## 🔄 Data Processing

### 1. Data Extraction
Reads candidate information from multiple structured sources.

### 2. Data Normalization
Standardizes:
- Email addresses
- Phone numbers
- Skills
- Experience

### 3. Data Merging
Combines information from multiple sources while removing duplicates and preserving the highest-priority values.

### 4. Data Validation
Checks mandatory fields before generating the final output.

### 5. Output Generation
Creates a standardized candidate profile in JSON format.

---

## 📄 Output

The final transformed candidate profile is generated as:

```text
output/candidate_profile.json
```

Example:

```json
{
  "Candidate_ID": "C001",
  "Name": "John Doe",
  "Email": "john.doe@gmail.com",
  "Phone": "+919876543210",
  "Location": "Nagpur",
  "Skills": [
    "Python",
    "SQL",
    "Power BI",
    "Excel"
  ],
  "Experience": "3 Years"
}
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/candidate-fusion-hub.git
```

Move into the project directory:

```bash
cd candidate-fusion-hub
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 📊 Project Highlights

- Consolidates candidate data from multiple sources
- Eliminates duplicate information
- Standardizes candidate details
- Validates mandatory fields
- Produces a clean JSON profile
- Easy to understand and extend

---

## 🚀 Future Enhancements

- Resume Parsing using NLP
- LinkedIn API Integration
- MongoDB/MySQL Database Support
- Web Dashboard using Streamlit
- AI-based Candidate Confidence Scoring
- Candidate Similarity Matching

---

## 📚 Learning Outcomes

This project demonstrates practical implementation of:

- Python Programming
- Data Processing
- Data Transformation
- JSON Handling
- CSV Processing
- Data Validation
- Modular Software Development
- Clean Project Architecture

---

## ⭐ Project Summary

**Candidate Fusion Hub** is a lightweight and modular Python application designed to transform candidate information from multiple sources into a unified and standardized JSON profile. By combining extraction, normalization, merging, and validation into a single workflow, the project demonstrates a practical approach to solving real-world data integration challenges in recruitment systems.
