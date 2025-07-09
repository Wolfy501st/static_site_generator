import os
import shutil
from textnode import TextType, TextNode 
from block_markdown import markdown_to_html_node, extract_title


def copy_static_files(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
        print(f"Deleted existing directory: {dest}")

    def recursive_copy(current_src, current_dest):
        os.makedirs(current_dest, exist_ok=True)
        for entry in os.listdir(current_src):
            src_path = os.path.join(current_src, entry)
            dest_path = os.path.join(current_dest, entry)
            if os.path.isdir(src_path):
                recursive_copy(src_path, dest_path)
            else:
                shutil.copy2(src_path, dest_path)
                print(f"Copied: {src_path} -> {dest_path}")

    recursive_copy(src, dest)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read markdown file
    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    # Read template file
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    # Extract title
    title = extract_title(markdown_content)

    # Replace placeholders
    page_content = template_content.replace("{{ Title }}", title)
    page_content = page_content.replace("{{ Content }}", html_content)

    # Ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write to destination file
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(page_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)
        if os.path.isdir(src_path):
            # Recursively process subdirectories
            generate_pages_recursive(src_path, template_path, dest_path)
        elif entry.endswith(".md"):
            # Change .md to .html for output file
            dest_file = os.path.splitext(entry)[0] + ".html"
            dest_file_path = os.path.join(dest_dir_path, dest_file)
            generate_page(src_path, template_path, dest_file_path)

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static_dir = os.path.join(base_dir, "static")
    public_dir = os.path.join(base_dir, "public")
    content_dir = os.path.join(base_dir, "content")
    template_path = os.path.join(base_dir, "template.html")

    # Copy static files
    if not os.path.exists(static_dir):
        print(f"DIRECTORY NOT FOUND: {static_dir}")
        return
    copy_static_files(static_dir, public_dir)

    # Generate HTML pages from markdown in content directory
    if not os.path.exists(content_dir):
        print(f"DIRECTORY NOT FOUND: {content_dir}")
        return
    if not os.path.exists(template_path):
        print(f"TEMPLATE NOT FOUND: {template_path}")
        return

    generate_pages_recursive(content_dir, template_path, public_dir)

    
if __name__ == "__main__":
    main()