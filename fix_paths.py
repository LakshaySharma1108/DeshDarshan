import os
import re

# Mapping of old folder names to new ones (removing spaces)
folder_renames = {
    "CSS Files": "css",
    "HTML Files": "html",
    "Js Files": "js"
}

# Function to rename folders
def rename_folders():
    for old_name, new_name in folder_renames.items():
        if os.path.exists(old_name):
            os.rename(old_name, new_name)
            print(f"Renamed '{old_name}' → '{new_name}'")

# Function to update paths in HTML files
def update_html_links():
    html_folder = "html"  # After renaming, this is the new location
    for file in os.listdir(html_folder):
        if file.endswith(".html"):
            file_path = os.path.join(html_folder, file)

            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Replace old paths with new ones
            content = re.sub(r'href="HTML Files/(.*?)"', r'href="/html/\1"', content)
            content = re.sub(r'href="CSS Files/(.*?)"', r'href="/css/\1"', content)
            content = re.sub(r'src="Js Files/(.*?)"', r'src="/js/\1"', content)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            
            print(f"Updated paths in {file}")

# Execute fixes
rename_folders()
update_html_links()

print("✅ Folder names and file references updated successfully!")
