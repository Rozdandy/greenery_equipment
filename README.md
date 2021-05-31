<img src="static/testing/test.png">


### **Website links:** 

*my github link*: [Rozdandy](https://github.com/Rozdandy/africadelishms3)


*Website Link*:

[Afric & delish](https://afric-delish.herokuapp.com/)




# Greenery Equipment
---
This project is online fictitious e-commerce store selling modern agricultural equipment in various categories, which provide farmers, government and investors to order online from the comfort of their homes, offices or farm yards. It also has the Blog section where users can read and comment on agricultural-climate change related news and posts.


# Project Summary
---
This is a Full Stack Frameworks with Django and other libraries, the project was made for Code Institute as MS4.

The website is an e-commerce shopping website. The store provides a distinct customer experience which includes some kind of user-friendly euphoria actions which afford individual customer of the website to review a particular product, view blog section and comment. The site also provide good responsive view for different devices and a well secured login, shopping and payment system.

The aim of the site is to allow the user to create an account and make a purchase of products with Stripe secure payment system and also have a taste of the latest news on climate change and agriculure. Most of the admin activities is built on Django admin-allauth login integrated modules. The site also provides enabling user-friendly  tasks such as adding, editing and deleting products or blog posts through the website User Interface.


# UX 
 ----

 ## User Experience Design UX 
 ----

## The Strategy Plane

The site owner aimed to provide customer e-commerce services to purchase items and have them delivered to their homes. Also, to provide more user interactions among users in order to built trust and good customer-owner relationships, this will enable us in understanding complex consumer behaviour to maximise conversion rates. The blog, comment and product review sections were created for this purpose but only for registered users.

 ### Main Objective:
 * To sell and promotes  online products.
 * To develope relevant targets
 * To generate revenue and provide a distincts customer experience
 * To establish brand awareness and corporate identity.
 * To know customers thought and feelings about a particular products and our services, through comment and reviews.


 ### User Stories
 ----

 The following User Stories were used to create the design that would meet the needs of several types of users which include ananymous user, regular and registered user, stakeholders and site owners.


 #### Site Users
| As A User  | I want to able to ...                                                                    | in order to...                                                                                                                                    |
|------------|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| user       | easily register for my account,                                                        | have a personalized account to be able to view my profile, rate and review products                                            |
| user       | quick login / logout                                                                   | access my account and information                                                                                                                      |
| user       | enable easy password recovery, incase I cannot remember                                       | regain access to my account                                                                                                                           |
| user       | have a personalized user profile                                                       | save my default delivery details, payment, see past order history and confirmations                                                              |
| user       | receive email confirmation upon sign up or password rest                               | verify that my account registeration was successful|                                                                                                                                                       |
| user       | view products by category, rate or price                                               | Make a selection to buy                                                                                                          |
| user       | view individual product details                                                        | identify product ratings, price, full size image, size, color, description,  and various ratings if other users had previously bought the item rated  |
| user       | search products                                                                        | add to shopping bag or buy                                                                                                         |
| user       | promptly see the outcomes of searched items and the number of products available for the searches | know if the product I searched for is available                                                                                       |                                     |
| user       | readily view the total of items in my bag anytime to avoid excessive spenidng          | avoid over spending                                                                                                                            |
| user       | sort products by either categories or prices                                            | quickly find products based on the best prices and categories                                                                           |
| user       | easily add, subtract or delete products from my shopping bag                           | ensure I can easily keep to my budget                                                                                                                 |
| user       | easily view all selected products in my shopping bag to be bought                      | see the total cost and quantity                                                                                                                       |
| user       | readily render payment with my card at checkout                                        | checkout easy                                                                                                                                         |
| user       | have confident for the security of payment process and my card details are secured     | provide the necessary info to complete the payment                                                                                        |
| user       | can readily view the order details after checkout is successful                        |  have a verified receipt of my purchase                                                                                                                |
| user       | have a confirmation email with the details of my purchase                           | have a copy of my confirmation                                                                                                                     |
| user       | have a confirmation email with the details of my purchase                           | have a copy of my confirmation                                                 
| user       | able to contact store owners                                                        | resolve any purchase or other issues I might encounter 
| user       | able to view latest post at the blog post                                           | be informed on latest climate change and agricultural related news
| site-owner | add products                                                                        | for users to see products and to be sold on my site                                                                                                                    |
| site-owner | edit / update products                                                              | easily make changes to any product attribute eg name, prices or descriptions                                                                        |
| site-owner | delete product                                                                      | easily remove product from the site.                                                                                                               |
| user       | have a confirmation email with the details of my purchase                           | have a copy of my confirmation                                                                                                                     |
| site-owner | add products                                                                        | for users to see products and to be sold on my site                                                                                                                    |
| site-owner | edit / update products                                                              | easily make changes to any product attribute eg name, prices or descriptions                                                                        |
| site-owner | delete product                                                                      | easily remove product from the site.                                                                                                               |
| site-owner | add, edit and amend blog post when necessary                                        | maintain and coordinate the serenity of the sites.


## The Scope Plane 

Covid-19 is a game-changer, a hallmark of our present dispensation. Online shopping and sales has risen drasticallly in the last 2 years and this trend will continue for a while especially with globalisation. Thus the aim here is to build user-friendly website that is intuitive and easy to navigate.

### Intended Features include:

* Responsive design.
* Intuitive and easy navigable website.
* Mobile and desktop navigations.
* Standard e-commerce feed of products with the option to sort products and filter them by price and category names. 
* Every product details could be viewed by just clicking on it.
* Blog post to inspire users, so that can be coming back for me.
* To enable customers to leave a review on a particualr product.
* Contact information to easily contact the store owner.







 ## The Skeleton Plane

 ### **Security**

The Heroku config variables to store all SECRET keys safely to prevent unwanted connections to the database.

Django allauth was used to set up user registration and built in decorators allowed restricted access to certain features on the website that are not meant for regular users.

### **Wireframe**

 [Balsamiq App](https://balsamiq.com/) was used for the design architechture and the site mockups. Below is the link to the wireframe for the desktop and mobile device.

**View all**

 * [Wireframe](wireframe/ms4_wireframe.pdf)


### **Database Design**

By default, Django works with SQL databases , thus the SQLite was used during the development. However, Heroku provides a PostgreSQL database for the deployment.

**View all**

 * [Database Schemer](toputdatabasehere)



## The Surface Plane

#### Fonts

[Google Fonts!](https://fonts.googleapis.com/css2?family=Berkshire+Swash&family=Dancing+Script:wght@500&family=Exo+2:wght@300&display=swap) Three main fonts were used for the whole sites:

* Exo+2: for the body with fall back on cursive.
* Berkshire+Swash&family: for the headers with fall back on cursive.
* Dancing+Script: for headers mute message and fall back on cursive.


#### **Colour Scheme**

The developer used [Schemecolor](https://www.schemecolor.com/floating-fall-leaves.php)  to choose colors when building the website. Particularly, the follwoing colors were used which are bright to make the site more appealling to sight:

 * #d32f2f (red color)
 * #455a64  (blue-grey color)
 * #263238  (blue-grey color )
 * #ba68c8 (purple color)
 * #69f0ae (green color)










# Features

## Existing Features

* Site Navigation bar
     it is visible on all the site pages and on all sizes (on a smaller width, it toggles into "hamburger"). It contains web-site logo and a set of links for each section and subsection of web-site. it is consistent accross the site it allows the user to do the following:

    * Allow users access to the blog site
    * Browse the site by price 
    * Browse the site by category
    * Search fucntionality via the search icon
    * User login, logout, sign-in, and sign-out
    * Access to user profile which is available to authenticated users
    * Access to shopping bag via the bag icon and toast functionality during shopping
    
* Search functionality

    * The search box is part of the top navigation bar which is accessible on all pages.
    * On smaller device, the search bar is collapsed under the search icon.
    * It allows customers to enter keywords associated with the products they wish to purchase.
    * The search results are displayed as a feed of products on `products` Django app products template.

    ![search](readme/images/search-1.png)<br>
    ![search](readme/images/search-2.png)


* Footer section

    This section is located at the bottom-most part of the page. It provides the user with the following information;

    * Links to the different sections of website: the BLOG and SHOP links
    * Telephone number
    * social media links
    * Email and Address

* Go TO Blog
    * This section contains all the blog posts which relate to climate change and agricultural matters.

* Shop

    * This is the main e-commerce feed of products of the site, it has the options to sort products and filter them by price by category name. Every product clicked will give full detail information about it sucha description, manufacturer, price sizes if any etc. It can be added to the cart and proced to checkout.
   

* User account 
    * Available to registered users to help in tracking their order history and safely storing shipping details for a smooth checkout.

* Admin account

    * Exclusvely available to the the site manager or administartor. It enables blog and products inventory. It aid access to the customers' orders, and user profiles . Majority of the information is stored in the Django admin site but the users can also do common tasks such as adding, editing and deleting products or blog posts through the site.





## Features and Django Apps

The [A Django project](https://docs.djangoproject.com/en/3.1/ref/applications/), consists of  7 Django applications listed below. 

### Home App

* The home app is the index page, a window to the site, it introduces or attract users to the website and the marketplace.
* Among features it contain are the Navigation bar and various links, the hero image and the links to the shopping site, it also conatin the footer.


### Django-allauth feature

1. Accounts/Registration:

    * `django-allauth` is a Python package installed at the beggining of the project. The package [django-allauth docs](https://django-allauth.readthedocs.io/en/latest/) is an integrated set of Django applications which enables authentication, registration, account management as well as 3rd party (social) account authentication.
    * Login / logout: a user can easily login with their registered details
    * Password reset: a user can easily recover their password incase they forget it.
    * After signing up, a verification e-mail is sent to the registered e-mail to confirm it. Once confirmed, the user can log in with their credentials and access the `profiles` app.
    

### Automatic e-mails

* A registered user will surely recieve an email for verification before they can sign in. Also, the automatic email feature allows reset and confirmation of password.
* Additionally, users receive an order confirmation e-mail after a purchase, account verification etc.


### Products app

* This is where all the logics and templates connected to the product feed and individual products are located.
* It has the: **shop**, **product detail** and **admin product management** sections

 * **shop**  user can user can sort the products by:
    - Price low
    - Price high
    - Rating low
    - Rating high
    - Product Name (A-Z)
    - Product Name (Z-A)
    - Category (A-Z)
    - category (Z-A)
 
 
  **product details**: clicking on a product;

    * Product description : here, the user can see the full description, full name, manufacurer of product etc.
    * Product Review : the review option on products is available for authenitacted users that have signed In.
    * Size selection : if product has a size : users have the option to chose  product size to purchase
    * Quantity : users get to chose from 1 to 50 qty of a particular product to add to shopping bag
  

* **Admin product management** 

    * site owner through product management link:
    - can add a product
    - edit / update a product 
    - delete a product 





[product](PUT_IMAGE_HERE)




### Profiles App

* THis app is only available to registered, authenticated users.
* It has the pre-filled users' information as a default of their shipping/delivery details on their profile page which will be used during their checkout to make it process faster.
- a user can add, update and delete their personal info
* Past order: a users profile page automatically save all their past order summary and confirmations






### Bag app

* The app main function is to aid the checkout process.
* It displays selected products to be purchased and its details 
* Users can add and reduce product quantity from the shopping bag and the cost will automatically adjust accordingly 
* Users can remove selected products from the shopping bag and cost will adjust accordingly
* For a user to proceed to checkout, they be required to register on the site. When user decides to finish shopping, they will need to input their information and credit card details so that purchases could be completed.
 
* When users empty their shopping bags, there will be a toast message with respect to that.



[Shopping bag](readme/images/cart.png)




### Toasts

* These are snippets of messages that appear based on the action performed by customers.
* The messages comes in four ways depending on the success or failure of the actoin done and they are:
    * `toast_success`
    * `toast_error` 
    * `toast_warning` 
    * `toast_info` 
    
* The primary aim of their appearance is to give feedback on the action a users performed which may include:

  * logging in
  * logging out
  * adding a product to the shopping bag
  * updating the shopping bag
  * editing a blog post
  * completing the checkout process



###  Reviews app
* It is only is available to registered/ authenticated users.
* The user also has the option to edit or delete their review after they have submitted a review.
* The rating options enables user to give a rating between 1 - 5 stars.

[Review](readme/images/review.png)



### Checkout App

* The functionality of this app is to enable users to complete their online purchasing proceseses, that is to make complete online order and secured payment.
* If user is authenticated, their profile delivery/shipping form will be pre-populated with their default 
info else if the user is not authenticated the form will be empty
* A summary of the products and cost of their purchases will be avaible on display next to the delivery/shipping form

* Stripe secure card validation: the card entered by the user will be validated in real time by stripe and if valid:
the purchase will go through and the user will be automatically redirected to success page showing order confirmation details
* A webhook is implemented to the checkout so that the order is successfully processed in case the checkout process gets interrupted. Some reasons might be closing the browser too soon or losing internet connection.
* Upon successful purchase: confirmation email is sent to the user, containing their order summary
* Logged in buyers can also see their **order history** on the `profiles page`.



### Blog app

* The app updated with post on climate change and agricultural related issues, the activities on the app is mainly of sections which are:
    * **Blog posts**: It displays short overview to all available blog posts and links to the details.
    * **Blog detail**: It gives a full detail of a particular post and also displays the comment sections
    * **Blog management**: Here, the admin has access to the blog management form to carry out CRUD activities whic include adding, editing and deleting blog posts.


[blog](readme/images/add-blog.png)<br>
[blog](readme/images/edit:delete-blog.png)





#### Features Left to Implement:

* A future feature could be adding

    * online customer service chat platform 
    * Additional payment methods like paypal or applepay
    * paginations on pages needed
    * social media loggin
    * A wish-list feature that allows authenticated users to save items for later purchase.
    * A like and unlike feature on comment and review section indicate how many people have liked a certain piece of content and certain products.







# **TECHNOLOGY USED**

*The follwoing Languages,, Frameworks, and Libraries were used to build the project*  

### Tools  

* **Git**: It was used for version control which uses the Gitpod terminal, Git was used to commit and Push codes to GitHub.
* **GitHub**:         [GitHub](https://github.com/) Developer used GitHub as a project repository to save.
* **Gitpod**:         [GitHub](https://www.gitpod.io/) The project used the Gitpod IDE as my workspace to develop the website. It is linked to GitHub repository to store data when coding.
* **Icons**:          [Font Awesome](https://fontawesome.com/) Social Media Icons were taken from this site.
* **Balsamiq**:       [Balsamiq](https://balsamiq.com/) The site was used to create the wireframes during the design stage of the project.

### Front-End Technologies

* [**HTML**](https://developer.mozilla.org/en-US/docs/Web/HTML): HTML/HTML5 the language used to create and as the markup text to add content to the website.  
* [**CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS): It provides the styling for the website.
* [**jQuery 3.4.0**](https://jquery.com/) Used as the main JavaScript functionality.
* [JavaScript](https://www.ecma-international.org/)  was used for interactivity.
* [Bootstrap](https://getbootstrap.com/) was used for page layout 
* [Google fonts](https://fonts.google.com/) was used for the site fonts
* [Font awesome](https://fontawesome.com/) was used for its icons 


### Back-End Technologies

    
* [Python3](https://www.python.org/) was used for the application scripting 
* [Django framework](https://www.djangoproject.com/) was used to build the Project, a high-level Python Web framework that encourages rapid development.
* [Heroku](https://dashboard.heroku.com/apps) is use for hosting the application.
* [Amazon web service AWS](https://aws.amazon.com/) was used to host static and media files.
* [Postgres database](https://www.postgresql.org/)  was used for the deployment of app on heroku.
* [Gunicorn server](https://gunicorn.org/) was used for the deployment app on heroku .
* [Stripe payment service](https://stripe.com/)  was used for product secured payments 
* [Google smtp](https://support.google.com/mail/answer/7126229?hl=en) was used  email to send emails to users 



* **CSS validator**:  [CSS validator](https://jigsaw.w3.org/css-validator/) The site was used to test for the validity of my CSS code. 
* **HTML validator**: [HTML validator](https://validator.w3.org/) The site was used to test for the validity of my HTML code.
* **Hover.css**:      [Hover.css](https://ianlunn.github.io/Hover/) The site was used on the navigation bar links and Social Media icons in the footer to create an hovering effects.



* [Django](https://www.djangoproject.com/) – Django is 







**References:**


* Special thanks to Tim Nelson lecture videos, most of the codes on registeration, authorization, authentication many more assisted me in completing this project.


## Media

All of the images in the site were supplied from the sources below.

* slider Image:
    *   https://www.pikrepo.com/flrcm/lasagna-on-top-of-white-ceramic-plate
    *   https://www.pikrepo.com/ftfhq/assorted-foods-on-table
    *   https://www.pikrepo.com/nuzcs/local-thai-food-buffet
    *   https://www.pikrepo.com/frive/roasted-steak-with-sliced-tomato-on-white-plate
    *   https://www.pikrepo.com/fwlnm/cooked-food-on-plate
    *   https://www.pikrepo.com/ffyyo/closeup-photo-of-cooked-food


* This sites were sources of inspiration to me:


**Miscellaneous**

 * The lecture videos and notes
 * [Stack overflow](https://stackoverflow.com/) To seek solutions to fix bugs.
 * [W3Schools](https://www.w3schools.com/) I used this site for references in many instances.

## Acknowledgements

I received inspiration for this project from:

* God for Mercies.
* Code Institute lecture video
* My mentor for advice and feedback.
* Student care and student tutors for being there when I needed them most.













































