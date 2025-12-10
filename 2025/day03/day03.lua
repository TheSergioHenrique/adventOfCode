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

function build_position_map(str)
    local positions = {}

    for i = 1, #str do
        local digit = str:sub(i, i)

        if not positions[digit] then
            positions[digit] = {}
        end

        table.insert(positions[digit], i)
    end

    return positions
end

function find_max_joltage(line)
    local positions = build_position_map(line)

    -- 99 até 10
    for first_digit = 9, 1, -1 do
        for second_digit = 9, 0, -1 do
            local first = tostring(first_digit)
            local second = tostring(second_digit)

            if positions[first] and positions[second] then
                for _, pos_first in ipairs(positions[first]) do
                    for _, pos_second in ipairs(positions[second]) do
                        if pos_second > pos_first then
                            local joltage = tonumber(first .. second)
                            print("  Found: " .. first .. " at pos " .. pos_first ..
                                  ", " .. second .. " at pos " .. pos_second ..
                                  " = " .. joltage)
                            return joltage
                        end
                    end
                end
            end
        end
    end

    return 0
end

function solve(filename)
    local lines = read_input(filename)
    local total = 0

    for i, line in ipairs(lines) do
        print("Bank " .. i .. ": " .. line)
        local max_joltage = find_max_joltage(line)
        print("  Max joltage: " .. max_joltage)
        total = total + max_joltage
    end

    return total
end

local result = solve(filename)
print("\nTotal output joltage: " .. result)
