import os
import re

# Folder name mapping (removing spaces)
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
            print(f"Renamed: '{old_name}' → '{new_name}'")

# Function to update paths inside HTML files
def update_html_links():
    html_folder = "html"  # Updated folder name
    if not os.path.exists(html_folder):
        print("Error: HTML folder not found after renaming!")
        return
    
    for file in os.listdir(html_folder):
        if file.endswith(".html"):
            file_path = os.path.join(html_folder, file)

            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Replace old paths with corrected ones
            content = re.sub(r'href="HTML Files/(.*?)"', r'href="/html/\1"', content)
            content = re.sub(r'href="CSS Files/(.*?)"', r'href="/css/\1"', content)
            content = re.sub(r'src="Js Files/(.*?)"', r'src="/js/\1"', content)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            
            print(f"Updated links in: {file}")

# Function to update the vercel.json file
def update_vercel_json():
    vercel_config = {
        "routes": [
            { "src": "/(.*)", "dest": "/html/index.html" },
            { "src": "/css/(.*)", "dest": "/css/$1" },
            { "src": "/js/(.*)", "dest": "/js/$1" },
            { "src": "/html/(.*)", "dest": "/html/$1" }
        ]
    }
    
    import json
    with open("vercel.json", "w", encoding="utf-8") as f:
        json.dump(vercel_config, f, indent=4)
    
    print("✅ Updated vercel.json")

# Execute the fixes
rename_folders()
update_html_links()
update_vercel_json()

print("\n✅ All fixes applied successfully! Your project is ready for deployment.")
