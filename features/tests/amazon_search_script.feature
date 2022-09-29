# Created by alder at 9/27/2022
Feature: Tests for amazon search

  Scenario: User can search for coffee
    Given Open amazon page
    When Search for coffee
    Then Search results for "coffee" are shown

    Scenario: User can search for mug
    Given Open amazon page
    When Search for mug
    Then Search results for "mug" are shown