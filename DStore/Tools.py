import os
import datetime
def cached_url(url):
    folder='cached_url'
    filename=url.split('?')[1].split('&')[0].split('=')[1]+'.html'
    path=os.path.join(folder,filename)
    #if has cached,return
    if os.path.exists(path):
        with open(path,'rb') as f:
            s=f.read();
            return s
    else:
        #save url to cache file
        if not os.path.exists(folder):
            os.mkdir(folder)
        html=get_html_text(url,HEADERS,format_cookie(COOKIES))
        if html!=-1:
            with open(path,'wb') as f:
                f.write(html)
            return html
        else:
            print ('{}download fail!'.format(filename))
            return -1

def format_to_week(day):
    day_map={
        0:'week yi',
        1:'week er',
        2:'week san',
        3:'week si'
    }
    week=datetime.strptime(day,"%Y-%m-%d").weekday()
    return day_map[week];