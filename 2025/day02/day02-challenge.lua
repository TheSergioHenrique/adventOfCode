local filename = 'input.txt'

function read_input(filename)
    local file = io.open(filename, "r")
    if not file then
        print("Error: Could not open file " .. filename)
        return ""
    end
    local content = file:read("*all")
    file:close()
    return content
end

function is_invalid_id(num)
    local str = tostring(num)
    local len = #str

    if str:sub(1, 1) == '0' then
        return false
    end

    for pattern_len = 1, len // 2 do
        if len % pattern_len == 0 then
            local pattern = str:sub(1, pattern_len)

            if string.rep(pattern, len / pattern_len) == str then
                return true
            end
        end
    end

    return false
end

function solve(filename)
    local input = read_input(filename):gsub("%s+", "")
    local total = 0

    for range_str in input:gmatch("[^,]+") do
        local start_num, end_num = range_str:match("(%d+)%-(%d+)")

        if start_num then
            for num = tonumber(start_num), tonumber(end_num) do
                if is_invalid_id(num) then
                    print("Found invalid ID: " .. num)
                    total = total + num
                end
            end
        end
    end

    return total
end

print("Total sum of invalid IDs: " .. solve(filename))
