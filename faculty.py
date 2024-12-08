# Program to get code based on the faculty present in CSV file scrapped from web

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('faculty.csv')

# Display the DataFrame (optional)
print(df)

with open('output.txt', 'w') as file:

    # Accessing individual elements in the DataFrame
    for index, row in df.iterrows():
        name = row['Name']
        email = row['Email']
        sublink = row['Sublink']
        division = row['Divison']
        division = division.title()
        program = row['Program']
        program = program.replace('"', '').replace('[', '').replace(']', '').replace("'",'')
        title = row['Title']
        affiliation = row['Affiliation']
        education = row['Education']
        research_areas = row['Research Areas']
        bio = row['Bio']
        image_url = row['ImageUrl']
        filename = image_url.split('/')[-1]
        image_src = "downloaded_images/"+filename
        
        # You can process or print each element here as needed
        # Writing each element to the text file
        file.write("""
                   <div class="col-lg-4 col-md-6 col-sm-6 col-xs-12 profile_details margin_bottom_30">
                        <div class="contact_blog">
                            <div class="contact_inner">
                                <div class="left">
                                <h3>{}</h3>
                                <ul class="list-unstyled">
                                    <li><i class="fa fa-envelope-o"></i> : {}</li>
                                    <li><i class="fa fa-university"></i> : {}</li>
                                    <li><i class="fa fa-users"></i> : {}</li>
                                </ul>
                                </div>
                                <div class="right">
                                <div class="profile_contacts">
                                    <img class="img-responsive" src="{}" alt="#" />
                                </div>
                                </div>
                                <div class="bottom_list">
                                <div class="left_rating">
                                    <p class="ratings">
                                    {}
                                    </p>
                                </div>
                                <div class="right_button">
                                    <button type="button" class="btn btn-primary btn-xs">
                                    <i class="fa fa-user"> </i> <a href="faculty_view.py?input1={}" style="color: #fff;">View Profile</a> 
                                    </button>
                                </div>
                                </div>
                            </div>
                        </div>
                    </div>
                   """.format(name, email, division, program, image_src, affiliation, name))
        file.write("\n")

file.close()
    
