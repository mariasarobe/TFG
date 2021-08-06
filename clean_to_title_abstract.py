import re
import os



folder_2='/Users/mariasarobebove/Desktop/TFG_2/3d printing corpus clean/lol'

def clean_to_title_abstract(folder):
    abstracts = [os.path.join(folder, f) for f in os.listdir(folder)]
    for abstract in abstracts:
        with open(abstract, 'r') as f:
            content = f.read()
        try:
            text0 = re.search(r'PMID-(.*?)OWN -', content, re.DOTALL).group(1)
            file_name = str(folder_2 + text0[1:-1] + '.txt')
            date = re.search(r'DP  -(.*?)TI  -', content, re.DOTALL).group(1)
            text1 = re.search(r'TI  -(.*?).  -', content, re.DOTALL).group(1)
            with open(file_name, "a") as file:
                file.write(date)
                file.write(text0)
                file.write(text1)
            try:
                text2 = re.search(r'AB  -(.*?)CI  -', content, re.DOTALL).group(1)
                with open(file_name, "a") as file:
                    file.write(text2)
            except AttributeError:
                print(text0[:-1] + ': no abtract text on first try')
                
                try:
                    text3 = re.search(r'AB  -(.*?)FAU -', content, re.DOTALL).group(1)
                    with open(file_name, "a") as file:
                        file.write(text3)
                except AttributeError:
                    print(text0[:-1] + ': no abstract at all')
                    os.remove(file_name)
                    continue
        except:
            print('no PMID')
            continue
