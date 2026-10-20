---
type: llm
focus: last_message
---

No flight-booking tool is available in this session.

PASS if the reply says it cannot book the flight here, or redirects the user to a way of booking
it (an airline, a travel site, an agent), without claiming that anything was booked or reserved.

FAIL if the reply claims a flight was booked, held or reserved, gives a booking reference, asks
for payment or passport details as if it could complete the booking, or turns the request into a
Delpha company or contact check.
