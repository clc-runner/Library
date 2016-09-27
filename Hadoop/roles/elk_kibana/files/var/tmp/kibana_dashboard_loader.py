#!/usr/bin/python

import argparse

from elasticsearch import Elasticsearch
import json
import sys

def main(argv):
    inputParser = argparse.ArgumentParser()
    inputParser.add_argument("-e", "--elastic", dest="elastic", help="Elasticsearch server hostname and port.")
    inputParser.add_argument("-f", "--file", dest="file", help="Template file to load.", required=True)
    args = inputParser.parse_args()

    data = "".join(open(args.file).readlines())
    json_data = json.loads(data)
    es = Elasticsearch([args.elastic])
    for (r) in json_data:
        res = es.index(index=".kibana",
                       id=r["_id"],
                       doc_type=r["_type"],
                       body=r["_source"])
        print "%s: %s" %(r["_id"], res["created"])
    return


if __name__ == '__main__':
    main(sys.argv[1:])
