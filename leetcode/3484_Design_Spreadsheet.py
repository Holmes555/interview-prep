class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.data = {c: {} for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}

    def setCell(self, cell: str, value: int) -> None:
        col = cell[0]
        row = int(cell[1:])
        self.data[col][row] = value

    def resetCell(self, cell: str) -> None:
        col = cell[0]
        row = int(cell[1:])
        if row in self.data[col]:
            del self.data[col][row]

    def getValue(self, formula: str) -> int:
        total = 0
        parts = formula.split('=')[1].split('+')
        if parts[0][0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            col1 = parts[0][0]
            row1 = int(parts[0][1:])
            if row1 in self.data[col1]:
                total += self.data[col1][row1]
        else:
            total += int(parts[0])

        if parts[1][0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            col2 = parts[1][0]
            row2 = int(parts[1][1:])
            if row2 in self.data[col2]:
                total += self.data[col2][row2]
        else:
            total += int(parts[1])
        return total


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
