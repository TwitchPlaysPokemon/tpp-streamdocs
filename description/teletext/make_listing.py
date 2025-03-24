import os
import json
from datetime import datetime
import re

script_dir = os.path.dirname(os.path.realpath(__file__))

# Get a list of files from the pages directory.
pages_dir = os.path.join(script_dir, "pages")
page_filenames = os.listdir(pages_dir)

filepath = os.path.join(script_dir, "pages.json")

def LoadRaw(filename):
    """
    Load raw files from edit.tf (Raw 0x00-0x7f)
    ZXNet calls this "Binary dump of Level 1 Page Data"
    Convert to edit.tf's base64 implementation
    """

    with open(filename, "rb") as f:
        # Now 24 lines of 40 characters follow (the header is omitted)
        data = bytearray(f.read())
    
    # Identify whether this file has LF or CRLF line endings, or none at all
    if len(data) == (24*40) or len(data) == (25*40):
        # raw data, no CRLF
        data_lines = [data[i:i+40] for i in range(0, len(data), 40)]
    elif len(data) == (24*41) or len(data) == (25*41):
        # raw data with LF line endings
        data_lines = [data[i:i+40] for i in range(0, len(data), 41)]
    elif len(data) == (24*42) or len(data) == (25*42):
        # raw data with CRLF line endings
        data_lines = [data[i:i+40] for i in range(0, len(data), 42)]
    else:
        raise IOError(f"Invalid Teletext-Raw file: {filename}")
    
    b64 = [0 for i in range(1167)]
    # Construct a base-64 array by iterating over each character in the frame.
    for row in range(25):
        for col in range(40):
            for bit in range(7):
                # How many bits into the frame information we are.
                frame_bit = 7 * ((row * 40) + col) + bit

                # Work out the position of the character in the base-64 encoding and the bit in that position.
                b64_bit_offset = frame_bit % 6
                b64_char_offset = int((frame_bit - b64_bit_offset) / 6)

                # Read bit, write bit.
                bit_val = data_lines[row][col] & (1 << (6 - bit))
                b64[b64_char_offset] |= min(bit_val, 1) << (5 - b64_bit_offset) 
    
    #Encode each char
    encoding = "0:"
    for char in b64:
        encoding += "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"[char]
    
    return encoding, bytearray([x for xs in data_lines for x in xs]).decode("ascii")

print("Generating listing...")

# Page list.
pages = []
for page_filename in page_filenames:
    page_number = int(page_filename[1:4])
    path = os.path.normpath(f"{pages_dir}/{page_filename}")
    b64, text = LoadRaw(path)
    pages.append({
        "number": page_number,
        "name": ' '.join(page_filename.split('.')[0].split('-')[1:]),
        "path": path.replace(script_dir + "/", ""),
        "image": "images/" + str(page_number) + ".png",
        "data": b64,
        "text": text
    })
pages.sort(key=lambda p: p["number"])

COLOURMAP = (
        "#000",   # Black
        "#F00",   # Red
        "#0F0",   # Green
        "#FF0",   # Yellow
        "#00F",   # Blue
        "#F0F",   # Magenta
        "#0FF",   # Cyan
        "#FFF"    # White
        )


def charmap_bedstead(cha, dhrow, mosaic, separated):
    """
    Private: map character set -- for Bedstead font

    dhrow:
        0 = normal height
        1 = double-height row 1
        2 = double-height row 2
    mosaic:
        True for mosaic graphics mode
    separated:
        False for contiguous mosaic
        True for separated mosaic
    """

    # Print nothing for the bottom half of a double-height char
    if dhrow == 2:
        return " "

    if mosaic and not separated:
        # mosaic, contiguous
        if cha >= 0x20 and cha <= 0x3F:
            return chr(0xEE00 + (cha - 0x20))
        elif cha >= 0x60 and cha <= 0x7F:
            return chr(0xEE40 + (cha - 0x60))
        # 0x40 <= cha <= 0x5F: Fall through to G0 character set

    elif mosaic and separated:
        # mosaic, separated
        if cha >= 0x20 and cha <= 0x3F:
            return chr(0xEE20 + (cha - 0x20))
        elif cha >= 0x60 and cha <= 0x7F:
            return chr(0xEE60 + (cha - 0x60))
    # 0x40 <= cha <= 0x5F: Fall through to G0 character set

    # character mapping table
    m = {
            0x23: 0xA3,     # 2/3: ASCII # => £
            0x24: 0x24,     # 2/4: ASCII $ => $
            0x40: 0x40,     # 4/0: ASCII @ => @
            0x5b: 0x2190,   # 5/B: ASCII [ => left arrow
            0x5c: 0xBD,     # 5/C: ASCII \ => 1/2 fraction
            0x5d: 0x2192,   # 5/D: ASCII ] => right arrow
            0x5e: 0x2191,   # 5/E: ASCII ^ => up arrow
            0x5f: 0x23,     # 5/F: ASCII _ => #
            0x60: 0x2014,   # 6/0: ASCII ` => emdash
            0x7b: 0xBC,     # 7/B: ASCII { => 1/4 fraction
            0x7c: 0x2016,   # 7/C: ASCII | => ||
            0x7d: 0xBE,     # 7/D: ASCII } => 3/4 fraction
            0x7e: 0xF7,     # 7/E: ASCII ~ => divide
            0x7f: 0x25a0    # 7/F: ASCII DEL => square block
        }

    if cha in m:
        return chr(m[cha])
    else:
        return chr(cha)

def text_convert(chars):
    """
    Text Convert

    chars:   40x25 1D array containing Viewtext character data.
                This is essentially the Viewtext/Teletext RAM buffer.
    reveal:  True if the REVEAL button has been pressed.
                Makes CONCEALed screen elements visible.

    Returns a string suitable for HTML
    """
    # Set start of page conditions
    #   Disable double-height
    dhrow = 0

    # Start rendering the data
    body = ""
    for row in range(24):
        s = ''              # string buffer

        # Set start of line condition
        # White text, black background
        fg              = COLOURMAP[7]
        bg              = COLOURMAP[0]
        def color_span():
            return f'<span style="color: {fg}; background-color: {bg};">'
        s += color_span()
        # Double Height off
        doubleheight    = False
        # Mosaic characters off, contiguous mode, Hold Mosaic off
        mosaic          = False
        sepMosaic       = False
        holdMosaic      = False
        holdMosaicCh    = ord(' ')
        holdMosaicSep   = False

        # If we had double-height on the last row, this row is the second
        # double-height row.
        # If this is the second double-height row, reset double-height.
        if dhrow == 1:
            dhrow = 2
            # ETS 300 706: Double height row 2 uses data from the previous row
        elif dhrow == 2:
            dhrow = 0

        for c in range(40):
            col = chars[row * 40 + c]

            # Mask off the MSB (sometimes set in image files)
            col &= 0x7F

            # process control characters
            if col < 0x20:
                # It's a control character

                # Deal with Set-After codes, which take effect from the
                # following character.
                if col <= 0x07 or \
                        (col >= 0x10 and col <= 0x17) or \
                        col in (0x08, 0x0A, 0x0B, 0x0D, 0x0E, 0x0F, 0x1B, 0x1F):
                    # this is a set-after code, preload a blank
                    if holdMosaic:
                        if doubleheight:
                            s = s + charmap_bedstead(holdMosaicCh, dhrow, True, holdMosaicSep)
                        else:
                            s = s + charmap_bedstead(holdMosaicCh, 0, True, holdMosaicSep)
                    else:
                        s = s + ' '
                    setAfter = True
                else:
                    setAfter = False

                # Control code handling

                if (col <= 0x07) or (col >= 0x10 and col <= 0x17):
                                    # 0x00 to 0x07: Alpha Colour (Set-After)
                                    # 0x10 to 0x17: Mosaic Colour (Set-After)
                    # TODO: Alpha Black only takes effect on some decoders (see ETSI ETS 300 706)
                    #       What does Teletext Level 1 spec say we should do here?
                    if (col != 0 and col != 0x10):
                        fg = COLOURMAP[col & 0x07]
                        s += "</span>" + color_span()

                        if (mosaic != (col >= 0x10)):
                            # The "Held-Mosaic" character is reset to "SPACE" at the start of each
                            # row, on a change of alphanumeric/mosaics mode or on a change of size
                            holdMosaicCh = ord(' ')

                        mosaic = (col >= 0x10)
                        conceal = False

                elif col == 0x08:   # 0x08: Flash (Set-After)
                    flash = True

                elif col == 0x09:   # 0x09: Flash (Set-At)
                    flash = False

                elif col == 0x0A:   # 0x0A: End Box (Set-After)
                    box = False     # TODO

                elif col == 0x0B:   # 0x0B: Start Box (Set-After)
                    box = True      # TODO

                elif col == 0x0C:   # 0x0C: Normal size (Set-At)
                    if doubleheight:
                        holdMosaicCh = ord(' ')
                        s += "</span>"
                    doubleheight = False

                elif col == 0x0D:   # 0x0D: Double Height (Set-After)
                    # The "Held-Mosaic" character is reset to "SPACE" at the start of each
                    # row, on a change of alphanumeric/mosaics mode or on a change of size
                    if not doubleheight:
                        holdMosaicCh = ord(' ')

                    # If doubleheight isn't enabled, enable it
                    if dhrow == 0:
                        dhrow = 1
                        s += '<span class="tall">'
                    doubleheight = True

                # 0x0E: Level 2.5 and 3.5: Double Width (Set-After) -- TODO
                # 0x0F: Level 2.5 and 3.5: Double Size  (Set-After) -- TODO

                # 0x10-0x17 are handled above (Mosaic Colour)

                elif col == 0x18:   # 0x18: Conceal (Set-At)
                    conceal = True

                elif col == 0x19:   # 0x19: Contiguous Mosaic characters (Set-At)
                    sepMosaic = False

                elif col == 0x1A:   # 0x1A: Separated Mosaic characters (Set-At)
                    sepMosaic = True

                # TODO: 0x1B / Escape

                elif col == 0x1C:   # 0x1C: Black Background (Set-At)
                    bg = COLOURMAP[0]
                    s += "</span>" + color_span()

                elif col == 0x1D:   # 0x1D: New Background (Set-At)
                    bg = fg
                    s += "</span>" + color_span()

                elif col == 0x1E:   # 0x1E: Hold Mosaic on (Set-At)
                    holdMosaic = True

                elif col == 0x1F:   # 0x1F: Hold Mosaic off (Set-At)
                    holdMosaic = False

                # If this was a Set-At code, load a space with the new
                # attributes into the buffer
                if not setAfter:
                    if holdMosaic:
                        if doubleheight:
                            s = s + charmap_bedstead(holdMosaicCh, dhrow, True, holdMosaicSep)
                        else:
                            s = s + charmap_bedstead(holdMosaicCh, 0, True, holdMosaicSep)
                    else:
                        s = s + ' '

            else:   # not col < 0x20
                if (not doubleheight) and dhrow == 2:
                    col = 32

                if (col & 0x20) and mosaic:
                    holdMosaicCh = col
                    holdMosaicSep = sepMosaic

                # text character
                if doubleheight:
                    s = s + charmap_bedstead(col, dhrow, mosaic, sepMosaic)
                else:
                    s = s + charmap_bedstead(col, 0, mosaic, sepMosaic)
        body += s + "</span>\n"
    return body

def make_title(page):
    return f'P{page["number"]}: {page["name"]}'

def make_img(page):
    return f'<img id="P{page["number"]}" src="../{page["image"]}" alt="{title}"/>'

def make_text(page, local_links = False):
    body = text_convert(bytearray(page["text"][40:].encode('ascii')))
    text = f'  P{page["number"]}  TELETEXT {page["number"]} {datetime.now().isoformat().replace("T"," ").split(".")[0]}\n'
    text += re.sub(r"(?i)([^\s\>])?(P)(\d\d\d)", rf'<a href="{local_links and "#P" or ""}\3{not local_links and ".html" or ""}">\1\2\3</a>', body)
    text = re.sub(r"(?i)(http(s)?://[^\s,\<]*)", r'<a href="\1" target="_blank">\1</a>', text)
    return f'<pre id="P{page["number"]}" >{text}</pre>'

print("Writing HTML pages...")
html_dir = os.path.join(script_dir, "html")
if not os.path.exists(html_dir):
    os.makedirs(html_dir)
disclaimer = "<!-- This page is autogenerated by make_listing.py. Do not edit this page. Edit the teletext page(s), page.template, or make_listing.py instead. -->\n\n\n"
with open(os.path.join(script_dir, "page.template"), "rb") as f:
    # Now 24 lines of 40 characters follow (the header is omitted)
    template= f.read().decode("utf8")
for p in range(len(pages)):
    page = pages[p]
    title = make_title(page)
    print(title)
    img = make_text(page)
    img += make_img(page)
    if p > 0:
        lastpage = pages[p - 1]
        img += f'\n<a href="{lastpage["number"]}.html" class="nav" title="{make_title(lastpage)}" id="last"></a>'
    if p + 1 < len(pages):
        nextpage = pages[p + 1]
        img += f'\n<a href="{nextpage["number"]}.html" class="nav" title="{make_title(nextpage)}" id="next"></a>'
    html = disclaimer + template.replace("--PAGE--", img).replace("--TITLE--", title).replace("--NUMBER--", str(page["number"]))
    f = open(os.path.join(html_dir, str(page["number"]) + ".html"), "w")
    f.write(html)
    f.close()    
print("Rules page")
rules = ""
for page in [page for page in pages if page["number"] >= 800]:
    rules += make_text(page, local_links=True) + '\n'
html = disclaimer + template.replace("--PAGE--", rules).replace("--TITLE--", "TPP Rules").replace("--NUMBER--", "rules").replace("rules.png", "combined_image.png")
f = open(os.path.join(html_dir, "rules.html"), "w")
f.write(html)
f.close()

for page in pages:
    del page["text"]

print("Writing page listing to {}...".format(filepath))
f = open(filepath, "w")
f.write(json.dumps(pages, separators=(',', ':')))
f.close()
print("Finished.")
