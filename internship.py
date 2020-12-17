def construct(seatsGrid):
    seats = []
    for i in seatsGrid:
        rows = i[1]
        cols = i[0]
        # mat = [[-1]*cols]*rows
        mat = []
        for i in range(rows):
            mat.append([-1]*cols)
        seats.append(mat)
    return seats


def printSeats(seats, seatsGrid,  passengers, length):
    blksize = len(str(passengers))
    rows = [x[1] for x in seatsGrid]
    cols = [x[0] for x in seatsGrid]
    maximum = max(rows)
    top = True
    for i in range(maximum):
        rowlist = []
        rowlistl = []
        for j in range(length):
            row = ' '
            rowl = ' '
            if len(seats[j]) <= i:
                for k in range(cols[j]):
                    row += ' '*blksize
                    rowl += ' '*blksize
                    row += ' '
                    rowl += ' '
            else:
                row = '|'
                rowl = '+'
                for k in seats[j][i]:
                    if k == -1:
                        row += ' '*blksize
                        rowl += '-'*blksize
                        row += '|'
                        rowl += '+'
                    else:
                        row += str(k)+(' '*(blksize - len(str(k))))
                        rowl += '-'*blksize
                        row += '|'
                        rowl += '+'

            rowlist.append(row)
            rowlistl.append(rowl)
        if top:
            print('    '.join(rowlistl))
            top = False
        print('    '.join(rowlist))
        print('    '.join(rowlistl))


def fill_aisle_seats(filled, passengers, seatsGrid, seats, length):
    print("filling aisle seats..")
    row = 0
    tempFilled = -1
    while filled < passengers and filled != tempFilled:
        tempFilled = filled
        for i in range(length):
            if seatsGrid[i][1] > row:
                if i == 0 and seatsGrid[i][0] > 1:
                    filled += 1
                    aisleCol = seatsGrid[i][0] - 1
                    seats[i][row][aisleCol] = filled
                    if filled >= passengers:
                        break
                elif i == length - 1 and seatsGrid[i][0] > 1:
                    filled += 1
                    aisleCol = 0
                    seats[i][row][aisleCol] = filled
                    if filled >= passengers:
                        break
                else:
                    filled += 1
                    aisleCol = 0
                    seats[i][row][aisleCol] = filled
                    if filled >= passengers:
                        break
                    if seatsGrid[i][0] > 1:
                        filled += 1
                        aisleCol = seatsGrid[i][0] - 1
                        seats[i][row][aisleCol] = filled
                        if filled >= passengers:
                            break
        row += 1
    print("filled aisle seats")
    return filled


def fill_window_seats(filled, passengers, seatsGrid, seats, length):
    print("filling window seats..")
    row = 0
    tempFilled = 0
    while filled < passengers and filled != tempFilled:
        tempFilled = filled
        if seatsGrid[0][1] > row:
            filled += 1
            window = 0
            seats[0][row][window] = filled
            if filled >= passengers:
                break
        if seatsGrid[length-1][1] > row:
            filled += 1
            window = seatsGrid[length-1][0] - 1
            seats[length-1][row][window] = filled
            if filled >= passengers:
                break
        row += 1
    print("fillied window seats..")
    return filled


def fill_middle_seats(filled, passengers, seatsGrid, seats, length):
    print("filling middle seats..")
    row = 0
    tempFilled = 0
    while filled < passengers and filled != tempFilled:
        tempFilled = filled
        for i in range(length):
            if seatsGrid[i][1] > row:
                if seatsGrid[i][0] > 2:
                    for col in range(1, seatsGrid[i][0] - 1):
                        filled += 1
                        seats[i][row][col] = filled
                        if filled >= passengers:
                            break
            if filled >= passengers:
                break
        row += 1
    print("filled middle seats..")


def fillSeats(seatsGrid, passengers):
    filled = 0
    seats = construct(seatsGrid)
    # print seats
    length = len(seatsGrid)
    # Aisle
    filled_new = fill_aisle_seats(filled, passengers, seatsGrid, seats, length)
    # Window
    filled_new_2 = fill_window_seats(
        filled_new, passengers, seatsGrid, seats, length)
    # Center
    fill_middle_seats(filled_new_2, passengers, seatsGrid, seats, length)

    printSeats(seats, seatsGrid, passengers, length)


if __name__ == "__main__":
    fillSeats([[3, 2], [4, 3], [2, 3], [3, 4]], 30)
