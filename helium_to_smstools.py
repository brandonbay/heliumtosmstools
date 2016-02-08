import json


def convert_to_smstools_format(input_filename='sms.json', output_filename='output.json'):
    infile = open(input_filename)
    outfile = open(output_filename, 'w')
    data = infile.read()

    for data_item in data.split('|'):
        old_json = json.loads(data_item)
        new_json = {}
        out_data = ''

        new_json['body'] = old_json['body']
        new_json['chatroom'] = None
        new_json['date'] = old_json['date']
        new_json['incoming'] = old_json['type'] == 2
        new_json['members'] = None
        new_json['num'] = old_json['address']

        out_data += json.dumps(new_json)
        out_data += ',\n'
        outfile.write(out_data)

    infile.close()
    outfile.close()
