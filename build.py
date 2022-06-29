print("printing a static site")

def main():
    header_template = open('./templates/header.html').read()
    footer_template = open('./templates/footer.html').read()

    content = open('./content/index.html').read()
    index_html = header_template + content + footer_template
    open('./docs/python/index.html', 'w+').write(index_html)

    content = open('./content/blog.html').read()
    blog_html = header_template + content + footer_template
    open('./docs/python/blog.html', 'w+').write(blog_html)

    content = open('./content/about.html').read()
    about_html = header_template + content + footer_template
    open('./docs/python/about.html', 'w+').write(about_html)


# pages = [
#     {
#    "filename": "./content/index.html",
#    "output": "./docs/python/index.html",
#    "title": "Home",
#    },
#    {
#    "filename": "./content/about.html",
#    "output": "./docs/python/about.html",
#    "title": "About Me",
#    },
#    {
#    "filename": "./content/blog.html",
#    "output": "./docs/python/blog.html",
#    "title": "Blog",
#    },
#]

#page_title = page; [’title’]
#print(page_title)

#for page in pages:
#    print(page_title)


main()

