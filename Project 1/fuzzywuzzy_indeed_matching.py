import pandas as pd
from fuzzywuzzy import process
from tqdm import tqdm

# Read the CSV file
df = pd.read_csv('merged_cleaned_files.csv')

# Read the skills and certifications files
with open('skill_list.txt', 'r') as f:
    skills = f.read().splitlines()

with open('certification_list.txt', 'r') as f:
    certifications = f.read().splitlines()

def find_skills(description):
    found_skills = []
    for skill in skills:
        if process.extractOne(skill, description.split(), score_cutoff=92):
            found_skills.append(skill)
    return found_skills

def find_certifications(description):
    found_certifications = []
    for certification in certifications:
        if process.extractOne(certification, description.split(), score_cutoff=95):
            found_certifications.append(certification)
    return found_certifications

# Apply the functions with a progress bar
tqdm.pandas()
df['skills'] = df['job_title_description'].progress_apply(find_skills)
df['certifications'] = df['job_title_description'].progress_apply(find_certifications)

# Print the first 10 rows of the DataFrame
print(df.head(10))

df.to_csv('jobs_with_skills_and_certifications.csv', index=False)
