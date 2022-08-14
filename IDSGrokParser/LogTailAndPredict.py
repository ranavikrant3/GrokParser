import time
import pickle
import logging
from pygrok import Grok
import yaml

logging.basicConfig(filename='ids.log',
                    filemode='a',
                    format='%(asctime)s %(name)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)
logger = logging.getLogger('GrokIDSLogger')
file = open("test.log", "r")

def parse_yaml():
    with open('config.yaml') as f:
        parsed_dict = yaml.safe_load(f)
        return parsed_dict

def check_if_sqli(line):
    parsed_dict = parse_yaml()
    for pattern in parsed_dict['patterns']:
        grok_pattern = parsed_dict['patterns'][pattern]['grok']
        fields = parsed_dict['patterns'][pattern]['match'].keys()
        match_dict = {}
        for field in fields:
            match_with = parsed_dict['patterns'][pattern]['match'][field]
            match_dict[field] = match_with
        grok = Grok(grok_pattern)
        dict_from_grok = grok.match(line)
        if dict_from_grok:
            matches = True
            for field in match_dict:
                if match_dict[field] not in dict_from_grok[field]:
                    matches = False
            if matches:
                return True
    return False


while True:
    pos = file.tell()
    line = file.readline()
    if not line:
        time.sleep(1)
        file.seek(pos)
    else:
        logline = line.strip()
        query = line.strip().split("INFO")[1]
        if check_if_sqli(logline):
            logger.info('Possible SQLI Attempt: '+query)
        else:
            logger.info('Logging input: '+query)