from blocknode import markdown_to_html_node
from htmlnode import *
import os

def extract_title(markdown):
  lines = markdown.split("\n")
  title = ""
  for line in lines:
    if line.startswith("# "):
      title = line.lstrip("# ")
  
  if len(title) != 0:
    return title
  else:    
    raise Exception("No valid headers")

def generate_files_recursive(source_dir_path, template_path,  dest_dir_path):
    #does destination directory exists
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    #open template 
    with open(template_path, 'r') as file:
      template = file.read()

# list entries in the content dir
    for filename in os.listdir(source_dir_path):
      source_path = os.path.join(source_dir_path, filename)


      if os.path.isfile(source_path):
        if filename.endswith('.md'):
          #create dest path with html ext
          dest_filename = filename[:-3] + '.html' # replacing .md with .html
          dest_path = os.path.join(dest_dir_path, dest_filename)

          #generate page
          with open(source_path, 'r') as md_file:
            md_content = md_file.read()

          #get title and content
          title = extract_title(md_content)
          html_content = markdown_to_html_node(md_content).to_html()

         #new page based on template with content from mkdown file
          updated_template = template.replace('{{ Title }}', title)
          updated_template = updated_template.replace('{{ Content }}', html_content)


          with open(dest_path, 'w') as dest_file:
              dest_file.write(updated_template)

      #if its a directory call it recursivly
      else:
        new_source_dir = source_path
        new_dest_dir = os.path.join(dest_dir_path, filename)
        #recursive call
        generate_files_recursive(new_source_dir, template_path, new_dest_dir)