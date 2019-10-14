#Code Name : de_thetruthaboutcars_paragraph_V1.0
#Source :https://www.thetruthaboutcars.com
#Purpose : Extracting paragraphs from each article
#Predecessor :  generate_thetruthaboutcars_article_id_v1.0
#Successor : de_thetruthaboutcars_sentence_master_V1.0
#Date originally writen : 27/08/2019
#Owner : Sangameshwar
#Path : D:\Projects\Automotive\Codes\Dev
#Version :

code_path = "D:\\Projects\\Automotive\\Codes\Dev\\"
exec(open(code_path + "global_environment_variables_v1.0.py").read())

df = pd.read_csv(path+'aggregated_article_master.csv')
print len(df)
df = df[(df['Source']=='Truth About Cars')]
print len(df)

all_paragraphs = []
all_paragraph_id = []
all_article_id = []
all_failed = []

s= 0
e = 5

for z in range(s,e):
    if z%500==0:
        print(z)

    u = df.iloc[z]['article_url']
    print u
    aid = df.iloc[z]['article_id']

    try:
        page = requests.get(u).text
        page = page[page.find('<div class="postbody">'):]
        page = page[:page.find('<!-- end postbody -->')]

        page = page.replace('\\r', '').replace('\\n', '').strip()
        soup = BeautifulSoup(page, "html.parser")

        soup_vector = soup.find_all('p')

        for k in range(len(soup_vector)):
            k2 = soup_vector[k]
            j = str(k2)
            j1 = join_lines(j)
            h = strip_tags(j1)
            h = h.replace(u"\u2019", "'")
            h = h.replace(u'\u20B9', "Rs ")
            h = h.replace(u"\u0024", "$")
            para = byteify(h).decode('unicode_escape').encode("ascii", "ignore").replace("&#8377;", "Rs ").replace('&amp;', '&').replace('"', '')

            if len(para.split()) > 3:
                para_id = aid + "_" + str(k + 1)
                all_paragraphs.append(para)
                all_paragraph_id.append(para_id)
                all_article_id.append(aid)

        outdf = pd.DataFrame({'article_id': all_article_id,
                              'paragraph_id': all_paragraph_id,
                              'Paragraph': all_paragraphs})
        outdf = outdf[['article_id', 'paragraph_id', 'Paragraph']]
        outdf.to_csv(path + 'thetruthaboutcars_paragraph_master_' + str(s) + "_" + str(e) + "_.csv", index=False)

    except:
        all_failed.append(u)
        pd.DataFrame({"article_url": all_failed}).to_csv(path + 'thetruthaboutcars_failed_urls_' + str(s) + "_" + str(e) + '.csv', index=False)

