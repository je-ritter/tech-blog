




print("Printing Updates:")

# Pages Directory for updating the site.
pages = [
    {
    "filename": "./content/index.html",
    "output": "./docs/index.html",
    "title": "Jake Ritter | Home",
    },
    {
    "filename": "./content/about.html",
    "output": "./docs/about.html",
    "title": "Jake Ritter | About Me",
    },
    {
    "filename": "./content/blog.html",
    "output": "./docs/blog.html",
    "title": "Jake Ritter | Blog",
    }
]


#Preps Pages and starts template creation
def apply_template():
    template = open("./templates/base.html").read()
    input_content = open(page["filename"]).read()
    active_link = " active"
    updated_title = page["title"]

    new_page = template.replace("{{content}}", input_content)
    new_title = new_page.replace("{{title}}", updated_title)
    if new_title == "Jake Ritter | Home":
        active_home = new_page.replace("{{active_1}}", active_link)
    else:
        if new_title == "Jake Riter | About Me":
            active_about = new_page.replace("{{active_2}}", active_link)
        else:
            if new_title == "Jake Riter | Blog":
                active_blog = new_page.replace("{{active_3}}", active_link)
            else:
                print("whoop de doo")
    final_page = active_home; active_about; active_blog
    return final_page



#Finishes and writes updated pages
def main():
    output = page["output"]
    open(output, "w+").write(final_page)

#Prints out Page Titles in Terminal    
def updates():
    page_title = page["title"]
    print(page_title)

for page in pages:
    final_page = apply_template()
    main()
    updates()





#def apply_template(content): 
# TODO: Read in template, do string replacing, and return result
#return results
#def main():
#content = open(’docs/index.html’).read()
#resulting_html_for_index = apply_template(content)

        


