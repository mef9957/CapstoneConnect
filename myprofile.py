#!/usr/bin/python3

import cgi
# Get the form data from the CGI environment
form = cgi.FieldStorage()
encodedemail = form.getvalue('email') # Get the value of the 'email' field from the form

# Open the 'student_database.txt' file in read mode
with open('student_database.txt', 'r') as file:
   for line in file:
      parts = line.strip().split(':')
      if parts[0] == encodedemail: # Check if the first part (index 0) matches the provided email
         name_user = parts[2] # Assign the name to a variable
         password = parts[1] # Assign the password to a variable

print("Content-Type: text/html\n\n")

# Print the HTML content for the profile page, including dynamic placeholders for email and name
print("""
<!DOCTYPE html>
<html lang="en">

<head>
   <!-- basic -->
   <meta charset="utf-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <!-- mobile metas -->
   <meta name="viewport" content="width=device-width, initial-scale=1">
   <meta name="viewport" content="initial-scale=1, maximum-scale=1">
   <!-- site metas -->
   <title>CapstoneConnect - My Profile</title>
   <meta name="keywords" content="">
   <meta name="description" content="">
   <meta name="author" content="">
   <!-- site icon -->
   <link rel="icon" href="images/fevicon.png" type="image/png" />
   <!-- bootstrap css -->
   <link rel="stylesheet" href="css/bootstrap.min.css" />
   <!-- site css -->
   <link rel="stylesheet" href="style.css" />
   <link rel="stylesheet" href="about-profile.css" />
   <!-- responsive css -->
   <link rel="stylesheet" href="css/responsive.css" />
   <!-- color css -->
   <link rel="stylesheet" href="css/colors.css" />
   <!-- select bootstrap -->
   <link rel="stylesheet" href="css/bootstrap-select.css" />
   <!-- scrollbar css -->
   <link rel="stylesheet" href="css/perfect-scrollbar.css" />
   <!-- custom css -->
   <link rel="stylesheet" href="css/custom.css" />
   <!-- calendar file css -->
   <link rel="stylesheet" href="js/semantic.min.css" />
   <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
      <![endif]-->
</head>

<body class="inner_page profile_page">
   <div class="full_container">
      <div class="inner_container">
         <!-- Sidebar  -->
         <nav id="sidebar">
            <div class="sidebar_blog_1">
               <div class="sidebar-header">
                  <div class="logo_section">
                     <a href="viewmatches.py?email={}"><img class="logo_icon img-responsive" src="images/logo/cclogo.png"
                           alt="#" /></a>
                  </div>
               </div>
               <div class="sidebar_user_info">
                  <div class="icon_setting"></div>
                  <div class="user_profle_side">
                     <div class="user_img"><img class="img-responsive" src="images/layout_img/user_img.jpg"
                           alt="#" />
                     </div>
                     <div class="user_info">
                        <h6>{}</h6>
                        <p><span class="online_animation"></span> Online</p>
                     </div>
                  </div>
               </div>
            </div>
            <div class="sidebar_blog_2">
               <h4>General</h4>
               <ul class="list-unstyled components">
                  <li class="active">
                     <a href="viewmatches.py?email={}"><i class="fa fa-dashboard yellow_color"></i> <span>Dashboard</span></a>
                  </li>
                  <li><a href="about.py?email={}"><i class="fa fa-object-group blue2_color"></i> <span>About</span></a>
                  </li>
                  <li>
                     <a href="myprofile.py?email={}"><i class="fa fa-clone purple_color2"></i> <span>My
                           Profile</span></a>
                  </li>
                  <li><a href="faculty_dir.py?email={}"><i class="fa fa-users green_color"></i> <span>Faculty
                           Directory</span></a>
                  </li>
                  <li>
                     <a href="contact_form.py?email={}">
                        <i class="fa fa-paper-plane red_color"></i> <span>Contact</span></a>
                  </li>
                  <li><a href="login.html"><i class="fa fa-cog yellow_color"></i> <span>Log Out</span></a></li>
               </ul>
            </div>
         </nav>
         <!-- end sidebar -->
         <!-- right content -->
         <div id="content">
            <!-- topbar -->
            <div class="topbar">
               <nav class="navbar navbar-expand-lg navbar-light">
                  <div class="full">
                     <button type="button" id="sidebarCollapse" class="sidebar_toggle"><i
                           class="fa fa-bars"></i></button>
                     <div class="logo_section">
                        <a href="viewmatches.py?email={}"><img class="img-responsive" src="images/logo/cclogowhite.png"
                              alt="#" /></a>
                     </div>

                  </div>
               </nav>
      """.format(encodedemail,name_user,encodedemail,encodedemail,encodedemail,encodedemail,encodedemail,encodedemail))

print("""
            </div>
            <!-- end topbar -->
            <!-- dashboard inner -->
            <div class="midde_cont">
               <div class="container-fluid">
                  <div class="row column_title">
                     <div class="col-md-12">
                        <div class="page_title">
                           <h2>Update Profile</h2>
                        </div>
                     </div>
                  </div>
                  <!-- row -->
                  <div class="row column1">
                     <div class="col-md-2"></div>
                     <div class="col-md-8">
                        <div class="white_shd full margin_bottom_30">
                           <div class="full graph_head">
                              <div class="heading1 margin_0">
                                 <h2>My Interests</h2>
                              </div>
                           </div>
                           <div class="full price_table padding_infor_info">
                              <div class="row">
                                 <!-- user profile section -->
                                 <!-- profile image -->
                                 <div class="col-lg-12">
                                    <div class="full dis_flex center_text">
                                       <!-- <div class="profile_img"><img width="180" class="rounded-circle" src="images/layout_img/user_img.jpg" alt="#" /></div> -->
                                       <div class="profile_contant">
                                          <div class="contact_inner">
                                             <h3></h3>
                                          </div>

                                          <div class="interest_form">
                                             <form action="update_profile.py" method="post">
                                                <fieldset>
                                                   <div class="field">
                                                      <label class="label_field">Full Name</label>
                                                      <select name="name">
                                                         <option value="{}">{}
                                                         </option>
                                                      </select>
                                                   </div>
                                                   <div class="field">
                                                      <label class="label_field">Email Address</label>
                                                      <select name="email">
                                                         <option value="{}">{}
                                                         </option>
                                                      </select>
                                                   </div>
      <div class="field">
                                                      <label class="label_field">Password</label>
                                                      <select name="password">
                                                         <option value="{}">{}
                                                         </option>
                                                      </select>
                                                   </div>
      """.format(name_user,name_user,encodedemail,encodedemail,password,password))


# Print the HTML content for the form fields including department, major, research interests, skills, number of semesters, advisor's affiliation, and update button
print("""
                                                   <div class="field">
                                                      <label class="label_field">Department</label>
                                                      <select name="department">
                                                         <option value="arts and humanities">Arts and Humanities
                                                         </option>
                                                         <option value="engineering">Engineering</option>
                                                         <option value="science">Science</option>
                                                         <option value="social science">Social Science</option>
                                                      </select>
                                                   </div>
                                                   <div class="field">
                                                      <label class="label_field">Major</label>
                                                      <select name="major">
                                                         <option value="african-studies">African Studies</option>
                                                         <option value="ancient-world">Ancient World</option>
                                                         <option value="anthropology">Anthropology</option>
                                                         <option value="arab-crossroads-studies">Arab Crossroads Studies</option>
                                                         <option value="arabic">Arabic</option>
                                                         <option value="art-and-art-history">Art and Art History</option>
                                                         <option value="biology">Biology</option>
                                                         <option value="chemistry">Chemistry</option>
                                                         <option value="chinese">Chinese</option>
                                                         <option value="civil-engineering">Civil Engineering</option>
                                                         <option value="computer-engineering">Computer Engineering</option>
                                                         <option value="computer-science">Computer Science</option>
                                                         <option value="design">Design</option>
                                                         <option value="economics">Economics</option>
                                                         <option value="electrical-engineering">Electrical Engineering</option>
                                                         <option value="environmental-studies">Environmental Studies</option>
                                                         <option value="film-and-new-media">Film and New Media</option>
                                                         <option value="french">French</option>
                                                         <option value="general-engineering">General Engineering</option>
                                                         <option value="history">History</option>
                                                         <option value="interactive-media">Interactive Media</option>
                                                         <option value="legal-studies">Legal Studies</option>
                                                         <option value="literature-and-creative-writing">Literature and Creative Writing</option>
                                                         <option value="mathematics">Mathematics</option>
                                                         <option value="mechanical-engineering">Mechanical Engineering</option>
                                                         <option value="music">Music</option>
                                                         <option value="philosophy">Philosophy</option>
                                                         <option value="physics">Physics</option>
                                                         <option value="political-science">Political Science</option>
                                                         <option value="psychology">Psychology</option>
                                                         <option value="social-research-and-public-policy">Social Research and Public Policy
                                                         </option>
                                                         <option value="theater">Theater</option>
                                                      </select>
                                                   </div>
                                                   <div class="field">
                                                      <label class="label_field">Research Interests (Select
                                                         Multiple)</label>
                                                         <select name="r-interests" multiple>
                                                            <option value="african-diaspora-studies">African Diaspora Studies</option>
                                                            <option value="african-studies">African Studies</option>
                                                            <option value="behavioral-economics">Behavioral Economics</option>
                                                            <option value="biological-sciences">Biological Sciences</option>
                                                            <option value="biomedical-engineering">Biomedical Engineering</option>
                                                            <option value="biochemistry-and-molecular-biology">Biochemistry and Molecular Biology
                                                            </option>
                                                            <option value="chemical-genetics-and-evolutionary-biology">Chemical Genetics and
                                                               Evolutionary Biology</option>
                                                            <option value="community-development">Community Development</option>
                                                            <option value="comparative-religious-studies">Comparative Religious Studies</option>
                                                            <option value="computational-geometry-and-algorithms">Computational Geometry and
                                                               Algorithms</option>
                                                            <option value="computational-social-sciences">Computational Social Sciences</option>
                                                            <option value="corporate-identity-and-branding-strategies">Corporate Identity and Branding
                                                               Strategies</option>
                                                            <option value="criminology-and-deviance-studies">Criminology and Deviance Studies</option>
                                                            <option value="cultural-heritage-preservation">Cultural Heritage Preservation</option>
                                                            <option value="cultural-representations-and-orientalism">Cultural Representations and
                                                               Orientalism</option>
                                                            <option value="data-science-and-analytics">Data Science and Analytics</option>
                                                            <option value="developmental-biology">Developmental Biology</option>
                                                            <option value="drug-development-and-pharmacology">Drug Development and Pharmacology
                                                            </option>
                                                            <option value="earth-and-environmental-sciences">Earth and Environmental Sciences</option>
                                                            <option value="economic-development-and-poverty-reduction">Economic Development and
                                                               Poverty Reduction</option>
                                                            <option value="education-and-pedagogy">Education and Pedagogy</option>
                                                            <option value="employment-trends">Employment Trends</option>
                                                            <option value="energy-policy-and-renewable-technologies">Energy Policy and Renewable
                                                               Technologies</option>
                                                            <option value="entrepreneurship-and-innovation">Entrepreneurship and Innovation</option>
                                                            <option value="environmental-engineering">Environmental Engineering</option>
                                                            <option value="environmental-sustainability-and-conservation">Environmental Sustainability
                                                               and Conservation</option>
                                                            <option value="evolutionary-genetics">Evolutionary Genetics</option>
                                                            <option value="fine-arts-and-visual-culture">Fine Arts and Visual Culture</option>
                                                            <option value="feminist-theory-and-gender-equality">Feminist Theory and Gender Equality
                                                            </option>
                                                            <option value="game-theory-and-decision-science">Game Theory and Decision Science</option>
                                                            <option value="gender-and-identity-studies">Gender and Identity Studies</option>
                                                            <option value="gender-studies-and-sexual-health">Gender Studies and Sexual Health</option>
                                                            <option value="genetics-and-genomics">Genetics and Genomics</option>
                                                            <option value="genomics-and-microbiome-research">Genomics and Microbiome Research</option>
                                                            <option value="global-literary-heritage">Global Literary Heritage</option>
                                                            <option value="global-studies">Global Studies</option>
                                                            <option value="human-behavior-and-social-networks">Human Behavior and Social Networks
                                                            </option>
                                                            <option value="human-computer-interaction">Human-Computer Interaction</option>
                                                            <option value="humanitarian-studies-and-refugee-crisis">Humanitarian Studies and Refugee
                                                               Crisis</option>
                                                            <option value="information-sciences">Information Sciences</option>
                                                            <option value="interface-science-and-materials-chemistry">Interface Science and Materials
                                                               Chemistry</option>
                                                            <option value="international-law-and-governance">International Law and Governance</option>
                                                            <option value="international-trade-policies">International Trade Policies</option>
                                                            <option value="labor-and-workforce-studies">Labor and Workforce Studies</option>
                                                            <option value="labor-market-economics">Labor Market Economics</option>
                                                            <option value="language-processing-and-computational-linguistics">Language Processing and
                                                               Computational Linguistics</option>
                                                            <option value="language-teaching-and-acquisition">Language Teaching and Acquisition
                                                            </option>
                                                            <option value="law-and-society">Law and Society</option>
                                                            <option value="legislative-studies-and-policy-analysis">Legislative Studies and Policy
                                                               Analysis</option>
                                                            <option value="legislative-systems-and-political-methodologies">Legislative Systems and
                                                               Political Methodologies</option>
                                                            <option value="linguistics-and-language-studies">Linguistics and Language Studies</option>
                                                            <option value="literary-and-cultural-travel-writing">Literary and Cultural Travel Writing
                                                            </option>
                                                            <option value="literary-studies">Literary Studies</option>
                                                            <option value="macroeconomic-analysis">Macroeconomic Analysis</option>
                                                            <option value="macroeconomic-modeling-and-forecasting">Macroeconomic Modeling and
                                                               Forecasting</option>
                                                            <option value="machine-intelligence">Machine Intelligence</option>
                                                            <option value="marine-studies">Marine Studies</option>
                                                            <option value="mathematics">Mathematics</option>
                                                            <option value="medical-technology-and-devices">Medical Technology and Devices</option>
                                                            <option value="metabolism-and-physiology">Metabolism and Physiology</option>
                                                            <option value="metaphysics-and-ontology">Metaphysics and Ontology</option>
                                                            <option value="migration-and-diaspora-research">Migration and Diaspora Research</option>
                                                            <option value="middle-east-studies">Middle East Studies</option>
                                                            <option value="music-and-cultural-studies">Music and Cultural Studies</option>
                                                            <option value="nanotechnology-and-biomedical-engineering">Nanotechnology and Biomedical
                                                               Engineering</option>
                                                            <option value="neural-imaging-and-brain-mapping">Neural Imaging and Brain Mapping</option>
                                                            <option value="neuroscience-and-brain-engineering">Neuroscience and Brain Engineering
                                                            </option>
                                                            <option value="network-science-and-graph-theory">Network Science and Graph Theory</option>
                                                            <option value="performance-studies">Performance Studies</option>
                                                            <option value="philosophy-and-ethics">Philosophy and Ethics</option>
                                                            <option value="pharmaceutical-sciences">Pharmaceutical Sciences</option>
                                                            <option value="physics-and-its-philosophical-implications">Physics and its Philosophical
                                                               Implications</option>
                                                            <option value="political-theory-and-ideologies">Political Theory and Ideologies</option>
                                                            <option value="population-genetics">Population Genetics</option>
                                                            <option value="postcolonial-and-decolonial-perspectives">Postcolonial and Decolonial
                                                               Perspectives</option>
                                                            <option value="probabilistic-modeling-and-statistical-analysis">Probabilistic Modeling and
                                                               Statistical Analysis</option>
                                                            <option value="public-health-and-epidemiology">Public Health and Epidemiology</option>
                                                            <option value="quantum-technologies">Quantum Technologies</option>
                                                            <option value="race,-ethnicity,-and-identity">Race, Ethnicity, and Identity</option>
                                                            <option value="reproductive-health-and-biology">Reproductive Health and Biology</option>
                                                            <option value="remote-sensing-technologies">Remote Sensing Technologies</option>
                                                            <option value="social-neuroscience">Social Neuroscience</option>
                                                            <option value="social-psychology-and-altruism">Social Psychology and Altruism</option>
                                                            <option value="soft-matter-physics-and-material-sciences">Soft Matter Physics and Material
                                                               Sciences</option>
                                                            <option value="stem-cell-research">Stem Cell Research</option>
                                                            <option value="sustainable-development">Sustainable Development</option>
                                                            <option value="sustainable-urban-development">Sustainable Urban Development</option>
                                                            <option value="systems-biology-and-bioinformatics">Systems Biology and Bioinformatics
                                                            </option>
                                                            <option value="urban-design-and-architecture">Urban Design and Architecture</option>
                                                            <option value="urban-planning-and-traffic-management">Urban Planning and Traffic
                                                               Management</option>
                                                            <option value="virtual-reality-and-augmented-reality">Virtual Reality and Augmented
                                                               Reality</option>
                                                            <option value="visual-arts-and-media-studies">Visual Arts and Media Studies</option>
                                                            <option value="world-history">World History</option>
                                                         </select>
                                                   </div>
                                                   <div class="field">
                                                      <label class="label_field">Relevant Skills</label>
                                                      <input type="text" name="skills" />
                                                   </div>
                                                   <div class="field">
                                                      <label class="label_field">Preferred Number of Semesters</label>
                                                      <select name="num-semesters">
                                                         <option value="1">1 semester</option>
                                                         <option value="2">2 semesters</option>
                                                      </select>
                                                   </div>
                                                   <div class="field">
                                                      <label class="label_field">Preferred Advisor's Affiliation</label>
                                                      <select name="affiliation">
                                                         <option value="NYU Abu Dhabi">NYU Abu Dhabi</option>
                                                         <option value="NYU New York">NYU New York</option>
                                                         <option value="Visiting">Visiting</option>
                                                      </select>
                                                   </div>
                                                   <div class="field margin_0">
                                                      <label class="label_field hidden">hidden label</label>
                                                      <button class="main_bt_profile">Update</button>
                                                   </div>
                                                </fieldset>
                                             </form>
                                          </div>
                                       </div>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>
                     <div class="col-md-2"></div>
                  </div>
                  <!-- end row -->
               </div>
            </div>
            <!-- end dashboard inner -->
         </div>
         <!-- end right content -->
      </div>
   </div>
   <!-- jQuery -->
   <script src="js/jquery.min.js"></script>
   <script src="js/popper.min.js"></script>
   <script src="js/bootstrap.min.js"></script>
   <!-- wow animation -->
   <script src="js/animate.js"></script>
   <!-- select country -->
   <script src="js/bootstrap-select.js"></script>
   <!-- nice scrollbar -->
   <script src="js/perfect-scrollbar.min.js"></script>
   <!-- custom js -->
   <script src="js/custom.js"></script>
   <script>
      document.addEventListener('DOMContentLoaded', function () {
         var select = document.getElementById('multiSelect');
         select.addEventListener('click', function (event) {
            var option = event.target;
            if (option.tagName === 'OPTION') {
               option.selected = !option.selected; // Toggle selection
               option.classList.toggle('selected'); // Toggle the 'selected' class for styling
               event.preventDefault(); // Prevent default to allow for multiple selection without Command key
            }
         });

      });
   </script>
</body>

</html>

""")