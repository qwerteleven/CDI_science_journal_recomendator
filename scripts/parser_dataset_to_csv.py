

def write_file(f, features):

    for article in features:
        f.write('¡'.join(article))
        f.write('\n')




def parse_file(file):

    f = open(file, encoding="utf8")

    features = []

    article_features = []

    for line in f:

        words = line.split(' ')

        if line.split('{')[0] == '@article':
            article_features.append(line.split('{')[-1][:-2])

        if words[0] == 'title':
            process_line = line.split('{')[-1]
            article_features.append(process_line[:-3])

        if words[0] == 'keywords':
            process_line = line.split('{')[-1]
            process_line = process_line[:-2].split(',')
            article_features.append('='.join(process_line[:-1]))

        if words[0] == 'abstract':
            process_line = line.split('{')[-1][:-2]
            article_features.append(process_line)
            features.append(article_features)
            article_features = []


    f.close()

    return features




def main(files):

    f = open('../dataset/features.csv', 'w', encoding="utf-8")

    for file in files:
        features = parse_file(file)
        write_file(f, features)

    f.close()

    print('Done')

if __name__ == '__main__':

    files = [
        '../dataset/journal_1.bib',
        '../dataset/journal_2.bib',
        '../dataset/journal_3.bib',
        '../dataset/journal_5.bib'
    ]

    main(files)