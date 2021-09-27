#! python3
"""
|code to evaluate all the attributes and methods of an object
|for example, can use requests to get a response type object, and then evalute all of the
|items in the dir(request object) to see the results
"""

import requests, pprint



def dirlist():
	i = 0
	for items in dir(sitelink):
		print('\n~~' + str(i) + '-> ' + str(dir(sitelink)[i]))
		try:

			if (dir(sitelink)[i]).startswith('__'):
##				print(str(dir(sitelink)[i]).strip('__'))
				print('\t' + str(eval( (str(dir(sitelink)[i])).strip('__')+'('+'sitelink'+')')))
				i += 1

##			elif (dir(sitelink)[i]).startswith('_'):
##				print(str(dir(sitelink)[i]).strip('_'))
##				print(eval((dir(sitelink)[i]).strip('_')+'('+'sitelink'+')'))
##				i += 1


			else:
##				print(dir(sitelink)[i])
				print('\t' + str(getattr(sitelink,dir(sitelink)[i])))
				i +=1

		except:
			i += 1

if __name__ == '__main__':

    sitelink = requests.get('http://www.automatetheboringstuff.com')
    dirlist()
    print('done')
