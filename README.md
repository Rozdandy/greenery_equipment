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






