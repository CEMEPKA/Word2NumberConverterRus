import number_convertor

__g_path_to_file = "./example.txt"


def get_file_content(path_to_file: str) -> str:
    try:
        with open(file=path_to_file, mode="r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError as e:
        print(e)
        return ""
    else:
        return content


def main() -> None:
    content = get_file_content(__g_path_to_file)
    print(f"Исходный текст:\n{content}")
    convertor = number_convertor.NumberConvertor()
    numbered_text = convertor.convert_groups(content)
    print(f"Преобразованный текст:\n{numbered_text}")


if __name__ == "__main__":
    main()
