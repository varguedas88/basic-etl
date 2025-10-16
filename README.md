# Basic ETL with Python & Pandas

This project demonstrates a simple **ETL (Extract, Transform, Load)** process using Python and Pandas.

---

## Project Overview
This repository contains a basic ETL pipeline designed for educational purposes.  
It extracts data from CSV files, cleans and transforms it using Pandas, and loads the final output into a structured format.

---

## Tools Used
- **Python 3.11**
- **Pandas**
- **SQLAlchemy**
- **SQLite**

---

## 📂 Project Structure
basic-etl/
│
├── data/ # Raw data sources
├── output/ # Processed data and results
├── src/ # ETL scripts (extract, transform, load)
└── README.md

---

## How to run
```bash
git clone https://github.com/tuusuario/etl_basico.git
cd etl_basico/src
pip install -r ../requirements.txt
python etl_pipeline.py
