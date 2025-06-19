Feature: Create booking

   @regression @positive
  Scenario: Verify simple booking creation
    Given The booking API is available
    When I create a booking with the following details
      | Fields          | Values     |
      | firstName       | John       |
      | lastName        | Doe        |
      | totalPrice      | 100        |
      | depositPaid     | true       |
      | checkin         | 2025-07-01 |
      | checkout        | 2025-08-01 |
      | additionalNeeds | Breakfast  |
    Then The booking should be created successfully

    @regression @positive
  Scenario: Verify simple booking creation with wrong date format
    Given The booking API is available
    When I create a booking with the following details
      | Fields          | Values     |
      | firstName       | John       |
      | lastName        | Doe        |
      | totalPrice      | 100        |
      | depositPaid     | true       |
      | checkin         | 01-01-2022 |
      | checkout        | 2025-08-01 |
      | additionalNeeds | Breakfast  |
    Then The booking should be created successfully

     @regression @positive @multiple
    Scenario Outline: Create multiple bookings with different details
        Given The booking API is available
        When I create a booking with the following details <firstName>, <lastName>, <totalPrice>, <depositPaid>, <checkin>, <checkout> and <additionalNeeds>
        Then All the bookings should be created successfully

        Examples:
            | firstName  | lastName  | totalPrice | depositPaid | checkin     | checkout    | additionalNeeds |
            | Alice      | Smith     | 150        | true        | 2025-07-01  | 2025-08-01  | None            |
            | Bob        | Johnson   | 200        | false       | 2025-07-15  | 2025-08-15  | WiFi            |