#!/usr/bin/env python


class SettingStore:

    # Set the API URL.
    def __init__(self, API_KEY):
        self.URL = 'http://thecatapi.com/api/images/get?format=xml'

        # Number of Images in one request.
        # Limit:1~100
        NUMBER = '20'

        # Image Type.
        # allow for jpg,png,gif
        TYPE = 'gif'

        # Add the API parameters and create API Url.
        self.URL += '&results_per_page=' + NUMBER
        self.URL += '&type=' + TYPE
        self.URL += '&api_key=' + API_KEY

    def get_api_url(self):
        return self.URL


class WebAccess():

    # Parameter is Image API Url.
    def __init__(self, url):
        self.url = url

        # network resource read lib.
        import urllib.request

        # get request to cat image api.
        self.resource = urllib.request.urlopen(self.url)

    # web content getter.
    def get_resource(self):
        return self.resource


class DecodeContent():

    # Decode the WebData to utf8
    def decode_data(self, response):
        # decode web data.
        web_data = ''
        for line in response.readlines():
            web_data += line.decode('utf-8')

        # xml data parse the element.
        # get the 'url' element.
        import xml.etree.ElementTree as ET
        xml_tree = ET.fromstring(web_data)
        for child_data in xml_tree.iter('url'):
            print(child_data.text)

if __name__ == "__main__":
    # Your API Key.
    # Please registration follow.
    # http://thecatapi.com/api-key-registration.html
    API_KEY = 'hogehoge'

    # get setting data for Image API.
    # and, create the API URL.
    setting = SettingStore(API_KEY)

    web = WebAccess(setting.get_api_url())
    response = web.get_resource()

    decoder = DecodeContent()
    decoder.decode_data(response)
