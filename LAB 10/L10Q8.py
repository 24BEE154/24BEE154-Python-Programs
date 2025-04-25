print("Name:Shubh Raval")
print("Roll no.:24BEE154")
import re

def remove_articles(input_file, output_file):
    pattern = r'\b(a|an|the)\b'

    try:
        with open(input_file, 'r') as infile:
            content = infile.read()
        cleaned_content = re.sub(pattern, ' ', content, flags=re.IGNORECASE)
        cleaned_content = re.sub(r'\s+', ' ', cleaned_content)

        with open(output_file, 'w') as outfile:
            outfile.write(cleaned_content.strip())

        print(f"✅ Cleaned content written to '{output_file}'")
    
    except FileNotFoundError:
        print(f"❌ File '{input_file}' not found.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

remove_articles('original.txt', 'cleaned.txt')
