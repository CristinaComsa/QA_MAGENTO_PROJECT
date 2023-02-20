 QA_MAGENTO_PROJECT -->  Project description

For this project I decided to make some tests on an E-Commerce website named Magento E-Commerce.

Magento is a test website where you can interact with the page such as searching, buying, removing a product from the shopping cart an many other functionalities.

The project contains 3 features, 17 scenarios and 81 steps. All of them pass successfully.

The first feature 'home_page' has 9 scenarios where I test the functionality of links and buttons, also if an user can search, add and remove items from cart:

1. Test home page and what's new icon 
2. Test home page women icon 
3. Test home page men icon
4. Test home page gear icon
5. Test home page training icon
6. Test home page sale icon
7. Search product
8. Add product to cart
9. Delete product from cart

The second feature 'login_page' has 4 scenarios:

1. Login successful
2. Login fail with credentials: username: cristina_comsha@yahoo.com and password: 1234
3. Login fail with credentials: username: cristina_comsa@yahoo.com and password: cristina2023@
4. Logout successful

The third feature 'women_page' has 4 scenarios where I check if the correct number of total products is displayed on the category page and all the sorting options work correctly when sorting the products according to the chosen criteria:

1. Shop by category
2. Sort by accending price
3. Sort by descending price
4. Check the page logo "LUMA"


To create this project I used the Python programming language with the PyCharm IDE.

Software Packages from Python, I used:

-- selenium

-- behave --> library that interprets and runs tests written in Gherkin

-- behave-html-formatter --> helps generate reports

-- webdriver-manager.

Steps to use the project:

Download or clone the project from GitHub with the command: git clone https://github.com/CristinaComsa/QA_MAGENTO_PROJECT.git

Install the necessary libraries with the command: pip install -r requirements.txt

Run the tests with the command: behave

To create the HTML report of the tests, use the command: behave -f html -o report.html

To access the reports, look for the generated HTML file in the project folder and open it in a browser.
