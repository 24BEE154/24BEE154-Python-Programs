print("Name:Shubh Raval")
print("Roll no:24BEE154")
def copy_with_uppercase(source_file, destination_file):
    try:
        
        with open(source_file, 'r') as src:
            content = src.read()
        upper_content = content.upper()

        with open(destination_file, 'w') as dest:
            dest.write(upper_content)

        print(f"✅ File copied from '{source_file}' to '{destination_file}' with uppercase transformation.")
    
    except FileNotFoundError:
        print(f"❌ Source file '{source_file}' not found.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")
copy_with_uppercase('input.txt', 'output.txt')
