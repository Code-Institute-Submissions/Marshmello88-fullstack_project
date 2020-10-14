# fullstack_project




A link to the shopping cart must be present on every page. This link should include a quick
summary about how many items are in the cart, maybe a small icon of the shopping cart? This needs to
be on every page so that whenever the user gets the itch to check out, no matter what page they are on,
they should be able to figure out how to do it quickly and without any confusion. Once they click on the 
shopping cart link, they should be taken to the cart page where they can review their items and edit
quantities or remove single items as they need. A checkout link should be present only if the cart is not
empty. IMPORTANT: Users, even anonymous ones that haven’t registered or logged in, should be able to
add items to their cart.”

Cart model:  4 things that I need to store with each item in a
user’s shopping cart:
1. unique Cart ID value
2. Product ID
3. Date product was added to the cart
4. Quantity in the cart


<!-- FORM TEST-->

			<!--<div class="addtocartbtn">
            <form method="POST" action="." class="cart">
            {% csrf_token %}
		{{ form.as_p }}
		<br />
		<input type="submit" value="Add To Cart" name="submit" alt="Add To Cart" />
	</form>
    </div>-->