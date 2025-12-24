local filename = 'input.txt'

local function parse_ranges(filename)
    local file = assert(io.open(filename, "r"), "Could not open " .. filename)
    local ranges = {}

    for line in file:lines() do
        if #line == 0 then
            break
        end

        local start_range, end_range = line:match("(%d+)%-(%d+)")
        table.insert(ranges, {
            start = tonumber(start_range),
            finish = tonumber(end_range)
        })
    end

    file:close()
    return ranges
end

local function merge_ranges(ranges)
    table.sort(ranges, function(a, b)
        return a.start < b.start
    end)

    local merged = {}
    local current = ranges[1]

    for i = 2, #ranges do
        local next_range = ranges[i]

        if next_range.start <= current.finish + 1 then
            current.finish = math.max(current.finish, next_range.finish)
        else
            table.insert(merged, current)
            current = next_range
        end
    end

    table.insert(merged, current)
    return merged
end

local function count_fresh_ids(merged_ranges)
    local total = 0

    for _, range in ipairs(merged_ranges) do
        total = total + (range.finish - range.start + 1)
    end

    return total
end

local function solve_part2(filename)
    local ranges = parse_ranges(filename)
    local merged = merge_ranges(ranges)
    return count_fresh_ids(merged)
end

local result = solve_part2(filename)
print(string.format("Total fresh ingredient IDs: %d", result))
