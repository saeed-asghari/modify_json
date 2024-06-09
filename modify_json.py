import json
import uuid
import pyperclip

def modify_json_key(json_data, key):
    def recursive_modify(d):
        if isinstance(d, dict):
            for k, v in d.items():
                if k == key:
                    d[k] = str(uuid.uuid4())
                elif isinstance(v, dict):
                    recursive_modify(v)
    recursive_modify(json_data)
    return json_data

def main():
    file_path = 'data.json'
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
    except FileNotFoundError:
        print(f"file '{file_path}' not found")
        return
    except json.JSONDecodeError:
        print("Invalid JSON format.")
        return

    key = input("Input Key ").strip()
    
    if not key:
        print("No key entered.")
        return

    modified_json = modify_json_key(json_data, key)

    modified_json_str = json.dumps(modified_json, ensure_ascii=False, indent=4)

    pyperclip.copy(modified_json_str)
    print("The new Json was saved to the clipboard.")

if __name__ == "__main__":
    main()
