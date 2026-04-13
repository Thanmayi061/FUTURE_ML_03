import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# LOAD DATASET
# -------------------------------
df = pd.read_csv("resumes.csv")

# -------------------------------
# JOB ROLE
# -------------------------------
job_role = "Data Scientist"

required_skills = ["python", "machine learning", "data analysis", "sql"]

print("\n🎯 Job Role:", job_role)
print("Required Skills:", required_skills)

# -------------------------------
# FUNCTION: CALCULATE SCORE
# -------------------------------
def calculate_score(resume):
    resume = resume.lower()
    score = 0
    matched_skills = []

    for skill in required_skills:
        if skill in resume:
            score += 1
            matched_skills.append(skill)

    missing_skills = list(set(required_skills) - set(matched_skills))

    return score, matched_skills, missing_skills

# -------------------------------
# APPLY SCORING
# -------------------------------
scores = []
matched = []
missing = []

for resume in df["resume_text"]:
    score, match, miss = calculate_score(resume)
    scores.append(score)
    matched.append(", ".join(match))
    missing.append(", ".join(miss))

df["score"] = scores
df["matched_skills"] = matched
df["missing_skills"] = missing

# -------------------------------
# SORT (RANKING)
# -------------------------------
df = df.sort_values(by="score", ascending=False)

# -------------------------------
# OUTPUT TABLE
# -------------------------------
print("\n📊 Candidate Ranking:\n")
print(df[["name", "score", "matched_skills", "missing_skills"]])

# -------------------------------
# GRAPH 1: BAR CHART
# -------------------------------
plt.figure()
plt.bar(df["name"], df["score"])

plt.xticks(rotation=90)
plt.title("Candidate Ranking (Scores)")
plt.xlabel("Candidates")
plt.ylabel("Score")

plt.tight_layout()
plt.show()

# -------------------------------
# GRAPH 2: PIE CHART
# -------------------------------

# Categorize candidates
def categorize(score):
    if score == 4:
        return "Excellent"
    elif score == 3:
        return "Good"
    elif score == 2:
        return "Average"
    else:
        return "Poor"

df["category"] = df["score"].apply(categorize)

# Count categories
category_counts = df["category"].value_counts()

# Plot pie chart
plt.figure()
category_counts.plot(kind='pie', autopct='%1.1f%%')

plt.title("Candidate Skill Match Distribution")
plt.ylabel("")

plt.show()
