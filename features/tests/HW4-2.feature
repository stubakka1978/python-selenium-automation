# Created by alder at 10/5/2022
Feature: Tests for amazon search

  Scenario: User can search for coffee
    Given Open amazon page
    When Search for coffee
    Then Search results for "coffee" are shown

  Scenario: User can search for mug
    Given Open amazon page
    When Search for mug
    Then Search results for "mug" are shown

  Scenario: User can add a product to the cart
    Given Open Amazon page
    When Search for earbuds
    And Click on the first product
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)