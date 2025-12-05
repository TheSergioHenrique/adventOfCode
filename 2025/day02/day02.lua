local filename = 'input.txt'

function read_input(filename)
    local file = io.open(filename, "r")
    if not file then
        print("Error: Could not open file..." .. filename)
        return ""
    end

    local content = file:read("*all")
    file:close()
    return content
end





function is_invalid_id(num)
    local str = tostring(num)
    local len = #str

    --tamanho precisa ser divisivel.
    if len % 2 ~= 0 then
        return false
    end

    local half = len / 2
    local left = str:sub(1, half)
    local right = str:sub(half +1)
    --leading zero é festa meme
    if left:sub(1, 1) == '0' then
        return false
    end

    return left == right
end

function parse_ranges(input)
    local ranges = {}
    input = input:gsub("%s+", "")

    for range_str in input:gmatch("[^,]+") do
        local start, end_val = range_str:match("(%d+)%-(%d+)")
        if start and end_val then
            table.insert(ranges, {tonumber(start), tonumber(end_val)})
        end
    end

    return ranges
end

function solve(filename)
    local input = read_input(filename)
    local ranges = parse_ranges(input)
    local total = 0

    for _, range in ipairs(ranges) do
        local start_num = range[1]
        local end_num = range[2]

        for num = start_num, end_num do
            if is_invalid_id(num) then
                print("Found invalid ID: " .. num)
                total = total + num
            end
        end
    end

    return total
end


local result = solve(filename)
print("\nTotal sum of invalid IDs: " .. result)


