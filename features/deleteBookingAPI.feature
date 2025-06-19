Feature: Delete booking using Booking API

    @dependent
  Scenario: Verify booking deletion with valid booking ID
    Given The booking API for deletion is available
    When I delete a booking with the following details
      | Fields     | Values     |
      | bookingId  | validBookingId |
    Then The booking should be deleted successfully

 # Scenario: Verify booking deletion with invalid booking ID
 #   Given The booking API for deletion is available
 #   When I delete a booking with the following details
 #     | Fields     | Values          |
 #     | bookingId | invalidBookingId |
 #   Then The booking deletion should fail with an error message