import pymupdf

doc = pymupdf.open('d:/quiza/scratch_osym/2009.pdf')
page = doc[15] # Page 16
rect = page.rect
print(f"Page width: {rect.width}, height: {rect.height}")
mid_x = rect.width / 2
print(f"Mid X: {mid_x}")

# Get blocks or words
words = page.get_text("words")
left_words = [w for w in words if w[0] < mid_x and w[1] > 60]
right_words = [w for w in words if w[0] >= mid_x and w[1] > 60]

print(f"Left words count: {len(left_words)}")
print(f"Right words count: {len(right_words)}")

# Check min X of right words and max X of left words
max_x_left = max(w[2] for w in left_words)
min_x_right = min(w[0] for w in right_words)
print(f"Max X in left column: {max_x_left}")
print(f"Min X in right column: {min_x_right}")
print(f"Divider gutter is between X={max_x_left:.1f} and X={min_x_right:.1f} (Center={mid_x:.1f})")
