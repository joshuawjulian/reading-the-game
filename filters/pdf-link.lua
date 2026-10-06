-- Adds a "Download PDF" link to the top of every chapter in the HTML book.
-- PDFs are built by scripts/build_pdfs.py into pdfs/<slug>.pdf (site root).
function Pandoc(doc)
  if not quarto.doc.is_format("html") then return doc end
  local input = quarto.doc.input_file
  local proj = quarto.project.directory
  if not input or not proj then return doc end
  local rel = input:sub(#proj + 2)
  if not rel:match("^chapters/") then return doc end
  local slug = rel:match("([^/]+)%.qmd$")
  local depth = select(2, rel:gsub("/", ""))
  local up = string.rep("../", depth)
  local link = pandoc.RawBlock("html",
    '<div class="pdf-link"><a href="' .. up .. 'pdfs/' .. slug .. '.pdf">⬇ Printable PDF</a></div>')
  table.insert(doc.blocks, 1, link)
  return doc
end
