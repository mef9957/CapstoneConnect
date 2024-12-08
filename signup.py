#!/usr/bin/python3  

import cgi  # Import CGI module for handling CGI scripts
import csv  # Import CSV module for CSV file operations
import numpy as np  # Import NumPy for numerical operations
from sklearn.feature_extraction.text import CountVectorizer  # Import CountVectorizer for text vectorization
from sklearn.metrics.pairwise import cosine_similarity  # Import cosine similarity for similarity computation

print("Content-Type: text/html")  # Declare content type for HTTP response
print("Location: login.html")     # Set location for redirection
print()                           # End of headers

data = cgi.FieldStorage()  # Get CGI form data

def store(line):  # Function to store data in the student database
    with open("student_database.txt", "a") as filer:  # Open database file in append mode
        filer.write(line)  # Write the line to the file

def read_advisor_data(filename):  # Function to read advisor data from a CSV file
    advisors = {}  # Dictionary to store advisor data
    with open(filename, newline='', encoding='latin-1') as csvfile:
        reader = csv.reader(csvfile) # Create CSV reader
        next(reader)  # Skip header
        for row in reader:
            # Extract data from row
            name = row[0]
            email = row[1]
            research_areas = row[8].split(', ')
            bio = row[9]
            department = row[3].title()
            affiliation = row[6]
            sublink = row[2]
            imglink = row[10]
            # Modify image link and format major
            filename = imglink.split('/')[-1]
            imglink = "downloaded_images/"+filename
            major = row[4]
            major = major.replace('[',"").replace(']',"").replace("'","").replace(","," ")
            # Store advisor data in dictionary
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
    return advisors # Return advisor data dictionary

# Function to find matching advisors
def getmatch(name,department,major,interests_str,affiliation): 

    advisors = read_advisor_data('faculty.csv') # Read advisor data
    major = major.replace("-", " ") # Replace '-' with space in major
    interests = interests_str.replace("-", " ").split(", ") # Split interests by comma and replace '-'

    # Extract text data for vectorization
    student_interests = interests_str
    advisor_areas = [", ".join(advisor_info["research_areas"]) for advisor_info in advisors.values()]
    all_texts = [student_interests] + advisor_areas

    # Vectorize the texts
    vectorizer = CountVectorizer().fit(all_texts)
    text_vectors = vectorizer.transform(all_texts).toarray()

    # Split vectors back into student and advisor parts
    student_vectors = text_vectors[0]  # Vector for the student
    advisor_vectors = text_vectors[1:]  # Vectors for advisors

    # Compute cosine similarity between student and advisors
    similarity_scores = cosine_similarity([student_vectors], advisor_vectors)[0]

    # Assign scores to advisors based on similarity
    for index, (advisor_name, advisor_info) in enumerate(advisors.items()):
        advisor_info["score"] = similarity_scores[index]

    # Filter advisors based on student's specified affiliation
    filtered_advisors = {advisor_name: advisor_info for advisor_name, advisor_info in advisors.items()
                         if affiliation in advisor_info["affiliation"]}

    # Iterate over remaining advisors and modify matching score based on student's details
    for advisor_name, advisor_info in filtered_advisors.items():
        # Increase score if student's major or department matches advisor's information
        if major.lower() in advisor_info["major"].lower():
            advisor_info["score"] += 0.1  # Increase score
        if department.lower() in advisor_info["department"].lower():
            advisor_info["score"] += 0.1  # Increase score

        # Check if any of the student's interests match with advisor's research areas
        for interest in interests:
            if interest.strip().lower() in [area.lower() for area in advisor_info["research_areas"]]:
                advisor_info["score"] += 0.1  # Increase score for matching interests
            if interest.strip().lower() in [area.lower() for area in advisor_info["bio"]]:
                advisor_info["score"] += 0.02  # Increase score for matching interests

    # Sort advisors based on modified matching score
    sorted_advisors = sorted(filtered_advisors.items(), key=lambda x: x[1]["score"], reverse=True)

    # Select top 6 advisors for the student
    top_advisors = [advisor_name for advisor_name, _ in sorted_advisors[:6]]

    return top_advisors

# Function to get form values
def getvalues():
    name = data.getvalue('name','N/A')
    email = data.getvalue('email', 'N/A')
    password = data.getvalue('password', 'N/A')
    major = data.getvalue('major', 'N/A')
    department = data.getvalue('department', 'N/A')

    # Handle multiple selections for research interests
    r_interests = data.getlist('r-interests')
    interests_str = ', '.join(r_interests) if r_interests else 'None'

    skills = data.getvalue('skills', 'N/A')
    
    # Handle single selection for number of semesters
    num_semesters = data.getvalue('num-semesters', 'N/A')
    affiliation = data.getvalue('affiliation', 'N/A')

    top_advisors = getmatch(name,department,major,interests_str,affiliation)

    # Create CSV file with student's email as the file name
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
                f"faculty_view.py?input1={advisor_name}"
            ])


    line = f"{email}:{password}:{name}:{department}:{major}:{interests_str}:{skills}:{num_semesters}:{affiliation}:{top_advisors}\n"
    return line  # Return line for storing in database

def main():
    # Process the form data and store it
    line = getvalues()
    store(line)

# Execute the main function
main()
