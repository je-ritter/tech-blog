

print("Printing Updates:")

# Pages Directory for updating the site.
pages = [
    {
    "filename": "./content/index.html",
    "output": "./docs/python/index.html",
    "title": "Home",
    },
    {
    "filename": "./content/about.html",
    "output": "./docs/python/about.html",
    "title": "About Me",
    },
    {
    "filename": "./content/blog.html",
    "output": "./docs/python/blog.html",
    "title": "Blog",
    }
]

def main ():
    for page in pages:
        header_template = open('./templates/header.html').read()
        footer_template = open('./templates/footer.html').read()
        input_filename = page['filename']
        content = open(input_filename).read()
        # curious about a way to write the if statements more DRY 
        if input_filename == "./content/index.html":
            index_html = header_template + content + footer_template
            open('./docs/index.html', 'w+').write(index_html)
        if input_filename == "./content/about.html":
            about_html = header_template + content + footer_template
            open('./docs/about.html', 'w+').write(about_html)
        if input_filename == "./content/blog.html":
            blog_html = header_template + content + footer_template
            open('./docs/blog.html', 'w+').write(blog_html)
            
# Prints out pages. Seem to be if the main is working, everything prints out.            
for page in pages:
    page_title = page['title']
    main ()
    print(page_title)



