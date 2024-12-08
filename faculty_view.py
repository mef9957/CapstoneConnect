#!/usr/bin/python
# -*- coding: utf-8 -*-
print("Content-Type: text/html\n")

import pandas as pd
import cgi

# Parse query parameters
form = cgi.FieldStorage()
input1 = form.getvalue('input1')
emailencoded = form.getvalue('input2')
input1=input1.replace("%20",' ')

with open('student_database.txt', 'r') as file:
   for line in file:
      parts = line.strip().split(':')
      if parts[0] == emailencoded:
         name_user = parts[2]

# Read the CSV file into a DataFrame
df = pd.read_csv('faculty.csv')

for index, row in df.iterrows():
    name = row['Name']
    if input1==name:
        name1 = row['Name']
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

#Generates a webpage displaying a faculty profile with navigation, profile content, and footer
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
            <title>CapstoneConnect - Faculty Profile</title>
            <meta name="keywords" content="">
            <meta name="description" content="">
            <meta name="author" content="">
            <!-- site icon -->
            <link rel="icon" href="images/fevicon.png" type="image/png" />
            <!-- bootstrap css -->
            <link rel="stylesheet" href="css/bootstrap.min.css" />
            <!-- site css -->
            <link rel="stylesheet" href="style.css" />
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
                     <div class="user_img"><img class="img-responsive" src="images/layout_img/user_img.jpg" alt="#" />
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
                     <a href="myprofile.py?email={}"><i class="fa fa-clone purple_color2"></i> <span>My Profile</span></a>
                  </li>
                  <li><a href="faculty_dir.py?email={}"><i class="fa fa-users green_color"></i> <span>Faculty Directory</span></a>
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
            </div>
      """.format(emailencoded,name_user,emailencoded,emailencoded,emailencoded,emailencoded,emailencoded,emailencoded))
print("""
            <!-- end topbar -->
                    <!-- dashboard inner -->
                    <div class="midde_cont">
                        <div class="container-fluid">
                            <div class="row column_title">
                                <div class="col-md-12">
                                <div class="page_title">
                                    <h2>Profile</h2>
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
                                            <h2>Faculty profile</h2>
                                        </div>
                                    </div>
                                    <div class="full price_table padding_infor_info">
                                        <div class="row">
                                            <!-- user profile section --> 
                                            <!-- profile image -->
                                            <div class="col-lg-12">
                                            <div class="full dis_flex center_text">
                                                <div class="profile_img"><img width="180" class="rounded-circle" src="{}" alt="#" /></div>
                                                <div class="profile_contant">
                                                    <div class="contact_inner">
                                                        <h3>{}</h3>
                                                        <p><strong>Title: </strong>{}</p>
                                                        <ul class="list-unstyled">
                                                        <li><i class="fa fa-envelope-o"></i> : {}</li>
                                                        <li><i class="fa fa-university"></i> : {}</li>
                                                        <li><i class="fa fa-users"></i> : {}</li>
                                                        </ul>
                                                    </div>
                                                </div>
                                            </div>
                                            <!-- profile contant section -->
                                            <div class="full inner_elements margin_top_30">
                                                <div class="tab_style2">
                                                    <div class="tabbar">
                                                        <nav>
                                                        <div class="nav nav-tabs" id="nav-tab" role="tablist">
                                                            <a class="nav-item nav-link active" id="nav-home-tab" data-toggle="tab" href="#recent_activity" role="tab" aria-selected="true">Research Interests</a>
                                                            <a class="nav-item nav-link" id="nav-profile-tab" data-toggle="tab" href="#project_worked" role="tab" aria-selected="false">Faculty Bio</a>
                                                        </div>
                                                        </nav>
                                                        <div class="tab-content" id="nav-tabContent">
                                                        <div class="tab-pane fade show active" id="recent_activity" role="tabpanel" aria-labelledby="nav-home-tab">
                                                            <div class="msg_list_main">
                                                                <ul class="msg_list">
                                                                    <li>
                                                                    Education: {}
                                                                    </li>
                                                                    <li>
                                                                    Research Interests: {}
                                                                    </li>
                                                                </ul>
                                                            </div>
                                                        </div>
                                                        <div class="tab-pane fade" id="project_worked" role="tabpanel" aria-labelledby="nav-profile-tab">
                                                            <p>{}
                                                            </p>
                                                        </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <!-- end user profile section -->
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-2"></div>
                                </div>
                                <!-- end row -->
                            </div>
                            <!-- footer -->
                            <div class="container-fluid">
                                <div class="footer">
                                <p>Copyright © 2024 Designed by CapstoneConnect. All rights reserved.<br><br>
                           Theme By: <a href="https://themewagon.com/">ThemeWagon</a>
                        </p>
                                </div>
                            </div>
                        </div>
                        <!-- end dashboard inner -->
                    </div>
                    </div>
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
            <!-- owl carousel -->
            <script src="js/owl.carousel.js"></script> 
            <!-- chart js -->
            <script src="js/Chart.min.js"></script>
            <script src="js/Chart.bundle.min.js"></script>
            <script src="js/utils.js"></script>
            <script src="js/analyser.js"></script>
            <!-- nice scrollbar -->
            <script src="js/perfect-scrollbar.min.js"></script>
            <script>
                var ps = new PerfectScrollbar('#sidebar');
            </script>
            <!-- custom js -->
            <script src="js/custom.js"></script>
            <!-- calendar file css -->    
            <script src="js/semantic.min.js"></script>
        </body>
        </html>
      """.format(image_src, name1, title, email, division, program, education, research_areas, bio))
