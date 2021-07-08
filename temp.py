import json
import requests

dict1 = [{'groupid':'3010','status':'active'},{'groupid':'3010','status':'active'},{'groupid':'200',
            'status':'failed'}]

lst = []
for asset in dict1:
    dict2 = {}
    dict2['groupid'] = asset['groupid']
    dict2['status'] = asset['status']
    if dict2 not in lst:
        lst.append(dict2)
    '''
    if asset['groupid'] not in lst:
        dict2['groupid'] = asset['groupid']
        dict2['status'] = asset['status']
        lst.append(dict2)
     '''   
