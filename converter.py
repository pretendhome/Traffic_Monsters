import pandas as pd
import simplejson as json
import codecs

data = input("Enter file directory for data: ")

c_data = pd.read_table(data, sep='\t', encoding='utf-8')

print("\n", c_data.head(5))

wc_data = c_data.count()

#c_data = c_data.drop(['mean_popularity_score'], axis=1)

print("\n""catalog row count: ""\n", wc_data)

file_format = input("\n""Enter the file format you want the catalog in tsv/json: ")
if file_format == 'tsv':
    # write tsv catalog into .tsv file
    write_filename = input("\n""Enter the output directory along with file_name :")
    with open(write_filename, 'w') as write_tsv:
        write_tsv.write(c_data.to_csv(sep='\t', index=False, header=False))
else:
    json_dict = ({"entities": [{"data": {"name": v}} for k, v in c_data.placeName.to_dict().items()]})

    #write json catalog into .json file
    write_json_filename = input("\n""Enter the output directory along with json file_name :")
    with codecs.open(write_json_filename, 'w', encoding='utf8') as write_json:
        #write_json.write(json.dump(json_dict))
        json.dump(json_dict, write_json, ensure_ascii=False)