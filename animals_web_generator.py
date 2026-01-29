import os
import data_fetcher  # your modular API fetcher

def serialize_animal(animal):
    """Convert any animal dictionary to an HTML card."""
    output = '<li class="cards__item">\n'

    # Name
    if "name" in animal:
        output += f'<div class="card__title">{animal["name"]}</div>\n'

    output += '<p class="card__text">\n'

    # Loop over all top-level keys except 'name'
    for key, value in animal.items():
        if key == "name":
            continue
        # If value is a dict, list each subkey
        if isinstance(value, dict):
            for subkey, subvalue in value.items():
                output += f'<strong>{subkey.capitalize()}:</strong> {subvalue}<br/>\n'
        # If value is a list, join as string
        elif isinstance(value, list):
            output += f'<strong>{key.capitalize()}:</strong> {", ".join(value)}<br/>\n'
        else:
            output += f'<strong>{key.capitalize()}:</strong> {value}<br/>\n'

    output += '</p>\n</li>\n'
    return output

def main():
    animal_name = input("Please enter an animal: ")

    animals_data = data_fetcher.fetch_data(animal_name)

    # Exact match filtering
    animals_data = [
        a for a in animals_data
        if a.get("name", "").strip().lower() == animal_name.strip().lower()
    ]

    if not animals_data:
        print("No animals found. Have you specified a correct animal name?")
        animals_string_data = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'
    else:
        print("The animal '" + animal_name + "' already exists.")
        animals_string_data = ""
        for animal in animals_data:
            animals_string_data += serialize_animal(animal)

    # Load template
    template_path = os.path.join(os.path.dirname(__file__), "animals_template.html")
    with open(template_path, "r", encoding="utf-8") as file:
        template_content = file.read()

    # Replace placeholder
    template_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_string_data)

    # Save HTML
    output_path = os.path.join(os.path.dirname(__file__), "animals.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(template_content)

    print("Website successfully generated: animals.html")


if __name__ == "__main__":
    main()
