#!/usr/bin/env python

import sys, requests

BASE = 'http://www.uniprot.org'
KB_ENDPOINT = '/uniprot/'
TOOL_ENDPOINT = '/uploadlists/'

def map_retrieve(ids2map, source_fmt='ACC+ID',target_fmt='ACC', output_fmt='tab'):
    if hasattr(ids2map, 'pop'):
        ids2map = ' '.join(ids2map)
        payload = { 'query': ids2map,
                    'from': source_fmt,
                    'to': target_fmt,
                    'columns': 'id,go-id,database(interpro),database(PDB)', # we can add whichever database ressources we want
                    'format': output_fmt,
                    }

    response = requests.get(BASE + TOOL_ENDPOINT, params=payload)

    if response.ok:
        return response.text
    else:
        response.raise_for_status()

uniprot_ids = sys.argv[1:] #command line arguments passed to script -> only one input in the script
uniprot_acc = map_retrieve(uniprot_ids, source_fmt='ACC+ID')
sys.stdout.write(str(uniprot_acc)+'\n')
