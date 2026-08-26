# Task 0: Python Fundamentals, Data Analysis & Git

**Name:** Arnav Agrawal

## Description

This repository contains my solutions for Task 0, a progressive introduction to Python fundamentals, NumPy, Pandas, Matplotlib, and Git/GitHub workflow, completed for the Mathematics Association (BITS Pilani) Development Team recruitment task.

- **Q1** – List analyzer (largest, smallest, sum, even/odd counts, reversed) without built-in functions
- **Q2** – `process_list()` function demonstrating safe list copying with `.copy()`
- **Q3** – Prime number checker using Python's `for-else` syntax
- **Q4** – NumPy array operations: shape, dtype, mean, max, min, std, vectorized operations, Boolean indexing
- **Q5** – Pandas analysis of `student_performance.csv`: filtering, sorting, new columns, CSV export
- **Q6** – Matplotlib visualizations: bar chart, scatter plot, histogram, and a custom plot

## Setup Instructions

1. Make sure Python 3 is installed.
2. Install the required libraries:

pip install numpy pandas matplotlib

## How to Run

Each question is a standalone script. Run them individually from the `task-0` folder:

python q1.py
python q2.py
python q3.py
python q4.py
python q5.py
python q6.py

- `q1.py` and `q3.py` will prompt for input in the terminal.
- `q5.py` reads `data/student_performance.csv` and generates `data/processed_student_performance.csv`.
- `q6.py` reads the processed CSV and saves 4 graph images into the `plots/` folder.

## Folder Structure

task-0/
├── README.md
├── q1.py
├── q2.py
├── q3.py
├── q4.py
├── q5.py
├── q6.py
├── data/
│   ├── student_performance.csv
│   └── processed_student_performance.csv
└── plots/
    ├── final_scores.png
    ├── study_vs_score.png
    ├── score_distribution.png
    └── custom_plot.png