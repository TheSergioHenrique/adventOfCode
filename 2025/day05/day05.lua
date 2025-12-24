local filename = 'input.txt'

local function parse_input(filename)
    local file = assert(io.open(filename, "r"), "Could not open " .. filename)
    local ranges = {}
    local ids = {}
    local parsing_ranges = true

    for line in file:lines() do
        if #line == 0 then
            parsing_ranges = false
        elseif parsing_ranges then
            local start_range, end_range = line:match("(%d+)%-(%d+)")
            table.insert(ranges, {
                start = tonumber(start_range),
                finish = tonumber(end_range)
            })
        else
            table.insert(ids, tonumber(line))
        end
    end

    file:close()
    return ranges, ids
end

local function is_fresh(id, ranges)
    for _, range in ipairs(ranges) do
        if id >= range.start and id <= range.finish then
            return true
        end
    end
    return false
end

local function solve(filename)
    local ranges, ids = parse_input(filename)
    local fresh_count = 0

    for _, id in ipairs(ids) do
        if is_fresh(id, ranges) then
            fresh_count = fresh_count + 1
        end
    end

    return fresh_count
end

local result = solve(filename)
print(string.format("Fresh ingredients: %d", result))
