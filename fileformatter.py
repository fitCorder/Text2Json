import itertools
import json

def generate_json(input_file_name, output_file_name):
    # Reading the content of the provided file
    with open(input_file_name, 'r') as file:
        file_content = file.readlines()

    # Parsing the file content
    urls = []
    base_prompt = ""
    outfits = []
    scenes = []
    negative_prompts = []

    for line in file_content:
        if line.startswith('URL'):
            urls.append(line.split(':', 1)[1].strip().strip('"'))
        elif line.startswith('BASE'):
            base_prompt = line.split(':', 1)[1].strip().strip('"')
        elif line.startswith('OUTFIT'):
            outfits.append(line.split(':', 1)[1].strip().strip('"'))
        elif line.startswith('SCENE'):
            scenes.append(line.split(':', 1)[1].strip().strip('"'))
        elif line.startswith('NEG'):
            negative_prompts.append(line.split(':', 1)[1].strip().strip('"'))

    # Creating combinations of outfits and scenes
    variable_combinations = itertools.product(outfits, scenes)

    # Generating all combinations with URLs and negative prompts
    combinations = itertools.product(urls, variable_combinations, negative_prompts)

    # Formatting the combinations into the desired JSON structure
    json_data = []

    for url, (outfit, scene), neg_prompt in combinations:
        entry = {
            "openpose_url": url,
            "template": base_prompt + " " + outfit + ", " + scene,
            "negative_prompt": neg_prompt,
            "count": 1
        }
        json_data.append(entry)

    # Converting to JSON format and writing to output file
    with open(output_file_name, 'w') as file:
        json.dump(json_data, file, indent=4)

# Example usage
input_file_name = 'autojson.txt'  # Name of your input file
output_file_name = 'autojson_output.json'  # Name for the output JSON file
generate_json(input_file_name, output_file_name)
