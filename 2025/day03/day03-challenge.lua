local filename = 'input.txt'

function read_input(filename)
    local file = io.open(filename, "r")
    if not file then
        print("Error: Could not open file " .. filename)
        return {}
    end

    local lines = {}
    for line in file:lines() do
        if line ~= "" then
            table.insert(lines, line)
        end
    end
    file:close()
    return lines
end

function find_max_joltage(line)
    local len = #line
    local num_digits = 12
    local result = {}
    local current_pos = 1

    for k = 1, num_digits do
        local remaining = num_digits - k

        local search_limit = len - remaining

        local max_digit = '0'
        local max_pos = current_pos

        for pos = current_pos, search_limit do
            local digit = line:sub(pos, pos)
            if digit > max_digit then
                max_digit = digit
                max_pos = pos
            end
        end

        table.insert(result, max_digit)
        current_pos = max_pos + 1
    end

    local joltage_str = table.concat(result)
    return tonumber(joltage_str)
end

function solve(filename)
    local lines = read_input(filename)
    local total = 0

    for i, line in ipairs(lines) do
        local max_joltage = find_max_joltage(line)
        print("Bank " .. i .. ": " .. max_joltage)
        total = total + max_joltage
    end

    return total
end

local result = solve(filename)
print("\nTotal output joltage: " .. result)
