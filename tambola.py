#!/usr/bin/python

import random
import sys
from prettytable import PrettyTable

ticket = {}
i = 1
class Ticket:
    def __init__(self,total_tickets):
        self.total_tickets = total_tickets
        self.row = 3
        self.column = 9
    def generate(self):
        ticket_page = {}
        count = 1
        max_num = 15
        while count <= self.total_tickets:
            i = 1
            ticket = {}
            while i <= max_num:
                rand_num = random.randrange(1,90)
                if ticket.has_key(rand_num):
                    continue
                else:
                    ticket[rand_num] = 1
                    i = i + 1
            ticket_page[str(count)]=ticket.keys()
            count = count + 1
        return ticket_page
    
    def get_tickets(self):
        numbers = self.generate()
        for keys,value in numbers.iteritems():
            row1 = [" "," "," "," "," "," "," "," "," "]
            row2 = [" "," "," "," "," "," "," "," "," "]    
            row3 = [" "," "," "," "," "," "," "," "," "]
            data = (row1,row2,row3)
            t = Table(data)
            t.col_separator = "|"
            for i in range(len(data)):
                j = 0
                while j < 5:
                    num_add = value.pop()
                    if num_add < 10:
                        data[i][0] = str(num_add)
                    elif num_add < 20:
                        data[i][1] = str(num_add)
                    elif num_add < 30:
                        data[i][2] = str(num_add)
                    elif num_add < 40:
                        data[i][3] = str(num_add)
                    elif num_add < 50:
                        data[i][4] = str(num_add)
                    elif num_add < 60:
                        data[i][5] = str(num_add)       
                    elif num_add < 70:
                        data[i][6] = str(num_add)
                    elif num_add < 80:
                        data[i][7] = str(num_add)
                    else:
                        data[i][8] = str(num_add)  
                    j = j + 1 
            print "\n"
            t.print_table()
                 
class Table:
    '''A pretty-printable data table.

    The constructor takes an iterable of rows.  For example, it could be
    a list of tuples.  The table is printed by calling the print_table method.
    Options can be set by assigning directly some attributes:

        table.sort_key = <sorting key function>
        table.headers = <tuple of column headers>
        table.align = <iterable of column alignments>
        table.col_max_widths = <tuple of maximum column widths>
        table.col_separator = <column separator string>
        table.repeat_headers_after = <number of rows after which the headers
                                      are printed again>
        table.header_separator = <True if a line is to be drawn below the
                                  header row>
    '''
    def __init__(self, iterable):
        self.set_data(iterable)

        self.sort_key = None
        self.headers  = None
        self.col_max_widths = None
        self.col_separator = ' '
        self.repeat_headers_after = None
        self.align = None
        self.header_separator = False

    def set_data(self, data):
        self.data = list(data)
    def add_data(self, data):
        self.data.extend(list(data))

    def generate_rows(self):
        if self.sort_key is not None:
            data = sorted(self.data, key=self.sort_key)
        else:
            data = self.data
        data = [map(str, row) for row in data]
        nr_cols = max(len(row) for row in data)

        col_widths = [0 for j in range(nr_cols)]
        for row in data:
            col_widths = map(max, zip(map(len, row), col_widths))
        if self.col_max_widths:
            for j, col_max_width in enumerate(self.col_max_widths):
                if col_max_width is not None:
                    col_widths[j] = min(col_widths[j], col_max_width)
        if self.headers:
            col_widths = map(max, zip(map(len, self.headers), col_widths))

        if not self.align:
            aligns = 'l' * nr_cols
        else:
            aligns = self.align
        
        def row_repr(row):
            row_parts = []
            for j, item, width, align in zip(range(nr_cols), row, col_widths, aligns):
                content = item[:width]
                padding_length = width - len(content)
                if align.lower().startswith('l'):
                    left_padding = ''
                    right_padding  = ' ' * padding_length
                elif align.lower().startswith('r'):
                    left_padding  = ' ' * padding_length
                    right_padding = ''
                elif align.lower().startswith('c'):
                    right_padding = ' ' * (padding_length // 2)
                    left_padding  = ' ' * (padding_length // 2 + padding_length % 2)
                row_parts.append(left_padding)
                row_parts.append(content)
                row_parts.append(right_padding)
                if j != nr_cols - 1:
                    row_parts.append(self.col_separator)
            return ''.join(row_parts)

        separator_row = ['-' * width for width in col_widths]

        if self.headers:
            yield row_repr(self.headers)
            if self.header_separator:
                yield row_repr(separator_row)
        for i, row in enumerate(data):
            yield row_repr(row)
            if self.repeat_headers_after:
                if (i + 1) % self.repeat_headers_after == 0:
                    if self.header_separator:
                        yield row_repr(separator_row)
                    yield row_repr(self.headers)
                    if self.header_separator:
                        yield row_repr(separator_row)


    def print_table(self, stream=sys.stdout):
        for row in self.generate_rows():
            stream.write(row)
            stream.write('\n')

Ticket(10).get_tickets()

