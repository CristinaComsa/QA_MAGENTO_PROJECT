Feature: Test Home Page
  As a buyer, I want to visit the ecommerce site
  I am on Magento ecommerce page

  Scenario: Test home page and what's new icon
    Given I open Magento page
    And Magento title is available
    And the message "demo store" appear
    When I click on what's new button
    Then I should be on what's new section


  Scenario: Test home page women icon
    Given I open Magento page
    When I click on women button
    Then I should be on women section

  Scenario: Test home page men icon
    Given I open Magento page
    When I click on men button
    Then I should be on men section

  Scenario: Test home page gear icon
    Given I open Magento page
    When I click on gear button
    Then I should be on gear section


  Scenario: Test home page training icon
    Given I open Magento page
    When I click on training button
    Then I should be on training section


  Scenario: Test home page sale icon
    Given I open Magento page
    When I click on sale button
    Then I should be on sale section

  Scenario: Search product
    Given I open Magento page
    When I click on search bar box
    And I input "pants gym" product items I want
    And I click on search button
    Then I should be on page with the searched products

  Scenario: Add product to cart
    Given I open Magento page
    When I click on search bar box
    And I input "Diva Gym Tee" product items I want
    And I click on search button
    And I click on the "Diva Gym Tee" product
    And I select size and colour
    And I click on add to cart button
    Then cart counter is incremented by one

  Scenario: Delete product from cart
    Given I open Magento page
    When I add an "Diva Gym Tee" product to cart
    And I click on basket button
    And I click on the remove item icon
    Then cart counter becomes empty


