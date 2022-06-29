print("printing a static site")

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


