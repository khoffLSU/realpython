from reader import feed
import parse

# pattern to match in the feed
pattern = parse.compile("The Real Python Podcase - Episode #{num:d}: {name}")

# iniffiecient construction because the parse function is called twice.
# podcasts = [
#     pattern.parse(title)["name"]
#     for title in feed.get_titles()
#     if pattern.parse(title)
# ]

# Rewritten podcast extract using the walrus operator
podcasts = [
    podcast["name"]
    for title in feed.get_titles()
    if (podcast := pattern.parse(title))
]

print(feed.get_titles()[:5]) 