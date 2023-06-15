def exists_word(word, instance):
    result = []

    for i in range(instance.__len__()):
        file = instance.search(i)
        data = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": []
        }
        for j, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                data["ocorrencias"].append({"linha": j + 1})
        if len(data["ocorrencias"]) > 0:
            result.append(data)
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
