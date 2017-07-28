import os
import argparse
from PIL import Image
import xml.etree.ElementTree as et
#import pdb

def parse_args():
	parser = argparse.ArgumentParser(description = 'folder contains images that you want to annotate!')
	parser.add_argument('--f',dest = 'folder')
	args = parser.parse_args()

	return args

def create_xmlfile(images_path, txt_file,class_name):
	""" read images and coordinates of boundingboxes from the text file,
		and then generate the annotation files"""

#	savepath = os.path.join(images_path, "{}_annotations".format(class_name))
#	print "savepath:{}".format(savepath)
#	if not os.path.exists(savepath):
#		os.mkdir(savepath)

	txt = open(txt_file, 'r')
	for line in txt:
#		pdb.set_trace()
		print ('line:{}'.format(line))
		words = line.split(" ")
		word_len = len(words)
		print('length of words:{}'.format(word_len))
		print ("word_len:{}".format(word_len))
		
		if word_len >3:
			a,b = words[0].split('.')
			
			img_path =a+'.jpg' #words[0]
			img_name =img_path # os.path.basename(img_path)
			print ('image Name:%s'%img_name)
			img = Image.open('/home/graymatics/py-faster-rcnn/data/violence/'+img_name)
			print(img)
			w,h = img.size
			#create xml
			annotation = et.Element('annotation')
			et.SubElement(annotation,'folder').text = 'demo'
			et.SubElement(annotation,'filename').text = img_name

			source = et.SubElement(annotation, 'source')
			et.SubElement(source, 'database').text = 'internet'
			et.SubElement(source, 'annotation').text = 'Lyushuen'
			et.SubElement(source, 'image').text = 'unknown'

			size = et.SubElement(annotation, 'size')
			et.SubElement(size, 'width').text = str(w)
			et.SubElement(size, 'height').text =str(h)
			et.SubElement(size, 'depth').text = '3'

			et.SubElement(annotation, 'segmented').text = str(0)
	                for i in range(word_len/4 + 1):
                                print ("I size:{}".format(i))
                                if i == 0:
                                        print "Image name is :{}".format(words[0])
                                elif i >= 1:
                                        index = i - 1

					obj = et.SubElement(annotation, 'object')
					et.SubElement(obj, 'name').text = class_name #words[5]#class_name
					et.SubElement(obj, 'pose').text = 'Unspecified'
					et.SubElement(obj, 'truncated').text = '0'
		   		 	et.SubElement(obj, 'difficult').text = '0'

		    			box = et.SubElement(obj, 'bndbox')
			       		et.SubElement(box, 'xmin').text = str(int(round(float(words[index*4+1]))))
			    		et.SubElement(box, 'ymin').text = str(int(round(float(words[index*4+2]))))
			       		et.SubElement(box, 'xmax').text = str(int(round(float(words[index*4+3]))))
			    		et.SubElement(box, 'ymax').text = str(int(round(float(words[index*4+4]))))

		    #write to file
		   	name, exten = os.path.splitext(img_name)
		   	anno_path = os.path.join(src_img,name+'.xml') #path of annotation files
			print "anno_path:{}".format(anno_path)
		    	tree = et.ElementTree(annotation)
		   	tree.write(anno_path)
	txt.close()

if __name__=="__main__":

#	args = parse_args()
#	folder_path = "/home/shuen/Shuen/datasets/handbag_brands/"
#	subdir = args.folder
#
#	src_img = folder_path + subdir
#	coord_txt = folder_path + "{}_coordinates.txt".format(subdir)
#	print "coord_txt:{}".format(coord_txt)

	src_img = '/home/graymatics/py-faster-rcnn/data/violence/'
	coord_txt = '/home/graymatics/py-faster-rcnn/tools/fight.txt'
	subdir = 'fighting'
        
	create_xmlfile(src_img, coord_txt, subdir)
