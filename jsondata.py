import json

def load_dataset(file_name):
    """Load the json file for dataset"""
    print('Opening {}...'.format(file_name))

    # Opening JSON file
    with open(file_name, "r") as f:
        # returns JSON object as a dictionary
        data = json.load(f)

    # process data here
    # print(data)
    # iplist = [{'ip': item['ip'], 'domain': item['domainName']} for item in data if 'port' in item and item['port'] == '443']
    # print(iplist)

    # iplist = [{'ip': item['ip'], 'domain': item['domainName'], 'Age': resp['value']} for item in data if 'response' in item for resp in item['response']['httpHeaders'] if resp['name'] == 'Age']
    # print(json.dumps(iplist, indent=4))
    # print(data["response"]["httpHeaders"])

    mlist = []
    for item in data:
        if 'response' in item:
            for resp in item['response']['httpHeaders']:
                if resp['name'] == 'Age':
                    mdict = {'ip': item['ip'], 'domain': item['domainName'], 'Age': resp['value']}
                    mlist.append(mdict)
    
    print(json.dumps(mlist, indent=4))
    # Closing file
    # f.close()


def main():
    """A dummy wrapper around print."""
    load_dataset("dataset.json")

if __name__ == '__main__':
    main()
