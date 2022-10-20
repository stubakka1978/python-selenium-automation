# Created by alder at 10/18/2022
Feature: Sign in test case

  Scenario: Amazon users see sign in button
    Given Open amazon page
    Then Verify Sign In is clickable
    When Wait for 5 sec
    Then Verify Sign In is clickable
    Then Verify Sign In disappears