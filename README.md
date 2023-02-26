# The Festival Ground

![full-mockup]()
This site has been designed to be a music based community forum. The general idea of the website was to build a place where anyone and everyone could come togther to discuss and debate any topics surronding music that would like to. A key goal from the start was for the user to be in complete control over what they build into the site, they have control over the rooms that they create, the conversations they start and the comments they leave.

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
## the road map
### User stories

___
### Development Plan:
![The flow chart](assets/roadmap.png)
- The plan for this was 

___
#### Structure:

___
#### Skeleton:

___
#### Surface:

___
## Final Product
### The start
![The start](assets/final-product.png)
* As you can see above this is the first screen that the user will be faced with. It is hoped that through reading this brief introduction that they will understand what this application has to offer and will be excited to begin to create their own charcater.
___
## Features: 
### Welcome page:
  - The first thing the user will see is the intro page. This was put in to help describe the purpose of the site and to help them understand the mechanics.
  ![the intro page](assets/intro.png)

### Colour scheme:
  - 
___
## Technology that was utilized:
### languages:
* python
* HTML
* CSS
* Javascript / JQuery
### external assets utilized:
* [GitHub](https://github.com/)
* [GitPod](https://gitpod.io/)
* [Heroku](https://dashboard.heroku.com/)
___
## Testing:
### Feature Testing:
* Fixes refers to any potential current fixes/improvements that are still potentially available. 'None required' refers to the fact that at this moment there is no additional work needed to improve that feature. Many bugs and errors were encounted during the development process and several of these features were very much trail and error. The accounts of which can be found throughout the commits in GitHub.
* Registration: 
   - What was expected? 
   - How it was tested? 
   - What was the outcome? 
   - Fixes? None required.
* Log-in: 
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