# Ecommerce webshop

My final project for Code Institute's Full Stack Web Developer course.


# Goal

It's an ecommerce website where a user can buy ingame items for their nintendo switch. The users only have three critical goal paths:

1) View the store's inventory of amiibo villagers.

2) Keep track of the villagers they want to purchase using favorites or using a shopping cart. Note: They don't need to create 
an account or anything to purchase an item.

3) Check out and pay for their items.

The central target audience for the website are people who want to buy in-game items for their Switch. These are people of all ages. 


# Important to note

I wasn't able to commit my last changes to github due to an error in gitpod (tried to resolve it with a tutor to no avail) so the email verification
isn't set up but I will provide my own password and email when I hand in this project. Some other small things that I wasn't able to commit and push:
When a logged in user makes a first purchase it erroneously states that they get 0.2? procent off when in fact it's 20%. Other changes I made but could not 
commit were, when a user signs up for a newsletter a "mission accomplished" text should appear. On small screens however it appears way too large and so it 
overflows it's div. The same goes for the order number on small screens. Lastly, the index page text should be slightly edited to include all perks of creating
an account. I changed one of the texts to: Discover new friends, keep track of favorites. Additional perk? New users with an account get 20% off their 
<strong> next </strong> order!</span>.


# Main features included:

- User account area

- Product pages

- Newsletter option

- Reviews and rating system

- Cart and checkout

- Promo code functionality (only for logged in users), after first order user gets 20 % off next purchase


# User Stories 

1) Authentication: User can signup/login/logout 

2) Filtering: User can view lists of items per category and search by name, filter by species or personalities.

3) Shopping Cart: User can add items to shopping cart. User can edit or remove items from the shopping cart.  

4) Checkout: User can fill in a form and submit shipping info. After submitting this info, order is processed and a success page is 
displayed.

5) Order processed: user gets confirmation email with order nr

6) Customer can create a profile (only for logged in users), where the user can save their favorite villagers, view order history 
or leave reviews on items.

7) If the user is logged in, he can view profile page. If not, user gets redirected to the login page.

8) User can edit and update profile details if needed

9) Customer is able to read reviews of other customers

10) Pagination added to reviews so it's not too crowded on a single page

11) Customer can use text search function to find something specific

12) User gets notification when an item is added/edited/removed to/from the cart.

13) Shows the total price of all items (on every page)

14) A link to the shopping cart must be present on every page. This should display order total. 

15) Users, even anonymous ones that haven’t registered or logged in, should be able to
add items to their cart.

16) A user can edit the billing information on their profile.

17) A user can sign up for a newsletter

18) User can also leave a review.

19) For logged in users only: After first order, user gets % off next purchase


# Tested on

Ipad pro (landscape and portrait), laptop with HPDI, laptop with MPDI, iphone 5, iphone 6/7/8, iphone 6/7/8 plus, iphone X
(phones tested in portrait mode).

# Nice to haves

- Kept the placeholder name/logo for the time being; original name would be a nice addition in the future

- When adding a product to favorites include some type of heart animation

- Responsive on more devices (also in landscape mode)

- Newsletter error (when an incorrect email address is entered) is currently unstyled (ran out of time). Am awate and will fix that in 
the future.

- Currently also a slight issue with the styling of product detail page where a user is not logged in :( Blue line is
displayed where the text "please sign in to leave a review" is. This is not a conscious styling choice : D

- "Remove" icon on favorites page should have a white background so as to not blend into the rest of the image. Will also be fixed.
That or it needs to be placed somewhere else it doesn't fit the rest of the page atm.

- Front page could look a bit better on phones, my mistake was that I didn't start off with bootstrap right away. So for FP I had to
adjust everything via media queries, which cost me a lot of time. 


# Main Tools/Frameworks

Django, Stripe, Django Crispy Forms, Allauth, Pillow, Heroku, SQlite3, Bootstrap


# Languages
This project uses HTML, CSS, JavaScript and Python programming languages.

# Testing
Testing is done using the Django testing framework. Everything else was tested manually.

# Validation Services:

The following validation services and linter were used to check the validity of the website code.

W3C Markup Validation was used to validate HTML.

W3C CSS validation was used to validate CSS.


# Deployment to Heroku

Steps to take:

Firstly, create a Heroku app by clicking the "New" button in the Heroku dashboard.

Secondly, we need to link our local Git repository to Heroku, which is what we're going to do in this video.

Thirdly, create a requirements.txt file (pip freeze > requirements.txt), which contains a list of our dependencies.

And finally, create a Procfile (echo web: python run.py > Procfile), which is a special kind of file that tells Heroku how to run the project.

In heroku dashboard select the master branch then click "Deploy Branch".

Link Heroku app to a GitHub repo. You can selectively deploy from branches or configure auto-deploys.

Deployed link https://whatevahh.herokuapp.com/

# Wireframes

![Cart Wireframe](media/cart_wf.jpg)

![Products Wireframe](media/product_wf.jpg)

![Front page Wireframe](media/frontpage_wf.jpg)


#MEDIA

Image sources taken from: https://www.nintendo.com/, www.starface.com.
