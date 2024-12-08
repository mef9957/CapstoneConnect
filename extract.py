# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import csv

# URL of the webpage
url = "https://nyuad.nyu.edu/en/academics/faculty.html"

program_names = [
    "African Studies",
    "Ancient World",
    "Anthropology",
    "Arabic",
    "Arab Crossroads Studies",
    "Arab Music Studies",
    "Art and Art History",
    "Chinese",
    "Design",
    "Film and New Media",
    "French",
    "History",
    "Interactive Media",
    "Legal Studies",
    "Literature and Creative Writing",
    "Music",
    "Philosophy",
    "Theater",
    "Biology",
    "Chemistry",
    "Computer Science",
    "Environmental Studies",
    "Mathematics",
    "Natural Science",
    "Physics",
    "Psychology",
    "Business, Organizations and Society",
    "Economics",
    "Peace Studies",
    "Political Science",
    "Social Research and Public Policy",
    "Bioengineering",
    "Civil Engineering",
    "Computer Engineering",
    "Electrical Engineering",
    "General Engineering",
    "Mechanical Engineering"
]

# Send a GET request to the webpage
response = requests.get(url)

# Parse the HTML content of the webpage
soup = BeautifulSoup(response.text, "html.parser")

# Find all faculty containers
faculty_list = soup.find_all("div", class_="faculty-container")

# Create a CSV file to write the data
with open("faculty.csv", "w", newline="", encoding="utf-8") as csvfile:
    # Define the CSV writer
    csvwriter = csv.writer(csvfile)

    # Write the header row
    csvwriter.writerow(["Name", "Email", "Sublink", "Divison", "Program", "Title", "Affiliation", "Education", "Research Areas", "Bio", "ImageUrl"])

    # Iterate through each faculty container
    for faculty in faculty_list:
        # Extract name
        name = faculty.find(itemprop="name").get_text()

        # Extract email and remove %20
        email = faculty.find(itemprop="email").get("href").replace("mailto:", "").replace("%20", "")

        # Extract sublink
        sublink = "https://nyuad.nyu.edu" + faculty.find('a', class_='photo-link').get('href')

        # Extract division from sublink
        division = sublink.split('/divisions/')[1].split('/')[0].replace("-", " ")

        # Send a GET request to the faculty sublink
        response2 = requests.get(sublink)
        soup = BeautifulSoup(response2.text, "html.parser")

        # Extract image URL
        image_url = "https://nyuad.nyu.edu" + soup.find('div', class_='responsive-img')['data-src']
        response3 = requests.get(image_url)
        soup2 = BeautifulSoup(response3.text, 'html.parser')

        # Find the img tag and extract the value of the src attribute
        src_value = soup2.find('img', class_='cq-dd-image')['src']

        # Construct the full image URL by appending it to the base URL
        image_url = "https://nyuad.nyu.edu" + src_value

        # Extract title from faculty detail section
        title_span = soup.find('div', class_='faculty-detail').find('span', class_='title')
        if title_span:
            title = title_span.get_text(strip=True)
        else:
            title = "N/A"

        # Check for program names in the title
        programs = []
        for program_name in program_names:
            if program_name.lower() in title.lower():
                programs.append(program_name)
                
        # If programs list is empty, add "N/A" to it
        if not programs:
            programs.append("N/A")

        # Extract affiliation
        affiliation = soup.find("strong", text="Affiliation:").find_next_sibling("span").get_text(strip=True)
        
        # Extract education information
        education_tag = soup.find('strong', text='Education:')
        if education_tag and education_tag.next_sibling:
            education_text = education_tag.next_sibling.strip()
        else:
            education_text = "N/A"

        # Extract research areas
        research_areas_tag = soup.find('strong', text='Research Areas:')
        if research_areas_tag and research_areas_tag.next_sibling:
            research_areas_text = research_areas_tag.next_sibling.strip()
        else:
            research_areas_text = "N/A"

        # Extract biography
        bio_hr_tag = soup.find('hr', class_='faculty-sep faculty-bio-sep')
        bio_paragraphs = []
        next_tag = bio_hr_tag.find_next_sibling()
        if next_tag and next_tag.name == 'p':  # Check if biography is enclosed in <p> tags
            while next_tag and next_tag.name == 'p':
                bio_paragraphs.append(next_tag.get_text(strip=True))
                next_tag = next_tag.find_next_sibling()

        bio = ' '.join(bio_paragraphs)
        if len(bio_paragraphs)==0:
            bio="N/A"

        # Write the data to the CSV file
        csvwriter.writerow([name, email, sublink, division, programs, title, affiliation, education_text, research_areas_text, bio, image_url])

print("Data written to faculty.csv successfully.")
