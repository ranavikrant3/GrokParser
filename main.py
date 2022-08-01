from pygrok import Grok
import yaml

def parse_log(logfile):
    parsed_dict = parse_yaml()
    for pattern in parsed_dict['patterns']:
        grok_pattern = parsed_dict['patterns'][pattern]['grok']
        fields = parsed_dict['patterns'][pattern]['match'].keys()
        for field in fields:

            match_with = parsed_dict['patterns'][pattern]['match'][field]
            print(field, match_with)
        f = open(logfile, 'r')
        lines = f.readlines()
        for line in lines:
            grok = Grok(grok_pattern)
            matched_grok_dict = grok.match(line)
            #print(matched_grok_dict)
            if matched_grok_dict[field] == match_with:
                print(line)




def parse_yaml():
    with open('config.yaml') as f:
        parsed_dict = yaml.safe_load(f)
        return parsed_dict





if  __name__ == '__main__':
    parse_log('testfile.log')