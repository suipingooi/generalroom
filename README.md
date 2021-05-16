## Code Institute Milestone Project 4 - Fullstack Frameworks with Django

### General Room | Co-Working Space

The goal of this project is to demonstrate the potential of what a fullstack development can offer for The General Room; 
with current focus and features limited to CRM database and some e-commerce functions.

The targetted main users of this site are:
1. (owner) TGR management for the following:
    1. track that all client requests are attended to by staffs
    2. automate current manual processes.
2. TGR staffs / client service administrators for the following actions:
    1. add, update, or remove products following the fluid nature of the business and promotional items. 
    2. manage and followup on client requests efficiently and effectively with less paperwork.
    3. follow up on transacted trails.
3. Clients and general public / new clients:
    1. learn more about TGR and its offering.
    2. on-line payment for products esp. for repeat customers.

<hr>

#### The General Room (TGR) - Background
![TGR](static/assets/readme/header_logo_main.png) <br>
We are a boutique coworking space with a mission of providing stylish, modern and no-frills environment to help businesses get things done. 
We are conveniently located in Orchard and Somerset with sophisticated and well equipped business meeting rooms for your needs.

TGR is also available for short term rentals.

### UX - User Experience

Wireframe of the build design includes:

![Wireframe](static/assets/readme/tgrlgbwire.jpeg)

<hr>

![Color Chart](static/assets/readme/tn_colors/tgrcolorchart.png)<br>


<img src="static/assets/readme/tn_colors/black.png" alt="black" width="20px"> Black: symbolizes elegance and sophistication. <br>
<img src="static/assets/readme/tn_colors/498c86.png" alt="#498c86" width="20px"> Teal: represents a calm, open, transparent relationship and dignified business dealings.<br> 
<img src="static/assets/readme/tn_colors/6d758c.png" alt="#6d758c" width="20px"> 
<img src="static/assets/readme/tn_colors/72788c.png" alt="#72788c" width="20px"> Shades of Gray: representing a stern and uncompromising nature; a General.<br>
<img src="static/assets/readme/tn_colors/030abc.png" alt="#030abc" width="20px"> 
<img src="static/assets/readme/tn_colors/393c73.png" alt="#393c73" width="20px"> 
<img src="static/assets/readme/tn_colors/565aa6.png" alt="#565aa6" width="20px"> Shades of Blue: associated with blue blooded nobility and aristrocractic birth.<br>




![Font Glyphs](static/assets/readme/fontglyph_tgrlgb.png)<br>

Colors & Font families for UI/UX is inherited and consistent with TGR's brand image, values and identity: 
personifying a blue blooded, accomplished and stately military General, highly decorated with badges of honour.

<hr>

A demo of the site can be found here [tgrlgbdemo](tgrlgbdemo.herokuapp.com)
1. Login as general user: <br>
    username: user <br>
    password: user1234 <br>
    <br>
2. Login as admin / staff: <br>
    username: admin <br>
    password: admin1234

![ERD]()<br>

<hr>

## Built With 
### Technologies
1. HTML 5.0 + CSS
2. Bootstrap 5.0 - CSS & JS [https://getbootstrap.com/](https://getbootstrap.com/)
3. Python + Django
4. JQuery 
5. Toastr [https://codeseven.github.io/toastr/](https://codeseven.github.io/toastr/)
6. Uploadcare [https://uploadcare.com/](https://uploadcare.com/)
7. Heroku [https://www.heroku.com/](https://www.heroku.com/) as deployment host.


### Styling
1. Google Fonts [https://fonts.google.com/](https://fonts.google.com/) for font-family pairings.
2. Fontawesome [https://fontawesome.com/](https://fontawesome.com/) for icons.
3. Gimp 2.10 [https://www.gimp.org/](https://www.gimp.org/) for image manipulation.
4. Adobe Color [https://color.adobe.com/](https://color.adobe.com/) to extract TGR base color chart.


### Testing
[W3C Validator](https://validator.w3.org/) for html validation. All errors dealt with save for Jinja templating errors/ warnings. Specifically uploadcare input.

[Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) for css validation. no errors found.

<hr>

| Action (development testing)             | Results                       | Status      |
| -----------------------------------------|:-----------------------------:|-------------|
| Submission of empty forms                | Unable to submit as expected  | COMPLETED   |
| Submission of invalid data in forms      | Alert and error trigger fixed | COMPLETED   |
| Loading in Chrome                        | Margin issues noted, fixed    | COMPLETED   |                         
| Loading in Firefox                       | Time widget not supported     |    nil      |
| Trolley add & stripe checkout            | Webhook issues fixed          | COMPLETED   |         
| Rezising of viewport widths              | Flexbox issues fixed          | COMPLETED   |
| Checkout / Client request autogen emails | message string issue fixed    | COMPLETED   |

| <h3>**User Features Tests during development**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Test 1: Hyperlinks of navigation tabs / hamburger dropdowns with multiple screen size.**                                                                                                                                                                                                          |
| **Expected:** 1. Navbar brings me to different specified pages. 2. Navbar turns to hamburger dropdown when screensize drops. <br> **Test:** Clicking on all different links to reload multiple times. <br/>**Result:** Multiple issues with some images noted; margins and flex issues noted; navigation controls works as expected.<br/>                                                                                                                                                           |
| **Test 2: Admin console navigation and functions**                                                                                                                                                                                                          |
| **Expected:** 1. on button click brings me to desired pages for CRUD actions where available <br/>**Test:** Clicking on all different buttons to reload table or forms multiple times. <br/>**Result:** page loads and reloads as expected<br/>                                                                                                                                                           |
| **Test 3: Admin CRUD**
| **Expected:** create reflected immediately in read; update forms display values to be edited; delete warning prior to action. form validation and error triggers for invalid data  <br/>**Test:** added new pricing to price list, added new space product to space listing; attempted invalid data submission, edited the info in each entry; deleted the entry<br/>**Result:** multiple issues with display size and margins esp. for smaller viewport width<br/>
| **Test 4: Authentication**                                                                                                                                                                                                          |
| **Expected:** all links and follow-on on screen instructions loads and responds to user. <br> **Test:** Clicking on all different links to sign-up, sign-in, forget password, change password multiple times following on screen instructions  <br>**Results:** all responds as expected except for sign-in link on password changed page that does not respond. Fixed path.                                                                                                                                                             |
| **Test 5: Trolley and Checkout**                                                                                                                                                                                                          |
| **Expected:** items to be able to add, price automatically adjusted; successful stripe payment triggers 1. transacted data storage 2. email notification to admin and client confirmation email. <br> **Test:** add item to trolley, proceed with stripe payment testing  <br>**Results:** multiple failed attempts. found error in port set to private. Fixed.                                                                                                                                            |
| **Test 6: Emails**                                                                                                                                                                                                          |
| **Expected:** receive email with confirmation of payment made <br> **Test:** add items to trolley, stripe checkout  <br>**Results:** email received as expected when stripe is successful and port setting is correct.                                                                                                                                            |
<hr>

**User Features Testing (HEROKU Deployment)** <br>
[Heroku Deployment User Tests detailed documentation](static/assets/readme/tgrlgb_UserTesting.pdf)

<hr>

## Features
### Existing Features
1. 
2. 
3. 


### Features left to Implement
1. 
2. 
3. 


## Deployment
Steps taken to deploy on HEROKU: <br>
1. Created account on Heroku.com and verified details /emails.
2. Logged into Heroku via bash
3. Created heroku app.
4. Checked git remote to confirm repo connection.
5. Installed gunicorn package dependency.
6. Created Procfile for heroku with web gunicorn
7. Created requirements.txt
8. Git add, commit and push to origin (as heroku prep) followed by git push heroku for app build.
9. Set config vars on heroku.
10. Test deployment.


## Acknowledgements

### References
1. [https://docs.djangoproject.com/en/3.0/ref/models/fields/](https://docs.djangoproject.com/en/3.0/ref/models/fields/)
2. [https://www.geeksforgeeks.org/datetimefield-django-forms/](https://www.geeksforgeeks.org/datetimefield-django-forms/)
3. [https://docs.djangoproject.com/en/3.1/ref/forms/widgets/](https://docs.djangoproject.com/en/3.1/ref/forms/widgets/)
4. [https://codepen.io/riyos94/pen/NXgXdp](https://codepen.io/riyos94/pen/NXgXdp)
5. [https://larsmidgaard.no/css-trick-fluid-text-size-with-max-font-size/](https://larsmidgaard.no/css-trick-fluid-text-size-with-max-font-size/)
6. [http://www.learningaboutelectronics.com/Articles/How-to-use-template-filters-in-Django.php](http://www.learningaboutelectronics.com/Articles/How-to-use-template-filters-in-Django.php)
7. [https://dev.to/megazear7/google-calendar-api-integration-made-easy-2a68](https://dev.to/megazear7/google-calendar-api-integration-made-easy-2a68)

### Credits
1. .gitignore from [https://www.toptal.com/developers/gitignore/api/django](https://www.toptal.com/developers/gitignore/api/django)
2. allauth templates adapted from [https://github.com/pennersr/django-allauth/tree/master/allauth/templates](https://github.com/pennersr/django-allauth/tree/master/allauth/templates)
3. Global Trent College mentors: Paul(KunXin) and Ace
4. toastr options form [https://codeseven.github.io/toastr/demo.html](https://codeseven.github.io/toastr/demo.html)
5. google maps [https://google-map-generator.com/](https://google-map-generator.com/)

### Special Thanks
1. Sean Lim, Owner, LGB Group
2. KK Kam, CEO, Wellco Capital
3. Pamela, Administrator, TGR