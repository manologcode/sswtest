import os
import sys
from datetime import datetime

from urllib.parse import urlparse

from in_out_data import InOutData
from find_urls import FindUrls
from my_selenium import MySelenium
from my_image import MyImage


class Test():
    config = InOutData.read_yaml('config.yml')

    folder = config['folder_export']

    def __init__(self, config_yml, file_name):

        self.name_project = file_name.split('.')[0]
        self.config = self.read_config(config_yml)

    def read_config(self, config_yml):
        options = {'path': f"{self.folder}{self.name_project}/",
                   'name_folder': datetime.now().strftime("%Y_%m_%d"),
                   'size_screen': '1420,1080',
                   'compare': None
                   }

        if 'name' in config_yml and config_yml['name'] is not None:
            options['path'] = f"{self.folder}{config_yml['name']}/"
        if 'folder' in config_yml and config_yml['folder'] is not None and config_yml['folder'] != '':
            options['name_folder'] = config_yml['folder']
        if 'size_screen' in config_yml and config_yml['size_screen'] is not None and config_yml['size_screen'] != '':
            options['size_screen'] = config_yml['size_screen']
        if 'compare' in config_yml and config_yml['compare'] is not None and config_yml['compare'] != '':
            options['compare'] = config_yml['compare']
        options['path_project'] = self.create_folder(
            options['path'], options['name_folder'])
        return options

    def url_to_name(self, url):
        parts = urlparse(url)
        name = parts.path.replace("/", '_').replace(".", '_')
        name = name[:-1] if name.endswith('_') else name
        name = name[1:] if len(name) > 1 else "index"
        return f"{name}.png"

    def create_folder(self, path, name):
        path_exit = path + name
        path_exit = InOutData.name_folder_free(path_exit)
        os.makedirs(path_exit)
        print(f"creando carpeta: {path_exit}")
        return path_exit

    def compare_images(self):
        if self.config['compare'] is not None:
            path_imgs_ini = f"{self.config['path']}{self.config['compare']}"
            path_imgs_now = self.config['path_project']
        result = MyImage.compare_two_folders(path_imgs_now, path_imgs_ini)
        url_relative = self.create_response_html(path_imgs_ini, path_imgs_now, result)
        InOutData.open_in_browser(url_relative)

    def tour_pages(self, pages):
        for item in pages:
            url = item['url']
            nsel = MySelenium(url, self.config['size_screen'])
            nsel.visit()
            actions = item['actions']
            self.tour_actions(actions, nsel, url)

    def tour_actions(self, actions, nsel, url):
        for action in actions:
            if 'input' in action:
                item = action['input']
                nsel.input(item['attr_type'], item['attr_val'], item['value'])

            if 'click' in action:
                item = action['click']
                nsel.click(item['attr_type'], item['attr_val'])

            if 'photo' in action:
                print(action)
                if action['photo'] is not None and action['photo'] != '':
                    name = action['photo']+".png"
                else:
                    name = self.url_to_name(url)
                path_photo = self.config['path_project'] + '/' + name
                path_photo = InOutData.name_file_free(path_photo)
                nsel.photo(path_photo)

    def create_response_html(self, path1, path2, result):
        path_file = f"{ self.config['path'] }index.html"
        path_img1 = path1.split('/')[-1]
        path_img2 = path2.split('/')[-1]
        f = open(path_file, 'w')
        html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Easy Screen Short Web Test</title>
    <style>
        html {
            font-family: Helvetica, Arial, sans-serif;
        }
        h4{
            margin: 4px;
        }
        img{
            width: 45%;
        }
        a{
            text-decoration: none;
            display: block;
            font-size: 16px;
            padding: 6px 10px;
        }
        .a-img{
            text-align: center;
        }
        .success{
            color: green;
            background-color: honeydew;
            border: solid 1px green;
            border-radius: 10px;
            margin: 6px;
        }
        .warning{
            color:red;
            background-color: #f9e8e8;
            border: solid 1px green;
            border-radius: 10px;
            margin: 6px;
        }
        .d-flex{
            display: flex;
            justify-content: space-evenly;
        }
    </style>
</head>
    <body>
        <h2>Resultados de Test</h2>"""
        html += f"        <p>Comparando {path1[9:]} == {path2[9:]}.</p>"
        for item in result:
            if isinstance(item['diff'], str):
                fragmen = f"""
             <a href="{path_img2}/{item['file']}" class="warning" target="_blank">
                {item['diff']} - {item['file']}
             </a>
            """
            elif item['diff'] < 0.1:
                fragmen = f"""
                <a href="{path_img2}/{item['file']}" class="success" target="_blank">
                    OK - {item['file']}
                </a>
            """
            else:
                fragmen = f"""
            <div class="warning">
                <h4>KO - {item['file']}</h4>
                <div class="d-flex">
                <a href="{path_img1}/{item['file']}" class="a-img" target="_blank">
                    <img src="{path_img1}/{item['file']}">
                </a>
                <a href="{path_img2}/{item['file']}" class="a-img" target="_blank">
                    <img src="{path_img2}/{item['file']}">
                </div>
                </a>
            </div> """
            html += fragmen
        html += """    </body>
</html>
        """
        f.write(html)
        f.close()
        return path_file[9:]


if __name__ == "__main__":

    param = InOutData.read_params()
    print(param)
    print('.....................')
    if param is not None:
        in_data = InOutData.read_yaml(param["file"])
        test = Test(in_data['config'], param["file"])
        test.tour_pages(in_data['pages'])
        test.compare_images()
    else:
        print('Crea y compara capturas de pantalla de url enviadas a traves de un archivo yml de configuración.')
        print('Para conocer todas las opciones de configuración y acceso entra en la git. https://github.com/manologcode/sswtest')
        print('Este programa también genera este archivo yml y captura urls automáticamente a partir de esa url inicial.')

        config = {
            'title': 'Generar yml a partir de url inicial',
            'fields': {
                'url': 'Url: '
            }
        }
        in_data = InOutData.input_data(config)
        FindUrls(in_data['url'], custom_links=True)
