# Created by alder at 9/27/2022
Feature: Tests for amazon sign in and cart

  Scenario: User can sign into account
    Given Open amazon page
    When Click Returns & Orders
    Then User is able to sign into account

    Scenario: User can see empty cart
    Given Open amazon page
    When Click Cart
    Then User is able to see cart is empty