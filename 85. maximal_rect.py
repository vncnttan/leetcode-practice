def floodfill(matrix, y, x, count):
    if matrix[y][x] == "0":
        return count
    
    if y < 0 or x < 0 or y >= len(matrix)-1 or x >= len(matrix[y])-1:
        # Index out of bound
        return count

    matrix[y][x] = "0"
    count += 1
    
    count = floodfill(matrix, y, x-1, count)
    count = floodfill(matrix, y, x+1, count)
    count = floodfill(matrix, y-1, x, count)
    count = floodfill(matrix, y+1, x, count)

    return count

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        maximum_number = 0

        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x] == "1":
                    current_rect = floodfill(matrix, y, x, 0)
                    if current_rect > maximum_number:
                        maximum_number = current_rect
        return maximum_number

        