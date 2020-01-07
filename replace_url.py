#!/usr/bin/env python

import sys
import json

def run():
    if len(sys.argv) != 3:
        print('usage: {} <config_file> <url>'.format(sys.argv[0]))
        exit(1)

    config_file_name = sys.argv[1]
    url = sys.argv[2]

    with open(config_file_name, 'r') as config_file:
        data = json.load(config_file)

    values = data['values']
    url_obj = next((e for e in values if e.get('key') == 'URL'), None)
    
    if url_obj is not None:
        url_obj['value'] = url
    else:
        print('Error: could not find URL key in config file, aborting')
        exit(1)

    with open(config_file_name, 'w') as config_file:
        data = json.dump(data, config_file)

if __name__ == '__main__':
    run()
