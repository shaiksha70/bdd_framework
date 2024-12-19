Feature: Login Page
  Scenario: Verifying Login Page
    Given Launch Chrome Browser
    When Open OrangeHRM Websites
    And Enter User "Admin" and Password "admin123"
    Then Click on Login