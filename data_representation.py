import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Loading data...")

df = pd.read_csv('../political_triples_grouped.csv')

# 2. Clean the data (ensure Scores are numbers and Subjects are strings)
df['Score'] = pd.to_numeric(df['Score'], errors='coerce').fillna(0.5)
df['Subject'] = df['Subject'].astype(str).str.strip()
 
# CHART 1: SELECTION BIAS (Who do they talk about?)

print("Chart 1: Top Subjects...")
plt.figure(figsize=(10, 6))
# Top 7 most mentioned subjects
top_subjects = df['Subject'].value_counts().head(7)

sns.barplot(x=top_subjects.values, y=top_subjects.index, palette='Blues_r')
plt.title('Selection Focus: Top Mentioned Political Entities', fontsize=14, fontweight='bold')
plt.xlabel('Number of Triplets (Mentions)', fontsize=12)
plt.ylabel('Entity / Subject', fontsize=12)
plt.tight_layout()
plt.savefig('Slide1_Selection_Focus.png', dpi=300)
plt.close()

# CHART 2: FRAMING BIAS (How do they talk about them?)

print("Generating Chart 2: Framing Scores...")
# Get the average score for those top 7 subjects
top_subject_names = top_subjects.index.tolist()
framing_data = df[df['Subject'].isin(top_subject_names)]

avg_scores = framing_data.groupby('Subject')['Score'].mean().sort_values()

plt.figure(figsize=(10, 6))
# Colors: Red for low score (negative frame), Green for high score (positive frame)
sns.barplot(x=avg_scores.values, y=avg_scores.index, palette='RdYlGn')
plt.axvline(x=0.5, color='black', linestyle='--', label='Neutral Baseline')

plt.title('Framing Bias: Average Intent Score per Entity', fontsize=14, fontweight='bold')
plt.xlabel('Average Score (0 = Critical, 1 = Positive)', fontsize=12)
plt.ylabel('Entity / Subject', fontsize=12)
plt.legend()
plt.tight_layout()
plt.savefig('Slide2_Framing_Score.png', dpi=300)
plt.close()


print("\n" + "="*50)
print("SUCCESS! Two images generated for your slides:")
print("1. Slide1_Selection_Focus.png")
print("2. Slide2_Framing_Score.png")
print("="*50)

print("\n--- FAST STATS TO READ TO THE JUDGES ---")
print(f"Total Triplets Extracted: {len(df)}")
print(f"Total Unique Subjects Found: {df['Subject'].nunique()}")
print("\nTop 3 Most Focused Entities:")
for i, (name, count) in enumerate(top_subjects.head(3).items(), 1):
    print(f"{i}. {name} ({count} mentions)")