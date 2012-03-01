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
        self.range = [0,0,0,0,0,0,0,0,0]
    
    def generate(self):
        self.range = [0,0,0,0,0,0,0,0,0]
        ticket_page = {}
        count = 1
        max_num = 27
        while count <= self.total_tickets:
            j = 1
            ticket = {}
            while j <= max_num:
                rand_num = random.randrange(1,91)
                if ticket.has_key(rand_num):
                    continue
                else:
                    if rand_num < 10 and self.range[0] < 3:
                        ticket[rand_num] = 1
                        self.range[0] = self.range[0] + 1
                        j = j + 1
                    elif (rand_num < 20 and rand_num >= 10) and self.range[1] < 3:
                        ticket[rand_num] = 1
                        self.range[1] = self.range[1] + 1
                        j = j + 1
                    elif (rand_num < 30 and rand_num >=20) and self.range[2] < 3:
                        ticket[rand_num] = 1
                        self.range[2] = self.range[2] + 1
                        j = j + 1
                    elif (rand_num < 40 and rand_num >= 30) and self.range[3] < 3:
                        ticket[rand_num] = 1
                        self.range[3] = self.range[3] + 1
                        j = j + 1
                    elif (rand_num < 50 and rand_num >= 40) and self.range[4] < 3:
                        ticket[rand_num] = 1
                        self.range[4] = self.range[4] + 1
                        j = j + 1
                    elif (rand_num < 60 and rand_num >= 50) and self.range[5] < 3:
                        ticket[rand_num] = 1
                        self.range[5] = self.range[5] + 1
                        j = j + 1
                    elif (rand_num < 70 and rand_num >= 60) and self.range[6] < 3:
                        ticket[rand_num] = 1
                        self.range[6] = self.range[6] + 1
                        j = j + 1
                    elif (rand_num < 80 and rand_num >= 70) and self.range[7] < 3:
                        ticket[rand_num] = 1
                        self.range[7] = self.range[7] + 1
                        j = j + 1
                    elif (rand_num <=90 and rand_num >= 80) and self.range[8] < 3:
                        ticket[rand_num] = 1
                        self.range[8] = self.range[8] + 1
                        j = j + 1
                    else:
                        continue
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
            j = 0
            count1 = 0
            count2 = 0
            count3 = 0
            for i in range(len(value)):
                rem = int(value[i]/10)
                if rem == 0:
                    if data[j][0] == " " and count1 < 9:
                        data[j][0] = str(value[i])
                        count1 = count1 + 1
                    elif data[j+1][0] == " " and count2 < 9:
                        data[j+1][0] = str(value[i])
                        count2 = count2 + 1
                    else:
                        data[j+2][0] = str(value[i])
                elif rem == 1:
                    if data[j][1] == " " and count1 < 9:
                        data[j][1] = str(value[i])
                        count1 = count1 + 1
                    elif data[j+1][1] == " " and count2 < 9:
                        data[j+1][1] = str(value[i])
                        count2 = count2 + 1
                    else:
                        data[j+2][1] = str(value[i])
                elif rem == 2:
                    if data[j][2] == " " and count1 < 9:
                        data[j][2] = str(value[i])
                        count1 = count1 + 1
                    elif data[j+1][2] == " " and count2 < 9:
                        data[j+1][2] = str(value[i])
                        count2 = count2 + 1
                    else:
                        data[j+2][2] = str(value[i])
                elif rem == 3:
                    if data[j][3] == " " and count1 < 9:
                        data[j][3] = str(value[i])
                        count1 = count1 + 1
                    elif data[j+1][3] == " " and count2 < 9:
                        data[j+1][3] = str(value[i])
                        count2 = count2 + 1
                    else:
                        data[j+2][3] = str(value[i])
                elif rem == 4:
                    if data[j][4] == " " and count1 < 9:
                        data[j][4] = str(value[i])
                        count1 = count1 + 1
                    elif data[j+1][4] == " " and count2 < 9:
                        data[j+1][4] = str(value[i])
                        count2 = count2 + 1
                    else:
                        data[j+2][4] = str(value[i])
                elif rem == 5:
                    if data[j][5] == " " and count1 < 9:
                        data[j][5] = str(value[i])
                        count1 = count1 + 1
                    elif data[j+1][5] == " " and count2 < 9:
                        data[j+1][5] = str(value[i])
                        count2 = count2 + 1
                    else:
                        data[j+2][5] = str(value[i])
                elif rem == 6:
                    if data[j][6] == " " and count1 < 9:
                        data[j][6] = str(value[i])
                        count1 = count1 + 1
                    elif data[j+1][6] == " " and count2 < 9:
                        data[j+1][6] = str(value[i])
                        count2 = count2 + 1
                    else:
                        data[j+2][6] = str(value[i]) 
                elif rem == 7:
                    if data[j][7] == " " and count1 < 9:
                        data[j][7] = str(value[i])
                        count1 = count1 + 1
                    elif data[j+1][7] == " " and count2 <9:
                        data[j+1][7] = str(value[i])
                        count2 = count2 + 1
                    else:
                        data[j+2][7] = str(value[i])           
                elif rem == 8 or rem == 9:
                    if data[j][8] == " " and count1 < 9:
                        data[j][8] = str(value[i])
                        count1 = count1 + 1
                    elif data[j+1][8] == " " and count2 < 9:
                        data[j+1][8] = str(value[i])
                        count2 = count2 + 1
                    else:
                        data[j+2][8] = str(value[i])        
                else:
                    print "Hi"    
                 
            print "\n"
        count = 1
        row1_elim = [0,0,0,0,0,0,0,0,0]
        while count <= 4:
            rand_num = random.randrange(0,9)
            if row1_elim[rand_num] != 0:
                continue
            else:
                row1_elim[rand_num] = 1
                count = count + 1
        row3_elim = [0,0,0,0,0,0,0,0,0]
        count = 1 
        while count <= 4:
            rand_num = random.randrange(0,9)
            if row3_elim[rand_num] != 0:
                continue
            else:
                row3_elim[rand_num] = 1
                count = count + 1
        for i in range(0,9):
            if row1_elim[i] == 1:
                data[0][i] = " "
            else:
                row2_res = i
        row1_elim[row2_res] = 1
        for i in range(0,9):
            if row1_elim[i] == 0:
                data[1][i] = " "
        for j in range(0,9):
            if row3_elim[j] == 1:
                data[2][j] = " "
        t = Table(data)
        t.col_separator = "|"
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

print Ticket(1).get_tickets()
