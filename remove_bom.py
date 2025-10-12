# remove_bom.py
input_file = "data_clean.json"
output_file = "data_final.json"

with open(input_file, "rb") as f:
    content = f.read()

# Remove UTF-8 BOM if it exists
if content.startswith(b'\xef\xbb\xbf'):
    content = content[3:]

with open(output_file, "wb") as f:
    f.write(content)

print("✅ BOM removed successfully and saved as data_final.json")
