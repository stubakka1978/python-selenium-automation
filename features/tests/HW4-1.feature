Feature: Tests for Amazon main page

Scenario: Hamburger menu is present
    Given Open amazon page
    Then Verify hamburger menu is present

Scenario: Footer has correct amount of links
    Given Open amazon page
    Then Verify that footer has 38 links

 Scenario: BestSellers page has correct amount of links
    Given Open amazon page
    When Click Best Sellers
    Then Verify that page has 5 links
