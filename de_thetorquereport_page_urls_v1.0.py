#Code Name : de_autoguide_page_urls_v1.0
#Source : www.autoguide.com
#Purpose : Extracting all page urls
#Predecessor :
#Successor :
#Date originally writen : 19/08/2019
#Owner : Kanwar
#Path : D:\Projects\Automotive\Codes\Dev
#Version :

code_path = "D:\\Projects\\Automotive\\Codes\Dev\\"
exec(open(code_path + "global_environment_variables_v1.0.py").read())

all_urls =[]
all_source=[]
all_category =[]

u = 'https://www.thetorquereport.com/category/news/page/'

for k in range(0,1244):

    if k%100==0:
        print(k)

    # category  = u.split('/category/')[1].split('-')[0]

    url = u+str(k)
    all_urls.append(url)
    all_category.append('News')
    all_source.append('The Torque Report')
    
    outdf = pd.DataFrame({'page_url': all_urls,
                       'Category':'News',
                       'Source':all_source})
    outdf = outdf[['Source','Category','page_url']]
    outdf.to_csv(path + 'thetorquereport_page_urls.csv', index=False)



