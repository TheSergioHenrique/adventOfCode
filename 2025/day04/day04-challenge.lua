local filename = 'input.txt'

-- Direções dos 8 vizinhos (relógio, começando do noroeste)
local DIRECTIONS = {
    { -1, -1 }, { 0, -1 }, { 1, -1 },
    { -1, 0 }, { 1, 0 },
    { -1, 1 }, { 0, 1 }, { 1, 1 }
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

local function find_accessible_rolls(grid)
    local accessible = {}
    local height, width = #grid, #grid[1]

    for y = 1, height do
        for x = 1, width do
            local cell = grid[y]:sub(x, x)

            if cell == '@' and count_neighbors(grid, x, y) < 4 then
                table.insert(accessible, { x = x, y = y })
            end
        end
    end

    return accessible
end

local function remove_roll(grid, x, y)
    local line = grid[y]
    grid[y] = line:sub(1, x - 1) .. '.' .. line:sub(x + 1)
end

local function solve_part2(filename)
    local grid = read_grid(filename)
    local total_removed = 0
    local round = 0

    while true do
        local accessible = find_accessible_rolls(grid)

        if #accessible == 0 then
            break
        end

        round = round + 1
        print(string.format("\nRound %d: removing %d rolls", round, #accessible))

        for _, pos in ipairs(accessible) do
            remove_roll(grid, pos.x, pos.y)
            total_removed = total_removed + 1
        end
    end

    return total_removed
end

local result = solve_part2(filename)
print(string.format("\n=== Total removed rolls: %d ===", result))
