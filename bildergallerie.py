from os import walk

_, _, filenames = next(walk('img'))

html = """
<html>
  <head>
    <title></title>
    
    <style>
        img {
          width: 400px;
          height: 150px;
          object-fit: cover;
        }
    </style>
  </head>
  <body>
"""

for f in filenames:
    html += '<img src="img/' + f + '">'

html += """
  </body>
</html>
"""

print(html)

# Write HTML String to file.html
with open("index.html", "w") as file:
    file.write(html)
