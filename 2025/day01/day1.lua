local filename = 'input.txt'

function read_file(filename)
    local rotations = {}
    local file = io.open(filename, "r")
    if not file then
        print("Error: Could not open file " .. filename)
        return rotations
    end

    for line in file:lines() do
        table.insert(rotations, line)
    end
    file:close()
    return rotations
end

function process_rotations(rotations)
    local position = 50
    local zero_count = 0

    for _, rotation in ipairs(rotations) do
        local direction = rotation:sub(1, 1)
        local distance = tonumber(rotation:sub(2))

        if direction == 'L' then
            position = (position - distance) % 100
        elseif direction == 'R' then
            position = (position + distance) % 100
        end

        if position == 0 then
            zero_count = zero_count + 1
        end
    end

    return zero_count
end

local rotations = read_file(filename)
local password = process_rotations(rotations)
print("Password: " .. password)
