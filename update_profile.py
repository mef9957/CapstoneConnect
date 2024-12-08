#!/usr/bin/python3

import cgi
import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Content-Type: text/html")
print("Location: login.html")     # Set location for redirection
print()  # End of headers

data = cgi.FieldStorage()

def read_advisor_data(filename):
    advisors = {}
    with open(filename, newline='', encoding='latin-1') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) 
        for row in reader:
            name = row[0]
            email = row[1]
            research_areas = row[8].split(', ')
            bio = row[9]
            department = row[3].title()
            affiliation = row[6]
            sublink = row[2]
            imglink = row[10]
            filename = imglink.split('/')[-1]
            imglink = "downloaded_images/" + filename
            major = row[4]
            major = major.replace('[', "").replace(']', "").replace("'", "").replace(",", " ")
            advisors[name] = {
                "email": email,
                "research_areas": research_areas,
                "bio": bio,
                "affiliation": affiliation,
                "department": department,
                "major": major,
                "sublink": sublink,
                "imglink": imglink
            }
    return advisors

def get_match(name, department, major, interests_str, affiliation):
    advisors = read_advisor_data('faculty.csv')
    major = major.replace("-", " ")
    interests = interests_str.replace("-", " ").split(", ")

    student_interests = interests_str
    advisor_areas = [", ".join(advisor_info["research_areas"]) for advisor_info in advisors.values()]
    all_texts = [student_interests] + advisor_areas

    vectorizer = CountVectorizer().fit(all_texts)
    text_vectors = vectorizer.transform(all_texts).toarray()

    student_vectors = text_vectors[0]
    advisor_vectors = text_vectors[1:]

    similarity_scores = cosine_similarity([student_vectors], advisor_vectors)[0]

    for index, (advisor_name, advisor_info) in enumerate(advisors.items()):
        advisor_info["score"] = similarity_scores[index]

    filtered_advisors = {advisor_name: advisor_info for advisor_name, advisor_info in advisors.items()
                         if affiliation in advisor_info["affiliation"]}

    for advisor_name, advisor_info in filtered_advisors.items():
        if major.lower() in advisor_info["major"].lower():
            advisor_info["score"] += 0.1
        if department.lower() in advisor_info["department"].lower():
            advisor_info["score"] += 0.1

        for interest in interests:
            if interest.strip().lower() in [area.lower() for area in advisor_info["research_areas"]]:
                advisor_info["score"] += 0.1
            if interest.strip().lower() in [area.lower() for area in advisor_info["bio"]]:
                advisor_info["score"] += 0.02

    sorted_advisors = sorted(filtered_advisors.items(), key=lambda x: x[1]["score"], reverse=True)
    top_advisors = [advisor_name for advisor_name, _ in sorted_advisors[:6]]

    return top_advisors

def update_profile():
    name = data.getvalue('name','N/A')  
    email = data.getvalue('email', 'N/A')
    major = data.getvalue('major', 'N/A')
    department = data.getvalue('department', 'N/A')
    r_interests = data.getlist('r-interests')
    interests_str = ', '.join(r_interests) if r_interests else 'None'
    affiliation = data.getvalue('affiliation', 'N/A')

    top_advisors = get_match(name, department, major, interests_str, affiliation)

    csv_filename = f"{email}.csv"
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        advisors = read_advisor_data('faculty.csv')
        for advisor_name in top_advisors:
            advisor_info = advisors[advisor_name]
            writer.writerow([
                advisor_name,
                advisor_info['email'],
                advisor_info['department'],
                advisor_info['major'],
                advisor_info['imglink'],
                advisor_info['affiliation'],
                f"faculty_view.py?input1={advisor_name}&input2={email}"
            ])


def get_values():
    name = data.getvalue('name','N/A')
    email = data.getvalue('email', 'N/A')
    password = data.getvalue('password', 'N/A')
    major = data.getvalue('major', 'N/A')
    department = data.getvalue('department', 'N/A')

    r_interests = data.getlist('r-interests')
    interests_str = ', '.join(r_interests) if r_interests else 'None'

    skills = data.getvalue('skills', 'N/A')
    
    num_semesters = data.getvalue('num-semesters', 'N/A')
    affiliation = data.getvalue('affiliation', 'N/A')

    top_advisors = get_match(name,department,major,interests_str,affiliation)

    csv_filename = f"{email}.csv"
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        advisors = read_advisor_data('faculty.csv')
        for advisor_name in top_advisors:
            advisor_info = advisors[advisor_name]
            writer.writerow([
                advisor_name,
                advisor_info['email'],
                advisor_info['department'],
                advisor_info['major'],
                advisor_info['imglink'],
                advisor_info['affiliation'],
                f"faculty_view.py?input1={advisor_name}&input2={email}"
            ])

    line = f"{email}:{password}:{name}:{department}:{major}:{interests_str}:{skills}:{num_semesters}:{affiliation}:{top_advisors}\n"

    with open('student_database.txt', 'r') as file:
        lines = file. readlines()
        #Filter out lines with the same email
        new_lines = [line for line in lines if not line.startswith(email)]

    # Write back to the file
    with open('student_database.txt', 'w') as file2:
        file2.writelines (new_lines)
    
    with open("student_database.txt", "a") as filer:
        filer.write(line)
    

def main():
    get_values()
    update_profile()

main()