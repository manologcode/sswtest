import yaml
import sys
import os

from yaml.loader import SafeLoader

class InOutData():


    @staticmethod
    def read_yaml(file_name):
        if os.path.isfile(file_name):
            with open(file_name) as f:
                data = yaml.load(f, Loader=SafeLoader)
            return data

    config=read_yaml('config.yml')

    @staticmethod
    def input_data(config):
        data = {}
        print()
        print()
        print(config['title'])
        divider = '-' * len(config['title'])
        print(divider)
        print()
        for k in config['fields']:
            data[k] = input( config['fields'][k] )
            print()
        print(divider)
        return data

    @staticmethod
    def menu(config):
        ans=True
        divider = '-' * len(config['title'])
        print()
        print(divider)
        print(config['title'])
        print(divider)
        print()
        print(config['description'])
        print()
        for item in config['items']:
            print()
            print(item)
        print()
        print(divider)
        print()
        ans = input("Que opción quieres? ") 
        return ans

    @staticmethod
    def create_yaml_data( name, data):
        file_name = name + ".yml"
        if 'config'  in data and 'name' in data['config']:
            data['config']['name'] = name
        print(f"Creando: {file_name}")
        with open( InOutData.config['folder_export'] + file_name, 'w') as f:
            data = yaml.dump(data, f, sort_keys=False)
    
    @staticmethod
    def name_file_free(path_file_name):
        part = path_file_name.split('.')
        name = part[0]
        ext = part[1]
        path_file_name = f"{name}.{ext}"
        if os.path.isfile(path_file_name):
            counter = 0
            while os.path.isfile(path_file_name):
                counter += 1
                path_file_name = f"{name}({counter}).{ext}"
        return path_file_name

    @staticmethod
    def name_folder_free(path_file_name):
        if os.path.isdir(path_file_name):
            counter = 0
            while os.path.isdir(path_file_name):
                counter += 1
                path_file_name = f"{path_file_name}_{counter}"
        return path_file_name

    @staticmethod
    def read_params():
        response = {}
        if len(sys.argv) > 1:
            param = sys.argv[1]
            path_file = InOutData.config['folder_export'] + param
            if os.path.isfile(path_file):
                response['file'] = path_file
                # response['name'] = InOutData.clean_name(param)
            else:
                print(f'ERROR: El archivo {param} no existe')
        response = response if response!={} else None
        return response

    @staticmethod
    def open_in_browser(url_relative):
        fileurl ='file://' + os.environ['mypath'] +'/'+ url_relative
        # fileurl ='file://' + os.environ['mypath'] +'/app/'+ url_relative
        print(fileurl)
        # os.system('x-www-browser" '+ fileurl )

