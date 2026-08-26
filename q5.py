import pandas as pd

df = pd.read_csv("data/student_performance.csv")

print(df.head())
print("\nNumber of rows and columns:", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nMissing values in each column:\n", df.isnull().sum())
avg_final = df["Final_Score"].mean()
print("\nAverage Final_Score:", avg_final)

top_student = df.loc[df["Final_Score"].idxmax()]
print("\nStudent with highest Final_Score:\n", top_student)

df["Improvement"] = df["Final_Score"] - df["Previous_Score"]
print("\nDataFrame with Improvement column:\n", df.head())

high_attendance = df[df["Attendance"] >= 80]
print("\nStudents with attendance >= 80:\n", high_attendance)

df_sorted = df.sort_values(by="Final_Score", ascending=False)
print("\nSorted by Final_Score descending:\n", df_sorted.head())

df_sorted.to_csv("data/processed_student_performance.csv", index=False)
print("\nSaved processed_student_performance.csv")