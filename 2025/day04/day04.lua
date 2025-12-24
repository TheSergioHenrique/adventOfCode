local filename = 'input.txt'

local DIRECTIONS = {
    {-1, -1}, {0, -1}, {1, -1},
    {-1,  0},          {1,  0},
    {-1,  1}, {0,  1}, {1,  1}
}

local function read_grid(filename)
    local file = assert(io.open(filename, "r"), "Couldn't open " .. filename)
    local grid = {}

    for line in file:lines() do
        if #line > 0 then
            table.insert(grid, line)
        end
    end

    file:close()
    return grid
end

local function is_valid_position(x, y, width, height)
    return x >= 1 and x <= width and y >= 1 and y <= height
end

local function count_neighbors(grid, x, y)
    local count = 0
    local height, width = #grid, #grid[1]

    for _, dir in ipairs(DIRECTIONS) do
        local nx, ny = x + dir[1], y + dir[2]

        if is_valid_position(nx, ny, width, height) and
           grid[ny]:sub(nx, nx) == '@' then
            count = count + 1
        end
    end

    return count
end

local function solve(filename)
    local grid = read_grid(filename)
    local accessible = 0
    local height, width = #grid, #grid[1]

    for y = 1, height do
        for x = 1, width do
            local cell = grid[y]:sub(x, x)

            if cell == '@' and count_neighbors(grid, x, y) < 4 then
                accessible = accessible + 1
                print(string.format("Roll at (%d, %d) with %d neighbors",
                                    x, y, count_neighbors(grid, x, y)))
            end
        end
    end

    return accessible
end

local result = solve(filename)
print(string.format("\nTotal: %d", result))
