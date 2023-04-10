def exists_word(word, instance, search_word=False):
    search = []
    word = word.lower()

    for item in instance.items:
        occurrences = []
        for line_number, line in enumerate(item["linhas_do_arquivo"], 1):
            if word in line.lower():
                occurrences.append({
                        "linha": line_number
                    } if not search_word else {
                        "linha": line_number,
                        "conteudo": line
                    })
        if occurrences:
            search.append({
                "palavra": word,
                "arquivo": item["nome_do_arquivo"],
                "ocorrencias": occurrences
            })

    return search


def search_by_word(word, instance):
    return exists_word(word, instance, True)
