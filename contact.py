#!/usr/bin/python
# -*- coding: utf-8 -*-

# Print HTTP header specifying content type as HTML
print("Content-type:text/html\n\n")

# Import CGI module for handling form data
import cgi

# Parse form data
form = cgi.FieldStorage() 

# Get data from form fields
name = form.getvalue('name')
email = form.getvalue('email')
subject = form.getvalue('subject')
message = form.getvalue('message')

# Print the beginning of the HTML document
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
    <title>CapstoneConnect - Form Submitted</title>
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
""")

# Print the rest of the HTML document, including the body content and JavaScript imports
print("""
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
                <!-- end topbar -->
                <div class="container-fluid">
                    <div class="row column_title">
                        <div class="col-md-12">
                            <div class="page_title">
                                <h2>Thank you for reaching out to us.</h2>
                            </div>
                        </div>
                    </div>
                    <!-- row -->
                    <!-- testimonial -->

                    <!-- end testimonial -->

                    <div class="row column1">
                        <div class="col-md-2"></div>
                        <div class="col-md-8">
                            <div class="white_shd full margin_bottom_30">
                                <div class="full graph_head">
                                    <div class="heading1 margin_0">
                                        <h2>Your Submission</h2>
                                    </div>
                                </div>
                                <div class="full graph_head">
                                    <div class="heading1 margin_0">
                                        <p><strong>Name:</strong> {}</p>
                                        <p><strong>Email:</strong> {}</p>
                                        <p><strong>Subject:</strong> {}</p>
                                        <p><strong>Message:</strong> {}</p>
                                    </div>
                                </div>
                            </div>
                        </div>
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
                <!-- end dashboard inner -->
            </div>
        </div>
    </div>
""".format(email,name,email,email,email,email,email,email,name, email, subject, message))

print("""
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
""")