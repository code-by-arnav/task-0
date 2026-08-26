import numpy as np

hours_studied = np.array([5.9, 3.6, 6.5, 5.4, 1.2])
attendance = np.array([100, 85, 73, 73, 74])
previous_scores = np.array([52, 74, 49, 78, 77])
final_scores = np.array([60, 47, 41, 50, 35])

print("Hours studied shape:", hours_studied.shape, "dtype:", hours_studied.dtype)
print("Attendance shape:", attendance.shape, "dtype:", attendance.dtype)
print("Previous scores shape:", previous_scores.shape, "dtype:", previous_scores.dtype)
print("Final scores shape:", final_scores.shape, "dtype:", final_scores.dtype)

mean_final = np.mean(final_scores)
max_final = np.max(final_scores)
min_final = np.min(final_scores)
std_final = np.std(final_scores)

print("\nMean final score:", mean_final)
print("Max final score:", max_final)
print("Min final score:", min_final)
print("Std deviation of final scores:", std_final)

final_scores_bonus = final_scores + 5
print("\nFinal scores with 5 bonus marks:", final_scores_bonus)

passed_75 = final_scores >= 75
print("Boolean array (scored >= 75):", passed_75)

print("Scores >= 75:", final_scores[passed_75])