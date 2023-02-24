# The Festival Ground

![full-mockup]()
This site has been designed to..

Find a link to the deployed site [here]()

## contents:
1. [User experience](#user-experience)
   - [what I wanted to achieve](#what-i-wanted-to-achieve)
   - [My goals for the user](#my-goals-for-the-user)
   - [the road map](#the-plan-and-the-roadmap)
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
      1. [feature 1]()
      2. [feature 2]()
   - [About Page](#about-page)
      1. [feature 1]()
      2. [feature 2]()
   - [Room View](#room-view)
      1. [feature 1]()
      2. [feature 2]()
   - [Your Rooms](#your-rooms)
      1. [feature 1]()
      2. [feature 2]()
   - [Register](#register)
      1. [feature 1]()
      2. [feature 2]()
   - [Login](#login)
      1. [feature 1]()
      2. [feature 2]()
   - [Edit Conversation and Edit Comment](#edit-conversation-and-edit-comment)
      1. [feature 1]()
      2. [feature 2]()
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

1. Create a...

___
### The Plan and the Roadmap:
![The flow chart](assets/roadmap.png)
- The plan for this application in the begining was...

___
## Final Product
### The start
![The start](assets/final-product.png)
* As you can see above this is the first screen that the user will be faced with. It is hoped that through reading this brief introduction that they will understand what this application has to offer and will be excited to begin to create their own charcater.
___
## Features: 
### Welcome page:
  - The first thing the user will see is the intro page. This was put in to help describe the purpose of the site and to help them understand the mechanics. It also helps the user understand that not all the information they read about a race or a class will be present at the end.
  ![the intro page](assets/intro.png)

### Colour scheme:
  - Throughout this application the user would of seen various colours. These were specific choices. The Logo is a bright red that so often is related to DnD. Each class and race has their own colour to give a sense of difference but also to give a sense of their 'personality' e.g the elf and gnome are green to reflect their link to Nature. The Tiefling is Red to give a sense of their link to Hell. The Character sheet at the end is also presnted in the colour of the users chosen class.

___
## Technology that was utilized:
### languages:
* python
### external assets utilized:
* [GitHub](https://github.com/)
* [GitPod](https://gitpod.io/)
* [Heroku](https://dashboard.heroku.com/)
___
## Testing:
### Feature Testing:
* Fixes refers to any potential current fixes/improvements that are still potentially available. 'None required' refers to the fact that at this moment there is no additional work needed to improve that feature. Many bugs and errors were encounted during the development process and several of these features were very much trail and error. The accounts of which can be found throughout the commits in GitHub.
* Choose Race: 
   - What was expected? The user types a Race from the list provided and is presented with the relevent information regarding that Race. The user can then read and cycle through the information at their liesure. If the user inputs a Race that is not present or misspells one of the races they are told that their choice is not playable and are asked to pick again.
   - How it was tested? First H was typed, "H is not a playable Race, please select again" was shown. Secondly Humman was typed, "Humman is not a playable Race, please select again." was shown. human was then typed, the first bit of infomation regarding humans was then presented to the user. with the next input "Click enter to cycle through info: " The text colour was also changed to reflect the chosen Race. Enter was clicked. the previos infomation was cleared and the next bit of information was presented. A was then typed into the input. Nothing happened. A was then entered. The next bit of information was then presented without issue. These steps were then repeated for all the playable races.
   - What was the outcome? All information presented was correct for that Race, the ability to cycle through the information worked just as planned and only the relevent information is shown. Incorrect inputs are correctly identified and the usre is prompt to choose again.
   - Fixes? None required.
* Choose Class: 
   - What was expected? The user types a class from the list provided and is presented with the relevent information regarding that Class. The user can then read and cycle through the information at their liesure. If the user inputs a Class that is not present or spells one of the Classes incorrectly they are told that their choice is not playable and are asked to pick again.
   - How it was tested?  First B was typed, "B is not a playable Class, please select again" was shown. Secondly Bardbarian was typed, "Bardbarian is not a playable Class, please select again." was shown. Barbarian was then typed, the first bit of infomation regarding barbarians was then presented to the user. with the next input "Click enter to cycle through info: " The text colour was also changed to reflect the chosen Class. Enter was clicked. the previos infomation was cleared and the next bit of information was presented. A was then typed into the input. nothing happened. A was then entered. The next bit of information was then presented without issue. These steps were then repeated for all the playable Classes.
   - What was the outcome? All information presented was correct for that Class, the ability to cycle through the information worked just as planned and only the relevent information is shown. Incorrect inputs are correctly identified and the usre is prompt to choose again.
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