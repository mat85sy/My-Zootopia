import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

# --- Configuration ---
JSON_FILE_PATH = 'animals_data.json'  # Updated filename
TEMPLATE_FILE_PATH = 'animals_template.html'  # Make sure this file exists
OUTPUT_FILE_PATH = 'animals.html'
PLACEHOLDER = '__REPLACE_ANIMALS_INFO__'
# --- End Configuration ---

# 1. Load the animal data from JSON
animals_data = load_data(JSON_FILE_PATH)

# 2. Generate the string with animals' data in the NEW HTML format
animals_info_string = ''  # define an empty string to accumulate HTML data

for animal in animals_data:
    # Start the list item for this animal
    animals_info_string += '<li class="cards__item">\n'

    # Add the title div
    animals_info_string += f'  <div class="card__title">{animal["name"]}</div>\n'

    # Start the text paragraph
    animals_info_string += '  <p class="card__text">\n'

    # Add Diet (from characteristics)
    diet = animal.get('characteristics', {}).get('diet')
    if diet:
        animals_info_string += f'      <strong>Diet:</strong> {diet}<br/>\n'

    # Add the first Location
    locations = animal.get('locations', [])
    if locations:
        animals_info_string += f'      <strong>Location:</strong> {locations[0]}<br/>\n'

    # Add Type (from characteristics)
    animal_type = animal.get('characteristics', {}).get('type')
    if animal_type:
        animals_info_string += f'      <strong>Type:</strong> {animal_type}<br/>\n'

    # Close the text paragraph and the list item
    animals_info_string += '  </p>\n'
    animals_info_string += '</li>\n'

# 3. Read the content of the template
try:
    with open(TEMPLATE_FILE_PATH, "r") as template_file:
        template_content = template_file.read()
except FileNotFoundError:
    print(f"Error: Template file '{TEMPLATE_FILE_PATH}' not found.")
    exit(1)

# 4. Replace the placeholder with the generated HTML string
final_html_content = template_content.replace(PLACEHOLDER, animals_info_string)

# 5. Write the new HTML content to a new file
with open(OUTPUT_FILE_PATH, "w") as output_file:
    output_file.write(final_html_content)

print(f"Generated {OUTPUT_FILE_PATH} successfully!")

