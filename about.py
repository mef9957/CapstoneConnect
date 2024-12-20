#!/usr/bin/python

# Import the CGI module
import cgi

# Parse the form data
form = cgi.FieldStorage()

# Get the value of the 'email' field from the form
encodedemail = form.getvalue('email')

# Open the student database file
with open('student_database.txt', 'r') as file:
   for line in file:
      parts = line.strip().split(':')  # Check if the first part of the line matches the encoded email
      if parts[0] == encodedemail:
          # If a match is found, store the user's name
         name_user = parts[2]

print("Content-Type: text/html\n\n")

# Print the beginning of the HTML document, including the head section and initial body content
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
   <title>CapstoneConnect - About</title>
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
   <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
      <![endif]-->
</head>

<body class="dashboard dashboard_1">
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
      """.format(encodedemail,name_user,encodedemail,encodedemail,encodedemail,encodedemail,encodedemail))

# Print the content after the sidebar
print("""
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
            <!-- dashboard inner -->
            <div class="midde_cont">
               <div class="container-fluid">
                  <div class="row column_title">
                     <div class="col-md-12">
                        <div class="page_title">
                           <h2>About Us</h2>
                        </div>
                     </div>
                  </div>
""".format(encodedemail))

# Print the content after the title
print("""
<div class="row column1">
                     <div class="col-md-2"></div>
                     <div class="col-md-8">
                        <div class="white_shd full margin_bottom_30">
                           <div class="full graph_head">
                              <div class="heading1 margin_0">
                                 <h2>CapstoneConnect</h2>
                              </div>
                           </div>
                           <div class="full graph_head">
                              <div class="heading1 margin_0">
                                 CapstoneConnect tackles the challenge many senior college students face in finding
                                 suitable academic mentors. Traditional methods, which often involve lengthy and
                                 cumbersome research, are replaced by our efficient, user-friendly web application. By
                                 leveraging a robust database of professor profiles and student preferences,
                                 CapstoneConnect simplifies the process of connecting students with mentors who align
                                 with their academic interests and career goals. Our mission is to facilitate accessible
                                 and meaningful mentorships that enrich the educational experience for both students and
                                 professors. Join CapstoneConnect today and discover a more straightforward path to
                                 academic collaboration and success.
                              </div>
                           </div>
                        </div>
                        <div class="col-md-12">
                           <div class="dark_bg full margin_bottom_30">
                              <div class="full graph_head">
                                 <div class="heading1 margin_0">
                                    <h2>Testimonials</h2>
                                 </div>
                              </div>
                              <div class="full graph_revenue">
                                 <div class="row">
                                    <div class="col-md-12">
                                       <div class="content testimonial">
                                          <div id="testimonial_slider" class="carousel slide" data-ride="carousel">
                                             <!-- Wrapper for carousel items -->
                                             <div class="carousel-inner">
                                                <div class="item carousel-item active">
                                                   <div class="img-box"><img src="images/layout_img/msg3.png" alt="">
                                                   </div>
                                                   <p class="testimonial">CapstoneConnect made mentorship simple. I
                                                      found a perfect match for my capstone project within seconds.
                                                      Thanks to them, I excelled and gained valuable insights for my
                                                      future career.</p>
                                                   <p class="overview"><b>Miguel Ramirez</b>Chemistry Major</p>
                                                </div>
                                                <div class="item carousel-item">
                                                   <div class="img-box"><img src="images/layout_img/msg1.png" alt="">
                                                   </div>
                                                   <p class="testimonial">CapstoneConnect surpassed my expectations.
                                                      Their diverse database ensured I found a mentor who understood my
                                                      interdisciplinary approach and I explored new research avenues.
                                                      CapstoneConnect is essential for any senior seeking mentorship.
                                                   </p>
                                                   <p class="overview"><b>Emily Chen</b>Psychology Major</p>
                                                </div>
                                                <div class="item carousel-item">
                                                   <div class="img-box"><img src="images/layout_img/msg4.png" alt="">
                                                   </div>
                                                   <p class="testimonial">As a first-gen student, CapstoneConnect was a
                                                      lifesaver. It took the stress out of finding a mentor. With their
                                                      intuitive platform, I connected with someone who not only helped
                                                      with my project but also guided my post-graduation plans.</p>
                                                   <p class="overview"><b>Jonathan Martinez</b>Electrical Engineering
                                                      Major</p>
                                                </div>
                                             </div>
                                             <!-- Carousel controls -->
                                             <a class="carousel-control left carousel-control-prev"
                                                href="#testimonial_slider" data-slide="prev">
                                                <i class="fa fa-angle-left"></i>
                                             </a>
                                             <a class="carousel-control right carousel-control-next"
                                                href="#testimonial_slider" data-slide="next">
                                                <i class="fa fa-angle-right"></i>
                                             </a>
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
""")

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
