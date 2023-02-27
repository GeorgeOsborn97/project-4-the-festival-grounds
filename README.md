# The Festival Ground

![full-mockup]()
This site has been designed to be a music based community forum. The general idea of the website was to build a place where anyone and everyone could come togther to discuss and debate any topics surronding music that they would like to. A key goal from the start was for the user to be in complete control over what they build into the site, they have control over the rooms that they create, the conversations they start and the comments they leave.

Find a link to the deployed site [here]()

## contents:
1. [User experience](#user-experience)
   - [what I wanted to achieve](#what-i-wanted-to-achieve)
   - [the road map](#the-road-map)
      1. [User Stories](#user-stories)
      2. [Development Plan](#development-plan)
      3. [Structure](#structure)
      4. [Skeleton](#skeleton)
      5. [Surface](#surface)
2. [Final product](#final-product)
   - [Home Page](#home-page)
   - [About Page](#about-page)
   - [Room View](#room-view)
   - [Your Rooms](#your-rooms)
   - [Register](#register)
   - [Login](#login)
   - [Edit Conversation and Edit Comment](#edit-conversation-and-edit-comment)
3. [Features](#features)
   - [Home Page](#home-page)
      1. [Navigation]()
      2. [Room layout]()
      3. [Room interactivity]()
      4. [Room creation]()
      5. [Pagination]()
   - [About Page](#about-page)
      1. [Website description]()
   - [Room View](#room-view)
      1. [Navigation edited]()
      2. [Conversation and Comment layout]()
      3. [Starting conversations]()
      4. [Adding comments]()
      5. [Edit]()
   - [Your Rooms](#your-rooms)
      1. [Your room layout]()
   - [Register](#register)
      1. [Registration layout]()
      2. [Registration form]()
   - [Login](#login)
      1. [Login layout]()
      2. [Log in form]()
   - [Edit Conversation and Edit Comment](#edit-conversation-and-edit-comment)
      1. [Edit layout]()
      2. [Edit forms]()
4. [Technology that was utilized](#technology-that-was-utilized)   
   - [Languages](#languages)
   - [External assets](#external-assets-utilized)
5. [Testing](#testing)  
   - [Feature testing](#feature-testing)
   - [Device testing](#device-testing)
   - [Validation](#validation)
6. [Deployment](#deployment)
7. [Known Bugs](#known-bugs)
8. [Future Improvments](#future-improvements)
9. [Credits/Acknowledgments](#creditsacknowledgments)
   - [Content](#content)
   - [Media](#media)  
10. [Final thoughts](#final-thoughts)    
___
## User experience:
### What I wanted to achieve:

1. Create community forum style website that was easy to navigate and contribute towards. 
2. Users can register for an account that will allow them to be able to interact with every aspect of the site, if a user is unregstered their interactivity will be very limited.
3. Users can create their own rooms to discuss topics important to them, or join any public room. 
4. Inside a room all members can start conversations to begin a discusion on a certain topic.
5. All members in a room can contribute to any conversation in that room via comments.
6. The creator of a room has the ability to edit and delete any conversation and comment, edit and delete the room itself as well as remove any unwanted members.
7. All members have the ability to edit and delete any conversation they started and any comments they left in any room. 
___
## Development Plan:
### User stories:
- As seen above severel features were identified through the user stories. These were seperated out into varying degrees of necessity, the plan being that those labeled 'Must have' were of key importance, these features were identified as being needed for a MVP (minimum viable product) and should therefore be focused on straight away. Those labeled as 'Should have' were secondary, features that would enhance the user experience and should be implemented if possible, yet are not needed for a deployed product. Then we have 'Could have' features that would be also enhance the user experience but would not impact impact the user if they were not implemented. These features were treated as though they would not make the final deployment until the time came when focus could be put onto them.
- The User stories each contain 2 sections, 'Acceptance Criteria' and 'Tasks'. The acceptance criteria defines the necessary features and processes the user would interact and go though in order to achieve the user story. The tasks define the ways in which I as a developer will put these features and processes into place. When all tasks are complete and all acceptance criteria is met, the user story can be tagged as complete.

___
### Structure:
![The flow chart](assets/roadmap.png)
- The Structure and flow of the site is defined in the flow chart above. It defines the movement of the user through the site and the different paths they can take. This flowchart was done prior to the development process, due to this there are some changes to the flow of the final product and some features such as the request entry to private rooms are not present.
___
#### Database Models:
- This site uses ElephantSQl for the Database managment. There are four models that have been developed for this site, Tags, Rooms, Conversations and Comments. The relationship between these databases can be seen below.
##### Tags:
- tag: tags that the users can add to their rooms upon creation and editing.
##### Rooms:
- title: A unique title for the room defined by its creator.
- creator: A foriegn key of the User model to get the username of the room creator.
- created_on: The date of the rooms creation.
- slug: a unique slugified version of the title.
- cover_image: an image that the user can upload to cloudinary to set at the front of their room.
- description: a brief description of the room provided by the room creator.
- status: an integer field that defines the status of the room as public or private. 
- tags: The room creator can select any of the tags defined in the Tags model.
- members: The users that join the room are added to this field and can be removed by the creator.
##### Conversations:
- room: a foriegn key that defines the room the conversation is started in.
- title: a title for the conversation defined by the creator.
- slug: a slufied version of the conversation title.
- creator: A foriegn key of the User model to get the username of the conversation creator.
- content: the content or 'start' of the conversation defined by the user.
- created_on: the date the conversation was started.
##### Comments:
- room: a foriegn key that defines the room the comment is posted in.
- conversation: a foriegn key that defines the conversation the comment is posted under.
- name: The name of the user that posted the comment.
- body: the content of the comment defined by the user.
- created_on: the date the conversation was started.
___
### Skeleton:
- The wireframes below demonstrate the initial plan for the appearence and layout of the site, as we can see when we compare the wireframes to the final product changes were made to this initial plan, however the basic layout has remained.

___
### Surface:
#### Colour scheme:
- Various colour schemes and styles were tested throughout the development process before landing on the final design. The Colour scheme is purposfully bright and colourful in order to best represent the 'festival feel' that the site aims to give off. The Rotating blurred borders that can be seen in the home and your rooms pages aim to be reminiscent of the bright light shows that occur at festivals and music shows hopefully aiding in the immersion of the user.
#### Style
- The user can see the same style running through the site as a whole, not only does this add to the sites consistency of imagery and colour but also the overall style should help refelect the themes of fun, music and the bright craziness of being at a festival.  

___
## Final Product
Page | Desktop Image | Mobile Image |
--- | --- | --- |
Register | a | b |
Login | a | b |
Logout | a | b |
Home | ![home page](assets/screenshots/home_page.png) | b |
Your Rooms | a | b |
About | a | b |
In Room | a | b |
Edit Conversation | a | b |
Edit Comment | a | b |
___
## Features: 
### General:
* Top Bar: The top bar contains the Logo for the site taht also acts as a button that returns to the home page, as well as a cover image that helps set the tone of the site. 
* Navigation: The Navigation bar incorperates the consistant style of the site, and provides links to all relevent pages. The nav bar changes depending on the authentication of the user, and the page they are currently on.
* Footer: The footer is simple yet mainatins the consistant colour scheme, it holds links to all social pages as well as declering which user is logged on, should it apply.

### User Authentication:
* Registration: Allows the user to register for a free account so they may access the bulk of the sites content.
* Log in: Allows the user to sign in if they have a registered account.
* Sign out: Allows the user to sign out of a registered account.

### Home Page/ Your Rooms:
* The Room Cards: Each card represents a room the user could join.
   - Card Front: The front of the cards show to the user the room title, any tags applied, whether the room is public or private and the cover image set to the room.
   - Card Back: The back of the cards show the description of the room, the creator of the room and how many other users have joined the room. It also has the button join the room if the user wishes. 
* Create a Room: The 'create a room' button opens a side canvas which contains the form for the user to create a new room. 
* Pagination: Each page contains a maximum of 5 room to reduce clutter, the pagination links allow the user to go between the pages and view all the rooms.

### About Page:
* Site description: The Site description is a simple but effective way to introduce a new user to the site and let them know what to expect.

### In Room:
* Conversation List: The conversation list begins as blank and alerts the user that no conversations have been started if the room is new. Once a conversation has started any members of the room can view the thread of the conversation and contribute to the conversation in the form of comments.
   - Add Comments: The 'add comment' opens a side canvas which contains the form for the user to add a new comment to an open conversation.
* Start a conversation: The 'start a conversation' button opens a side canvas which contains the form for the user to start a new converstaion.
* Edit Room: The 'edit room' button opens a side canvas which contains the form for the user to edit the room they are in (This is only available for the room creator). 
* Edit Conversation / Comments: These two edit buttons redirect the user to an edit page in order to edit the specific conversation or comment. (This is only available for the room creator and the creator of the specific converstaion or comment.)
___
## Technology that was utilized:
### languages:
* python
* HTML
* CSS
* Javascript / JQuery

### Libraries and Frameworks

* [Django](https://www.djangoproject.com/)   
    * Django was used as the web framework for this project.
   
* [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)  
    * Bootstrap 5 was used throughout the website to help with styling and responsiveness.

* [Google Fonts](https://fonts.google.com)  
    * Google fonts was used to import the fonts that were utilised for this site.

* [Font Awesome](https://fontawesome.com)  
    * Font Awesome was used to add icons to the social links included in the footer.  

### Packages / Dependecies Installed

* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)  
    * Django Allauth was used for user authentication, registration, and account management.

* [Django Crispy Form](https://django-crispy-forms.readthedocs.io/en/latest/)   
    * Django Crispy Form was used to control the rendering of the forms. 
 
* [Gunicorn](https://gunicorn.org/)  
    * Gunicorn was used as Python WSGI HTTP Server for UNIX to support the deployment of Django application.  

* [Summernote](https://summernote.org/) 
    * Summernote has been used as WYSIWYG editor.

* [Cloudinary](https://cloudinary.com/)
    * Cloudinary has been used for image management

### Database Management
* [ElephantSQL](https://www.elephantsql.com/)   
    * ElephantSQl was used for database management


### Tools and Programs
* [GitPod](https://gitpod.io/)
   * GitPod was used for writing code, committing, and then pushing to GitHub.

* [GitHub](https://github.com)  
   GitHub was used to store the projects code and was used to create and mange the user storied during the design process. 

* [Heroku](https://www.heroku.com)   
   * Heroku was used to deploy the website.
   
* [Lucid Charts](https://www.lucidchart.com/)
   * Lucid Charts was used to create the wireframes, flow chart and ERD for this project

* [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
   * Chrome DevTools was used during development process primarily to test the design on different platforms and devices.

* [W3C Markup Validator](https://validator.w3.org/)
   * W3C Markup Validator was used to validate the HTML code.

* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
   * W3C CSS Validator was used to validate the CSS code.

* [JSHint](https://jshint.com/) 
   * JSHint was used to validate the JavaScript code.
   
* [Pythonchecker](https://www.pythonchecker.com/)
   * Pythonchecker was used to validate the Python code.
___
## Testing:
### Feature Testing:
* Fixes refers to any potential current fixes/improvements that are still potentially available. 'None required' refers to the fact that at this moment there is no additional work needed to improve that feature. Many bugs and errors were encounted during the development process and several of these features were very much trail and error. The accounts of which can be found throughout the commits in GitHub.
* Top Bar: 
   - What was expected? 
   - How it was tested? 
   - What was the outcome? 
   - Fixes? None required.
* Navigation:
   - What was expected? 
   - How it was tested? 
   - What was the outcome? 
   - Fixes? None required.
* Footer:
   - What was expected? 
   - How it was tested? 
   - What was the outcome? 
   - Fixes? None required.
* Registration: 
   - What was expected? 
   - How it was tested? 
   - What was the outcome? 
   - Fixes? None required.
* Log in: 
   - What was expected? 
   - How it was tested?  
   - What was the outcome? 
   - Fixes? None required.
* Log out: 
   - What was expected? 
   - How it was tested?  
   - What was the outcome? 
   - Fixes? None required.
* The Room Cards: 
   - What was expected? 
   - How it was tested?  
   - What was the outcome? 
   - Fixes? None required.
* Pagination:
   - What was expected? 
   - How it was tested?  
   - What was the outcome? 
   - Fixes? None required.
* Create a Room:
   - What was expected? 
   - How it was tested?  
   - What was the outcome? 
   - Fixes? None required.
* Start a conversation:
   - What was expected? 
   - How it was tested?  
   - What was the outcome? 
   - Fixes? None required.
* Add Comments:
   - What was expected? 
   - How it was tested?  
   - What was the outcome? 
   - Fixes? None required.
* Edit Room:
   - What was expected? 
   - How it was tested?  
   - What was the outcome? 
   - Fixes? None required.
* Edit Conversation / Comments
   - What was expected? 
   - How it was tested?  
   - What was the outcome? 
   - Fixes? None required.
                   
#### Device testing:
This site has been physically tested on:
   - ASUS ZenBook
#### Validation
The code was put into pythonchecker.com a link to which can be found [here](https://www.pythonchecker.com/)
As you can see from the two images the highest score was a 92% and the lowest 82% which upon their rating system is regarded as excellent. All of the code was put through this checker I have purposely only included images of the highest and lowest scores as to avoid clutter. All other results sit in between these two figures.
![Validatio High](assets/validation-high.png)
![Validation Low](assets/validation-low.png)   

   ___
## Deployment:
1. Firstly pip3 freeze > requirements.txt was used in order to update the requirements.txt file so that all the imports would be read properly on Heroku.
2. From the Heroku dashboard 'create a new app' was clicked.
3. I then named my app characetr-creator-ci-project-3. 
4. I selected my region and clicked create app.
5. I then clicked on settings at the tab at the top of the page.
6. I then created a configs var to include my creds.json file 
7. I then added the python and node.js buildpacks.
8. I then hit deploy in tab at the top of the page.
9. I then connected to my github.
10. After connecting to my gitHub I was able to search and select my required repository.
11. I then selected automatic deployment in order to push any changes made in GitHub automatically to my application.
12. With that done I was able to view my application and ensure everything worked as expected.

___
## credits/acknowledgments
### Content:
- All code was written by myself, no external code was taking during the devolopment of this application. 
- Pandas was used to read the google sheets.
- Tabulate was used for the presentation of the character sheet.
### Media:
- I would like to Thank DnD Beyond for providing all the information available throughout this application. Without their vast amount of available information this application would not have been quite so possible.

## Final thoughts
- This was a monumental task I set myself, I under estimated the work that would be needed to achieve what I wanted. However I do have to say im happy with how it has turned out. There is still lots that could be done here. I know that it's far from perfect but I learnt a lot along the way and I pushed myself to do something different and I can be proud of what I achieved here.