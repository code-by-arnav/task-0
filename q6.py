import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed_student_performance.csv")

plt.figure(figsize=(12, 6))
plt.bar(df["Student"], df["Final_Score"])
plt.title("Final Scores by Student")
plt.xlabel("Student")
plt.ylabel("Final Score")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("plots/final_scores.png")
plt.close()

print("Saved final_scores.png")

plt.figure(figsize=(8, 6))
plt.scatter(df["Hours_Studied"], df["Final_Score"])
plt.title("Hours Studied vs Final Score")
plt.xlabel("Hours Studied")
plt.ylabel("Final Score")
plt.tight_layout()
plt.savefig("plots/study_vs_score.png")
plt.close()

print("Saved study_vs_score.png")
plt.figure(figsize=(8, 6))
plt.hist(df["Final_Score"], bins=10, edgecolor="black")
plt.title("Distribution of Final Scores")
plt.xlabel("Final Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("plots/score_distribution.png")
plt.close()

print("Saved score_distribution.png")
plt.figure(figsize=(8, 6))
plt.scatter(df["Attendance"], df["Final_Score"], color="green")
plt.title("Attendance vs Final Score")
plt.xlabel("Attendance (%)")
plt.ylabel("Final Score")
plt.tight_layout()
plt.savefig("plots/custom_plot.png")
plt.close()

print("Saved custom_plot.png")
