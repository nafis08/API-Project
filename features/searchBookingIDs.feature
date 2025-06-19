Feature: Search booking IDs for given parameters
  Scenario:
    Given The booking API is available
    When I search for booking IDs with the following parameters
      | Fields    | Values     |
      | firstName | Nafis      |
      | lastName  | F18        |
      | checkin   | 2023-10-01 |
      | checkout  | 2023-10-10 |
    Then The API should return one or more booking IDs

    Given The booking API is available
    When I search for booking IDs with the following parameters
      | Fields    | Values     |
      | firstName | Tim        |
      | lastName  | Ross       |
      | checkin   | 2025-10-01 |
      | checkout  | 2023-09-01 |
    Then The API should return an empty list