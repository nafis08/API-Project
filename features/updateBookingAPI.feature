Feature: temporary test

  @dependent
  Scenario Outline: Verify booking update with multiple updates
    Given The booking API for update is available
    When I update a booking with the parameters <firstName>, <lastName>, <totalPrice>, <checkin>, <checkout>, <depositPaid>, <additionalNeeds>
    Then The booking should be updated successfully with the given parameters

    Examples:
      | firstName  | lastName  | totalPrice | checkin     | checkout    | depositPaid | additionalNeeds |
      | Alex       | Johnson   | 2000.00    | 2025-10-01  | 2025-11-01  | True        | Pool            |
      | Sarah      | Connor    | 2500.00    | 2025-11-15  | 2025-12-15  | False       | None            |