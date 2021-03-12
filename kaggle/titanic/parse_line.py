def parse_line(line):
    entries = []

    entry_str = ""

    inside_quotes = False

    quote_symbol = None
    
    for char in line:
        if char == quote_symbol or quote_symbol == None and char == '"' or quote_symbol == None and char == "'" :
            quote_symbol = char
            inside_quotes = not inside_quotes

        if char == ',' and not inside_quotes :
            entries.append(entry_str)
            entry_str = ""
            continue

        entry_str = entry_str + char

    entries.append(entry_str)
    return entries
