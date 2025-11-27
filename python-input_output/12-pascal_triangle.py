def pascal_triangle(n):
    """Returns Pascal's triangle as a list of lists"""
    if n <= 0:
        return []

    triangle = []  # Initialize empty triangle

    for i in range(n):
        row = [1]  # Each row starts with 1
        if triangle:  # If there is a previous row
            last_row = triangle[-1]
            # Add sums of neighboring elements from the previous row
            for j in range(len(last_row) - 1):
                row.append(last_row[j] + last_row[j + 1])
            row.append(1)  # Each row ends with 1
        triangle.append(row)  # Add the row to the triangle

    return triangle
