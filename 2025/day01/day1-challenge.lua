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

function count_zero_crossings(current_pos, direction, distance)
    local crossings = 0

    if direction == 'R' then
        crossings = math.floor((current_pos + distance) / 100) - math.floor(current_pos / 100)
    elseif direction == 'L' then
        crossings = math.floor((current_pos - 1) / 100) - math.floor((current_pos - distance - 1) / 100)
    end

    return crossings
end

function process_rotations(rotations)
    local position = 50
    local zero_count = 0

    for _, rotation in ipairs(rotations) do
        local direction = rotation:sub(1, 1)
        local distance = tonumber(rotation:sub(2))

        local crossings = count_zero_crossings(position, direction, distance)
        zero_count = zero_count + crossings

        if direction == 'L' then
            position = (position - distance) % 100
        elseif direction == 'R' then
            position = (position + distance) % 100
        end
    end

    return zero_count
end

local rotations = read_file(filename)
local password = process_rotations(rotations)
print("Password (Challenge): " .. password)
