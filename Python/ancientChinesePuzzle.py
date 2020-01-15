def solve(heads, legs):
    error_msg = "No solution"
    chicken_count = 0
    rabbit_count = 0
    for rabbit_count in range(heads + 1):
        chicken_count = heads - rabbit_count
        if 2 * chicken_count + 4 * rabbit_count == legs:
            print(chicken_count, rabbit_count)
            return
    print(error_msg)

    # Start writing your code here
    # Populate the variables: chicken_count and rabbit_count

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    # print(chicken_count,rabbit_count)
    # print(error_msg)


# Provide different values for heads and legs and test your program
solve(38, 131)
