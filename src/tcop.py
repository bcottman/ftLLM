# read in a yaml file and return a dictionary
import yaml
import urllib
import bs4 as BeautifulSoup
def read_yaml_file(yaml_file):
    with open(yaml_file, 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            # return None if there is an error in reading the yaml file
            return None
# input the url on command line using --url and the yaml file using --yaml
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', help='url of the website')
    parser.add_argument('--yaml', help='yaml file')
    args = parser.parse_args()
    if args.url:
        links = get_all_links(args.url)
        if links:
            for link in links:
                print(link)
        else:
            print("Error in reading the url")
    elif args.yaml:
        dictionary = read_yaml_file(args.yaml)
        if dictionary:
            print(dictionary)
        else:
            print("Error in reading the yaml file")
    else:
        print("Please provide either url or yaml file")
#read in all links of a website whose url is given as parameter and create or append to urlLinks.yaml
def get_all_links(url):
    try:
        page = urllib.request.urlopen(url)
    except:
        return None
    soup = BeautifulSoup.BeautifulSoup(page)
    links = soup.findAll('a')
    link_list = []
    for link in links:
        link_list.append(link.get('href'))
    # write the links to a yaml file
    with open('urlLinks.yaml', 'w') as outfile:
        yaml.dump(link_list, outfile, default_flow_style=False)
    return link_list
