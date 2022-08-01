from pygrok import Grok
import yaml

def parse_log(logfile):
    parsed_dict = parse_yaml()
    for pattern in parsed_dict['patterns']:
        grok_pattern = parsed_dict['patterns'][pattern]['grok']
        fields = parsed_dict['patterns'][pattern]['match'].keys()
        match_dict = {}
        for field in fields:
            match_with = parsed_dict['patterns'][pattern]['match'][field]
            match_dict[field] = match_with
        f = open(logfile, 'r')
        lines = f.readlines()
        for line in lines:
            grok = Grok(grok_pattern)
            dict_from_grok = grok.match(line)
            if dict_from_grok:
                matches = True
                for field in match_dict:
                    if dict_from_grok[field] != match_dict[field]:
                        matches = False
                if matches:
                    print('Matched: ',line)


def parse_yaml():
    with open('config.yaml') as f:
        parsed_dict = yaml.safe_load(f)
        return parsed_dict

if  __name__ == '__main__':
    parse_log('test.log')