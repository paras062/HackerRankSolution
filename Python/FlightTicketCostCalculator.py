# The flight ticket rates for a round-trip (Mumbai->Dubai) were as follows:
# Rate per Adult: Rs. 37550.0
# Rate per Child: 1/3rd of the rate per adult
# Service Tax: 7% of the ticket amount (including all passengers)
# As it was a holiday season, the airline also offered 10% discount on the final ticket cost (after inclusion of the service tax).
# Find and display the total ticket cost for a group which had adults and children.

# Test the program with different input values for number of adults and children.
# Sample Input
# Adults = 5, Childer = 2 | Expected Output/Total ticket cost = 204910.35
# Adults = 3, Childer = 1 | Expected Output/Total ticket cost = 120535.5
import decimal
from decimal import Decimal, ROUND_05UP, ROUND_DOWN, ROUND_HALF_DOWN
from decimal import ROUND_HALF_UP, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN, ROUND_UP


def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost = 0
    # Write your logic here
    ticket_price = 37550.0
    tax_percentage = 7
    discount_percentage = 10
    ticket_price_child = round(float(ticket_price) / 3, 2)
    total_ticket_cost_adult = float(ticket_price) * float(no_of_adults)
    total_ticket_cost_child = float(ticket_price_child) * float(no_of_children)

    ticket_fare = float(total_ticket_cost_adult) + \
        float(total_ticket_cost_child)
    tax = float(ticket_fare) * (float(tax_percentage)/100)

    ticket_fare_taxed = float(ticket_fare) + float(tax)
    discounted_amount = float(ticket_fare_taxed) * \
        (float(discount_percentage)/100)

    total_ticket_cost=float(total_ticket_cost)
    total_ticket_cost = Decimal(
        float(ticket_fare_taxed) - float(discounted_amount))
    total_ticket_cost = Decimal(total_ticket_cost.quantize(
        Decimal('.01'), rounding=ROUND_DOWN))

    total_ticket_cost = str(total_ticket_cost)
    total_ticket_cost = str(total_ticket_cost).rstrip('0').rstrip(
        '.') if '.' in total_ticket_cost else total_ticket_cost
    # Logic ends

    return total_ticket_cost


# Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost = calculate_total_ticket_cost(5, 2)
# total_ticket_cost = calculate_total_ticket_cost(3, 1)
print("Total Ticket Cost:", total_ticket_cost)
