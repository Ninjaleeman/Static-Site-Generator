import os
from pathlib import Path
from blocknode import markdown_to_html_node


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


def generate_page(from_path, template_path, dest_path, basepath):
  print(f"Generating page from {from_path} to {dest_path} using {template_path}")
#copy mkdown file
  with open(from_path,'r') as markdown_file:
    markdown_content = markdown_file.read()
#copy template
  with open(template_path, 'r') as template_file:
    template_content = template_file.read()
#get title and content
  title = extract_title(markdown_content)
  html_content = markdown_to_html_node(markdown_content).to_html()

#new page based on template with content from mkdown file
  updated_template = template_content.replace('{{ Title }}', title)
  updated_template = updated_template.replace('{{ Content }}', html_content)
  updated_template = updated_template.replace('href="/', 'href="' + basepath)
  updated_template = updated_template.replace('src="/', 'src="' + basepath)
  # Create directories if they don't exist
  os.makedirs(os.path.dirname(dest_path), exist_ok=True)

  # Write the updated template to the destination file
  with open(dest_path, 'w') as dest_file:
      dest_file.write(updated_template)
      
    

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)