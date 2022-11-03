# Created by alder at 10/1/2022
Feature: Tests for Amazon main page

  Scenario: Hamburger menu is present
    Given Open amazon page
    Then Verify hamburger menu is present

  Scenario: Footer has correct amount of links
    Given Open amazon page
    Then Verify that footer has 38 links

  Scenario: User can see language options
    Given Open amazon page
    When Hover over language options
    Then Verify Spanish option present

  Scenario: User can see New Arrival deals
    Given Open Amazon product B074TBCSC8 page
    When Hover over New Arrivals
    Then Verify New Arrival deals