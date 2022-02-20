# heedngrow
A complex Django Blog project.

## Description
This project is aimed at building a very standard blog and the aim was really archived, this project navigate through the whole crud of a thing and contains almost everything a blog site requires, it was build as my very first independent site, and it's really what makes me move.

## Language, Framework, and Libraries

- Python
- Django
- Tailwind CSS
- Htmx
- Java Script

## Pages and Compositions

- User registration and authentication
- Blog list
- Blog Description
- Comment
- Comment reply
- Comment Edit and Delete
- Blog Like
- Users list
- Category List
- Category details
- and lot more pages which can be found in the views.py

## Technology pattern

This project uses the generic class based view system, `from django.views import View` which is now a subclass for all other subsequent views in the project, methods in the view are straingt forward and follows a really smooth pattern mostly this project uses 
```
from django.views import View

class MyView(View):
    def get(self,request):
        pass
    def post(self,request,*args,**kwargs):
        pass
    def delete(self,pk):
        pass
```
This view method is basically what the project pattern follows which makes the code really more request specific, expand its readability and makes it clearer.
However on the front end, djangos' built it template engine was used and HTMX handles all the form and request taking in the front end to avoid unnecessary full page reloads.

The small Java Script that was sprinkle on this project is mainly to toggle comment replies and provide the form to user.
While tailwind CSS (CDN) was used to handle all the styllings and other necessary UIs, however the site does it's work really well, but since I'm not that verse in designs the UI might not look it's best but all the specified functionalities runs to their best.

## Installations

This project can be cloned to your local system from the command linee or you download it as zip after which all the requirement to run the project is just having Python and Django installed on your local machine.

## Take on

The best thing I took from this project after it's completion is confidence, the level of my skill boosted and I'm pretty confident that I've got the real and basic understanding of Django from work.

## Errors
I didn't know how to use GitHub effectively at the time of this project and my aim and believe was just that I need to push to GitHub whenever I'm done with a project, I wish my instructors mentioned GitHub when I was learning from them, I would have love to see all my trials and errors display all over, but never the less I'm still happy about the project.
