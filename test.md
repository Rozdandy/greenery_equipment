

## Responsiveness

[responsivness](readme/images/responsive.png)

This site was was tested on multiple browsers (Google Chrome, Mozzila Firefox and Opera), multiple mobile devices (Samsung Galaxy, Huawei, Sony) and tablet device(Samsung Galaxy Tab) and it shown responsivness and compatibility. Web-site is responsive for screens from 350px to 2k. Everything is in order and responsive. But, viewing it on a 4k desktop, Background pictures are too small and they cover 2/3 of the width.








| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Viewing on mobile device | Images filled correctly, no overflow | As Expected | Pass |
| Viewing on tablet device | Pages rendering properly | As expected | Pass |
| Viewing on laptop & desktop devices | All work well, no distortion | As expected | Pass |



### Navigation performance

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on Logo button | Opens "Index" page | As Expected | Pass |
| Clicking on `My account` link | Opens dropdown tab with links | As expected | Pass |
| Clicking on `log In` link | Opens Log In page | As expected | Pass |
| Clicking on `log Out` link | Logs out user and redirects to log in page | As expected | Pass |
| Clicking on `Register` link | Opens Register page | As expected | Pass |
| Clicking on `Shopping bag icon` link | Opens the page links | As expected | Pass |
| Clicking on `GO TO BLOG` link | Opens dropdown with links | As expected | Pass |
| Clicking on `ALL PRODUCTS` link | Opens dropdown with links | As expected | Pass |
| Clicking on `MACHINE EQUIPMENT` link | Opens dropdown with links | As expected | Pass |
| Clicking on `FARM IMPLEMENT` link | Opens dropdown with links | As expected | Pass |
| Clicking on `MISCELLANEOUS` link | Opens dropdown with links | As expected | Pass |
| Clicking on nav menu link | Opens the appropriate web page | As expected | Pass |



### SHOP NOW BUTTON 

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `SHOP NOW` link | Opens and takes you to all products page | As expected | Pass |

### Button "Go to top" 
* It appears in the all products page and whereaver search is made both in large and small devices but not available in the blog section

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on Go to top button | It scrolls up to top of the page | As Expected | Pass

### Footer

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `Facebook` icon | Opens Facebook site in new tab | As expected | Pass |
| Clicking on `Instagram` icon | Opens Instagram site in new tab | As expected | Pass |
| Clicking on `linkedin` icon | Opens LinkedIn site in new tab | As expected | Pass |
| Clicking on `Pinterest` icon | Opens Pinterest site in new tab | As expected | Pass |
| Clicking on `SHOP` link | Opens and takes you to all products page | As expected | Pass |
| Clicking on `BLOG` link | Opens dropdown with links | As expected | Pass |

## Home App/ page

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on product cards | Opens the selected product detail | As expected | Pass |
| Clicking on `SHOP NOW` link | Opens and takes you to all products page | As expected | Pass |


## Products App/ page

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on filter button | Show products under that category | As Expected | Pass
| Clicking on product | Show product details info on a new page | As Expected | Pass
| Selecting the number in input and clicking "Add" | Adds the selected quantity of the item to cart and then opens "Shop" page |As Expected | Pass
| Clicking on breadcrumbs `products home` button | Opens "All Products" page | As Expected | Pass
| Clicking on nav menu link | Opens the appropriate web page | As expected | Pass |

## Comments App/ page

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `Add comment` button without filling all the forms | Displays Validation to tell the user to enter all the forms | As Expected | Pass |
| Clicking on `Add comment` | the message is added | As Expected | Pass

## Bag & Checkout/ page

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| When no items in shopping bag, clicking on `Bag icon` button | Shows 'Your bag is empty' & "Keep Shopping" page | As Expected | Pass
| Adding & removing quantity | change of quantity of products "shopping bag items" toast snippet displays message of either add or remove. If quantity changed to zero, removes product from bag | As Expected | Pass
| Clicking on products image and/or name | Displays that products detail page | As Expected | Pass
| Clicking on `Secure Checkout` button | Opens "Chekout" page | As Expected | Pass
| Clicking on `Secure Checkout` button without filling the form | Redirects user to required field | As Expected | Pass
| Clicking on `Adjust bag` button while filling out the form | Redirects user to shopping bag | As Expected | Pass
| Clicking on `Complete Order` button after filling out the form | Checks with Stripe if everything is ok and redirects to "order summary with Thank you message" page | As Expected | Pass

## Reviews

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `Submit` button without filling all the form fields | Displays Validation to tell the user to enter all the fields | As Expected | Pass |
| After clicking on ``Submit`` button | User is redirected to "Products" page, with review now sucessfully added | As Expected | Pass |
| Clicking on `Edit` symbol | User is redirected to "Edit your review" modal pre-filled with instance of previous comment | As Expected | Pass |
| Clicking on `Delete` symbol | user is directed to modal to delete their review | As Expected | Pass |

## Account

### Registration

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `Register` button | Registers the user and redirects to confirm email address. If registration form is incomplete, shows Please fill out this field | As Expected | Pass

### Sign in

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `LogIn` with correct username and password | Directs user to the index page | As Expected | Pass |
| Clicking on `LogIn` with Incorrect username and password | flash message to user showing incorrect username or password | As Expected | Pass |
| Clicking on Forgot password | Opens "Forgot password" page | As Expected | Pass

### Profile App/ page

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on profile button | Opens "profile" page |As Expected | Pass
| Clicking on `Update` button | Saves changes to profile and redirects to "Profile" page | As Expected | Pass


### Log Out

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `log Out` button | Logs out user and redirects to index page | As expected | Pass |


**Back to [Top](testing.md)**



#### User stories tests:
MOre on Testing user experience:

1. Authenticated and Unauthenticated users:

  * user: can  browse the site by sorting, category or price, or by rating and make a selection to buy
  * user : can use the search icon to look for products they like
  * user: can view each product details to identify price, read other users reviews on the product,select a product
  size or quantity
  * user : can easily access products on sale and keep track of their total shopping bag cost throughout the site via their shopping bag
  * user: can make easy and secure stripe checkout processes.
  * user: upon successful checkout, will be gets redirected to success page with order details and a confirmation email is also sent to them containing their order details.


2. Sign-up / Login:

  * user: can successfully sign up for an account by filling the the required form fields and will recieve a confirmation email
  * user: users can successfully recover their passwords by clicking on the forgot password: which will send an email to
the provided email adddress with the necessary link for password recovery.


3. Logged in / authenticated users: 

  * user: authenticated users can save their default delivery/billing info on their profile page
  * user: authenticated users can add to blog post when they visit a particular post
  * user: logged in users can review products that they have bought


1. Site Owner:

  * can easily add a product via the product management form 
  * can easily add a blog post via the blog management form 
  * can easily edit/update product info
  * can easily delete products






### Python:
* Validated my python file with inbuilt code institute gitpod python lint : there are still some lint line errors coming from the model character fields
upon the use of both null and blank as True.


MINEEEEEEEEEEEEEEE


# TESTING

#### Validating  HTML, CSS and JavaScript and Python/django:


* **Lighthouse**:     [Balsamiq](https://developers.google.com/web/tools/lighthouse/?utm_source=devtools) To audit the site perfomance and accessibility.

* **Am I Responsive?**:[Am I Responsive?](http://ami.responsivedesign.is/) It was used to test the responsiveness of the site and to take screenshot of devices.

* [HTML-Validator](https://validator.w3.org/#validate_by_input"):   validator produced django template syntaxes as errors

* [Jshint](https://jshint.com/): When using the tool some warnings were flagged which mainly were the use of ES6 (use 'esversion: 6'). But the codes work perfectly. However, I have taken note of that for next project. [Javascript test](static/testing/jsms3.png).

* The [CSS validator](https://jigsaw.w3.org/css-validator/) was without any issues [CSS test](static/testing/cssms3.png).

* The [PEP8](http://pep8online.com/checkresult) was without any issues [PEP8 test](static/testing/pep8.png).

#### Compatability Test :
##### i used the following browsers the test the project:

      * Systems: Macbook Pro Laptop, HP laptop, and Lenovo laptop.
      * Browsers: Chrome, Opera, Edge, Firefox, Safari
      * Phones and Tabs: iPad Pro, different Iphone series and androids


