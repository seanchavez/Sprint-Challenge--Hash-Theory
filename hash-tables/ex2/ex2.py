def reconstruct_trip(tickets):
    ticket_table = {}
    trip = []

    for ticket in tickets:
        ticket_table[ticket[0]] = ticket[1]
    current_ticket = ticket_table[None]
    while current_ticket:
        trip.append(current_ticket)
        if current_ticket not in ticket_table:
            return []
        current_ticket = ticket_table[current_ticket]   
    return trip 

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass
