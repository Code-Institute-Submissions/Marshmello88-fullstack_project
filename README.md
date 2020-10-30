
#The Amiibo Store Application

It's a store where a user can buy ingame items for their nintendo switch. The users only have three critical goal paths:

View the store's inventory of amiibo villagers.
Keep track of the villagers they want to purchase using favorites or using a shopping cart. 
Note: They don't need to create an account or anything to purchase an item.
Check out and pay for their items.

#UX

#User Stories 

Authentication: User can signup/login/logout

Filtering: User can view lists of items per category and search by name, filter by species or personalities.

Shopping Cart: User can add items to shopping cart. User can edit or remove items from the shopping cart.  

Checkout: User can fill in a form and submit shipping info. After submitting this info, order is processed and a success page is displayed.

Order processed: user gets confirmation email with order nr

Create a customer profile that is only for logged in users, where the user can save their favorite villagers, view order history 
or leave reviews on purchased items.

If the user is logged in, show the page. If not, redirect the user to the login page.

Create more then 10 items.

Add pagination to reviews.

Add search box to items listing page, search uses GET and query params to generate new page. The search query uses the name and description fields.

Allow the user to filter items by species and personalities.

User gets notification when an item is added to the cart.

Allow user to edit/delete items from the cart

Shows the total price of all items

Allows them to purchase items, purchasing takes the user to payment form 

Create a form that allows the user to enter billing info

On submit, the order id status changes to purchased

A link to the shopping cart must be present on every page. This should display order total. 

Users, even anonymous ones that haven’t registered or logged in, should be able to
add items to their cart.

A user can edit the billing information on their profile.

#Tested on

ipad ipad pro (landscape and portrait) laptop with hpdi aptop with mpdi, iphone 5, iphone 6/7/8/, iphone 6/7/8 plus, iphone x
(phones tested in portrait mode)