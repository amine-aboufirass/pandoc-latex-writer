
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

function BulletList(items)
    print("entering BulletList function")
    for i, item in pairs(items) do
        print(i, item)
    end
    return " "
end

function Plain(s)
    return s
end

function Doc(body, metadata, variables) 
    return body
end
