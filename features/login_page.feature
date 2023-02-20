Feature: Test Login Page
  As a user, I want to login with my email and password to the ecommerce site
  I am on Magento ecommerce page


    Scenario: Successful login with valid email and valid password
      Given I open Magento page
      When I click on sign in button
      And the Customer login message appear
      And I input a "cristina_comsha@yahoo.com" username
      And I input a "cristina2023@" password
      And I click on sign in
      Then I should be logged in to my account

    Scenario: Successful logout
      Given I Am successful logged in
      When I click on my account button to go on the user menu page
      And On the user menu page I click the Sign out button
      Then I don't find the username on the main page

    Scenario Outline: Fail Login
      Given I open Magento page
      When I click on sign in button
      And I input a "<email>" username
      And I input a "<password>" password
      And I click on sign in
      Then the "Customer Login" still appear
      Examples: Credentials
          |email                        | password        |
          | cristina_comsha@yahoo.com   | 1234            |
          | cristina_comsa@yahoo.com    | cristina2023@   |


