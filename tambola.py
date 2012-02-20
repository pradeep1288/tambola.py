#!/usr/bin/python

import random

ticket = {}
i = 1
class Ticket:
    def __init__(self,total_tickets):
        self.total_tickets = total_tickets
    def generate(self):
        ticket_page = {}
        count = 1
        max_num = 15
        while count <= self.total_tickets:
            i = 0
            ticket = {}
            while i <= max_num:
                rand_num = random.randrange(1,90)
                if ticket.has_key(rand_num):
                    continue
                else:
                    ticket[rand_num] = 1
                    i = i + 1
            ticket_page[count]=ticket.keys()
            count = count + 1
        return ticket_page


a = Ticket(2)
tiks = a.generate()
print tiks
