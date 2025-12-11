local filename = 'input.txt'

function read_grid(filename)
local file = io.open(filename, "r")
if not file then
print("Error: Could not open file " .. filename)
return {}
end

local grid = {}
for line in file:lines() do
    if line ~= "" then
        table.insert(grid, line)
        end
        end
        file:close()
        return grid
        end

        function count_neighbors(grid, x, y)
        local offsets = {
            {-1, -1}, {0, -1}, {1, -1},
            {-1,  0},          {1,  0},
            {-1,  1}, {0,  1}, {1,  1}
        }

        local count = 0
        local height = #grid
        local width = #grid[1]

        for _, offset in ipairs(offsets) do
            local nx = x + offset[1]
            local ny = y + offset[2]

            if nx >= 1 and nx <= width and ny >= 1 and ny <= height then
                if grid[ny]:sub(nx, nx) == '@' then
                    count = count + 1
                    end
                    end
                    end

                    return count
                    end

                    function solve(filename)
                    local grid = read_grid(filename)
                    local accessible = 0
                    local height = #grid

                    if height == 0 then
                        return 0
                        end

                        local width = #grid[1]

                        for y = 1, height do
                            for x = 1, width do
                                local cell = grid[y]:sub(x, x)

                                if cell == '@' then
                                    local neighbors = count_neighbors(grid, x, y)

                                    if neighbors < 4 then
                                        accessible = accessible + 1
                                        print("Accessible roll at (" .. x .. ", " .. y .. ") with " .. neighbors .. " neighbors")
                                        end
                                        end
                                        end
                                        end

                                        return accessible
                                        end

                                        local result = solve(filename)
                                        print("\nTotal accessible rolls: " .. result)
