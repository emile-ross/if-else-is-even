--
-- Run the generator:
-- $ lua lua.lua 9
--
-- Run it directly after generate:
-- $ lua lua.lua 9 | lua
-- false
-- 
-- Redirect it to a file to reuse it later:
-- $ lua lua.lua 9 > is_even.lua
--
-- Later, if you don't remember if 9 is even or not, just run:
-- $ lua is_even.lua
--

if #arg == 0 then
    print("Usage: lua lua.lua <number>")
    os.exit(1, true)
end

Number = tonumber(arg[1])

if math.type(Number) == nil or math.type(Number) == "float" then
    print("Invalid number")
    os.exit(2, true)
end

Output = "Number = " .. Number .. "\n"
for i = 0, Number do
    Output = Output .. "if Number == " .. i .. " then\n"
    local result = "false"
    if i % 2 == 0 then
        result = "true"
    end
    Output = Output .. "    print(" .. result .. ")\n"
    Output = Output .. "end\n"
end

print(Output)

