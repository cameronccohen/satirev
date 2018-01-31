from bs4 import BeautifulSoup
import glob, os, urllib2, urllib, re
import unicodecsv as csv


# download all images to directory
img_dir = "images_temp/"

# store urls in a set
urlset = set()

# open xml sitemap on old site
soup = BeautifulSoup(urllib2.urlopen("http://satirev.org/sitemap.xml"), "html5lib")

# extracting all links, less the first one (which is always the index)
for link in soup.findAll('loc')[1:]:
    urlset.add(link.text)

metadata = []  

#iterating through urlset  
count = 0
for url in urlset:
    count +=1
    #opening article
    soup = BeautifulSoup(urllib2.urlopen(url).read(), "html5lib")

    # extract category
    category = soup.select("#article-content > div.field.field-name-field-category.field-type-taxonomy-term-reference.field-label-above > div.field-items > div > a")[0].text

    # extract title
    title =  soup.find(property = "dc:title")["content"]    

    # some articles don't have images; if not, leave null
    img_url = ""
    img_filename = ""
    caption = ""
    try:
        # extract image url
        img_elem = soup.select("#article-picture > div.field.field-name-field-image.field-type-image.field-label-hidden > div > div > img")[0]
        img_url = img_elem["src"]

        # download image, store filename
        #img_filename = img_url.split('/')[-1]
        #img_filename = img_filename.split("?itok")[0]

        #dir_to_download = img_dir + img_filename
        #urllib.urlretrieve(img_url, dir_to_download)
        
        # extract caption
        caption = soup.select("#article-caption > div > div > div")[0].text
    except IndexError:
        pass

    # extract text content
    full_text = soup.select("#article-content > div.field.field-name-body.field-type-text-with-summary.field-label-hidden > div > div")[0]
    text = ''.join(['%s' % x for x in full_text.findChildren(recursive=False)])
    # remove outer div tag
    #print text.findChildren()

    #print text.get_text(' ', strip=False)
    #try:
    #    text = ' '.join(soup.select("#article-content > div.field.field-name-body.field-type-text-with-summary.field-label-hidden > div > div")[0].findAll('p'))
    #except:
    #    pass
    #print text
    #print "\n \n \n"

    # extract tags, some don't have
    tags = []

    try:
        tag_elems = soup.select("#article-content > div.field.field-name-field-tags.field-type-taxonomy-term-reference.field-label-above > div.field-items")[0]
        for tag in tag_elems:
            tags.append(tag.text)
    except IndexError:
        pass
    
    metadata.append([title,category,(img_url,img_url,caption),text,tags])

    if count >= 30:
        break

for idx,article in enumerate(metadata):
    image = article[2]
    a = re.search("(?:jpg|gif|png|jpeg|JPG)", image[0])
    if a is not None:
        new_name = str(idx+1) + "." + re.search("(?:jpg|gif|png|jpeg|JPG)", image[0]).group(0)
        #urllib.urlretrieve(image[0], img_dir+new_name)
        #new_name = "/images/" + new_name
        article[2] = (new_name, image[0], image[1])




# image_list = []
# tag_set = set()
# tag_list = []
# sections = {"Harvard" : 1, "U.S." : 2, "Region" : 3, "World" : 4, "Opinion" : 5, "Everything Else" : 6}

# for article in metadata[:]:
#     image = article[2]
#     if image not in image_list:
#         a = re.search("(?:jpg|gif|png|jpeg|JPG)", image[0])
#         if a is not None:
#             img_id = len(image_list)+1
#             new_name = img_dir + str(img_id) + "." + re.search("(?:jpg|gif|png|jpeg|JPG)", image[0]).group(0)
#             caption = image[1]
#             urllib.urlretrieve(image[0], new_name)
#             image_list.append([new_name,caption])

#             article[2] = img_id 

#     else:
#         article[2] = image_list.index(image)+1

#     article_tags = article[4]
#     for idx,tag in enumerate(article_tags):
#         if tag not in tag_set:
#             tag_id = len(tag_list)+1
#             tag_list.append([tag])
#             article_tags[idx] = tag_id
#         else:
#             article_tags[idx] = tag_list.index(tag)+1

#     article[4] = article_tags

#     article[1] = sections[article[1]]

# image_list = [[idx+1,image[0],image[1]] for idx, image in enumerate(image_list)]
# tag_list = [[idx+1,tag[0]] for idx, tag in enumerate(tag_list)]



# def find_in_list():
# write new function that goes through existing set / list - has to find if the list contains the elemtn NOT including the id num
# or just dont have the id nums in the original list, just do that at the end when everything been added to list 



#print tag_list

# save tags
# tag_set = set()
# tag_dict = {}
# for x in metadata:
#     for y in x[4]:
#         tag_set.add(y)
# tag_list = list(tag_set)

# #creating image csv
# image_set = set()
# for x in metadata:
#         if x[2] != "":
#             image_set.add(x[2])

# image_list = list(image_set)
# print image_list
# new_image_list = []
# image_dict ={}
# for x in range(len(image_list)):
#     a = re.search("(?:jpg|gif|png|jpeg|JPG)", image_list[x][0])
#     if a is not None:
#         new_name = img_dir + str(x+1) +"." + re.search("(?:jpg|gif|png|jpeg|JPG)", image_list[x][0]).group(0)
#         caption = image_list[x][1]
#         image_dict[image_list[x]] = (new_name, caption)

#         urllib.urlretrieve(image_list[x][0], new_name)
#         new_image_list.append([x+1, new_name, caption])

# # change image src
# for post in metadata:
#     post[2] = image_dict[post[2]]

# with open("imageinfo.csv",'wb') as file:
#    writer = csv.writer(file)
#    for x in image_list:
#     writer.writerow(x)


# with open("tags.csv",'wb') as file:
#     writer = csv.writer(file)
#     for x in tag_list:
#         writer.writerow(x)

with open("metadata.csv",'wb') as file:
    writer = csv.writer(file)
    for l in metadata:
        # flatten lists into 'tab' separated so they can be read in
        l[2] = "    ".join(l[2])
        l[4] = "    ".join(l[4])

        writer.writerow(l)


# later things to do

#storing old urls of images - have to then download the image and save new url