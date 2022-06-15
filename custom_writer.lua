local bullets = {}

function Header(lev, s, attr)
    level_sequences = {
        "section",
        "subsection",
        "subsubsection",
        "subsubsubsection"
    }
    return string.format("\\%s{%s}", level_sequences[lev], s)
end

function Blocksep()
    return "\n\n"
end

function Para(s)
    return s.."\n\n"
end

function Str(s)
    return s
end

function Space()
    return " "
end

-- replacement for BulletList, returned via global metatable
function BulletList_(items)
    local buffer = {}

    for key, value in pairs(items) do
        table.insert(buffer, table.concat(bullets) .. value)
    end
    
    -- remove bullet inserted in metatable
    table.remove(bullets)
    return table.concat(buffer, "\n") 
    
end

function Plain(s)
    return s
end

function print_table(tbl)
    for k, v in pairs(tbl) do
        print(
            "key = " .. tostring(k) .. "[" .. type(k) .. "], " ..
            "val = " .. tostring(v) .. "[" .. type(v) .. "]"
        )
    end
end

setmetatable(
    _G, 
    {
        __index = function (tbl, fname)
            if fname == "BulletList" then
                print("\nCALLING BULLETLIST\n")
                print("before insertion")
                print_table(bullets)
                table.insert(bullets, "*")
                print("\nafter insertion")
                print_table(bullets)
                
                return BulletList_
            end
        end
    }
)

function Doc(body, metadata, variables) 
    return body
end
