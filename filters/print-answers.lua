-- Print builds only: move collapsed "Answer..." callouts to an "Answers" section at the end
-- of the chapter, leaving a pointer in place, so readers can try drills on paper first.
-- Quarto (1.4+) turns callouts into custom "Callout" nodes before user filters run, so a
-- plain Div handler never sees them; the Callout handler below catches them, nested or not.
-- The Div handler is kept for plain (non-callout-node) divs.
local answers = {}

local function title_text(t)
  if t == nil then return "" end
  if type(t) == "string" then return t end
  return pandoc.utils.stringify(t)
end

local function is_answer_div(div)
  local collapsed = div.attributes["collapse"] == "true"
  local title = div.attributes["title"] or ""
  local callout = false
  for _, c in ipairs(div.classes) do
    if c:match("^callout") then callout = true end
  end
  return callout and collapsed and title:match("^Answer")
end

local function pointer(n)
  return pandoc.Para({pandoc.Emph({pandoc.Str("Answer " .. n .. " is at the end of the chapter. Try it first.")})})
end

local function take(content)
  if content.t ~= nil or content.tag ~= nil then content = {content} end  -- a single Block
  table.insert(answers, content)
  return pointer(#answers)
end

function Div(div)
  if not is_answer_div(div) then return nil end
  return take(div.content)
end

function Callout(c)
  local collapsed = c.collapse == true or c.collapse == "true"
  if collapsed and title_text(c.title):match("^Answer") then
    return take(c.content)
  end
  return nil
end

function Pandoc(doc)
  if #answers == 0 then return doc end
  doc.blocks:insert(pandoc.Header(2, "Answers to Predict the play"))
  for i, content in ipairs(answers) do
    doc.blocks:insert(pandoc.Para({pandoc.Strong({pandoc.Str("Answer " .. i .. ".")})}))
    for _, b in ipairs(content) do doc.blocks:insert(b) end
  end
  return doc
end
