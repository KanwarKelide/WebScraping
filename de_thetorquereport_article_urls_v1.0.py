#Code Name : de_autoguide_article_urls_v1.0
#Source :
#Purpose : Extracting article urls and title from each page
#Predecessor : de_autoguide_page_urls_V1.0
#Successor : generate_autoguide_article_id_v1.0
#Date originally writen : 19/08/2019
#Owner : Kanwar
#Path : D:\Projects\Automotive\Codes\Dev


#code_path = "D:\\Projects\\Automotive\\Codes\Dev\\"
exec(open(code_path + "global_environment_variables_v1.0.py").read())

df = pd.read_csv(path + 'test_url.csv')
print(len(df))
import datetime
all_article_urls = []
all_title=[]
all_source =[]
all_category =[]
all_date_posted=[]
all_aid=[]
all_failed =[]

for k in range(12):

    if k%100==0:
        print(k)

    u = df.iloc[k]['page_url']
    category = df.iloc[k]['Category']
    source = df.iloc[k]['Source']
    #print(u)
    page = requests.get(u).content
    page = str(page)
    soup = BeautifulSoup(page,'html.parser')

    #for i in soup.find_all('h3'):
        j = str(i)
        if 'class="entry-title td-module-title"' in j:
            url = j.split('href="')[1].split('"')[0].strip()
            title = j.split('</a')[0].split('">')[-1].replace('&amp;',' and ').strip()
            title = remove_unicode(title)
            print(url)
            print(title)
            all_article_urls.append(url)
            all_title.append(title)

    for d in soup.find_all('time'):
        jj=str(d)
        if 'class="entry-date updated td-module-date"' in jj:
            dp = jj.split('</time>')[0].split('>')[-1].replace(',','').strip()
            dp = datetime.datetime.strptime(dp,'%B %d %Y')
            date_posted = datetime.date.strftime(dp,'%d-%m-%Y')
            #print date_posted
            all_date_posted.append(date_posted)
            all_source.append(source)
            all_category.append(category)


    outdf = pd.DataFrame({"Source": all_source,
                          'Category':all_category,
                          'article_url': all_article_urls,
                          'article_title':all_title,
                          'date_posted':all_date_posted})
    outdf = outdf.drop_duplicates(subset=['article_title'],keep='first')
    outdf = outdf[['Source','Category','article_url','article_title','date_posted']]
    outdf.to_csv(path+'thetorquereport_article_urls.csv',index=False)
    #
