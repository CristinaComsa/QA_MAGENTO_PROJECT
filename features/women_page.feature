Feature: Test Women Page
  As a buyer, I want to visit the women page
  I am on Magento ecommerce page

  Scenario: Shop by category
    Given I open Magento page
    When I click on women button
    Then I click on tops category
    And I should be on tops category items page
    And I expected to be 13 shopping categories
    And I expected to be 50 items


  Scenario: Sort by ascending price
    Given I open Magento page
    When I click on women button
    Then I click on tops category
    And I select sort by price
    And items should be on ascending order

  Scenario: Sort by descending price
    Given I open Magento page
    When I click on women button
    Then I click on tops category
    And I select sort by price
    And items should be on descending order

  Scenario: Check the logo button
    Given I open Magento page
    When I click on women button
    Then I click on the "LUMA" icon
    And I should be on the home page

