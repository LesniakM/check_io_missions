from typing import List


def checkio(land_map: List[List[int]]) -> List[int]:
    already_counted_cells = []
    areas = []
    for row_index in range(len(land_map)):
        for cell_index in range(len(land_map[0])):
            cell_x = cell_index
            cell_y = row_index
            if land_map[row_index][cell_index] == 1:
                if [cell_x, cell_y] not in already_counted_cells:
                    this_island = [[cell_x, cell_y]]
                    neighbours = list(check_neighbourhood(land_map, cell_x, cell_y))
                    while neighbours:
                        for neighbour in neighbours:
                            if neighbour not in this_island:
                                this_island.append(neighbour)
                            new_neighbours = list(check_neighbourhood(land_map, neighbour[0], neighbour[1]))
                            for new in new_neighbours:
                                if new not in this_island and new not in neighbours:
                                    neighbours.append(new)
                            neighbours.pop(neighbours.index(neighbour))

                    areas.append(len(this_island))
                    for counted_cells in this_island:
                        already_counted_cells.append(counted_cells)
    return sorted(areas)


def check_neighbourhood(grid: List[List[int]], x: int, y: int) -> list[int, int] or False:
    # Check point above
    if y > 0:
        if grid[y - 1][x] != 0:
            yield [x, y - 1]
    # Check point below
    if y < len(grid) - 1:
        if grid[y + 1][x] != 0:
            yield [x, y + 1]
    # Check point on the left side
    if x > 0:
        if grid[y][x - 1] != 0:
            yield [x - 1, y]
    # Check point on the right side
    if x < len(grid[0]) - 1:
        if grid[y][x + 1] != 0:
            yield [x + 1, y]

    # Check left-above point
    if y > 0 and x > 0:
        if grid[y - 1][x - 1] != 0:
            yield [x - 1, y - 1]
    # Check right-above point
    if y > 0 and x < len(grid[0]) - 1:
        if grid[y - 1][x + 1] != 0:
            yield [x + 1, y - 1]
    # Check left-below point
    if y < len(grid) - 1 and x > 0:
        if grid[y + 1][x - 1] != 0:
            yield [x - 1, y + 1]
    # Check right-below point
    if y < len(grid) - 1 and x < len(grid[0]) - 1:
        if grid[y + 1][x + 1] != 0:
            yield [x + 1, y + 1]

    return False


if __name__ == '__main__':
    print("Example:")
    print(checkio([[0, 0, 0, 0, 0],
                   [0, 0, 1, 1, 0],
                   [0, 0, 0, 1, 0],
                   [0, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0]]))

    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]) == [5], "2nd example"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"
