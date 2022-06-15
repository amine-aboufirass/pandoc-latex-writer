
function Blocksep()
  return '\n\n'
end

function Doc(body, metadata, variables)
  return body
end


function Str(s)
  return s
end

function Space()
  return ' '
end

-- lev is an integer, the header level.
function Header(lev, s, attr)
  return '<h' .. lev .. '>' .. s .. '</h' .. lev .. '>'
end

