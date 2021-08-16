import requests
import logging
from common.logger import Logging
from conf import Config


Logging()
_timeout = 30

class Request:
    def __init__(self):
        """
        :session:
        """
        self.s = requests.session()
        self.conf=Config.Config()


    def request(self, method, url, data=None, params=None, files=None,headers=None, cookies=None, json=None,timeout=int(_timeout)):
        #url = self.set_url(url)
        print(headers)
        # if not url.startswith('http://'):
        #     url = 'http://%s' % url

        try:

            if method.upper() == 'POST':
                response = self.s.request(method='POST', url=url, data=data, params=params,json=json,headers=headers,files=files,
                                          cookies=cookies)

            elif method.upper() == 'GET':
                if params:
                    response = self.s.request(method='GET', url=url, params=params, headers=headers,
                                              cookies=cookies)

                else:
                    response = self.s.request(method='GET', url=url, headers=headers,
                                              cookies=cookies)
            elif method.upper() == 'PUT':
                response = self.s.request(method='PUT', url=url, data=data, files=files, headers=headers,
                                          cookies=cookies)

            elif method.upper() == 'DELETE':
                response = self.s.request(method='DELETE', url=url, data=data,params=params,  headers=headers,
                                          cookies=cookies)



        except requests.RequestException as e:
            logging.error('RequestException URL : %s' % url)
            logging.error('RequestException Info: %s' % e)
            return

        except Exception as e:
            logging.error('Exception URL : %s' % url)
            logging.error('Exception Info: %s' % e)
            return

        time_total = response.elapsed.total_seconds()
        status_code = response.status_code


        logging.info("-" * 100)
        logging.info('[ api name    ] : {}'.format(url.rsplit("/")[-1]))
        logging.info('[ request url ] : {}'.format(response.url))
        logging.info('[ request paramer ] : {}'.format(params))
        logging.info('[ request hearder ] : {}'.format(headers))
        logging.info('[ request data ] : {}'.format(data))
        logging.info('[ request json ] : {}'.format(json))
        logging.info('[ method      ] : {}'.format(method.upper()))
        logging.info('[ status code ] : {}'.format(status_code))
        logging.info('[ time total  ] : {} s'.format(time_total))

        if "application/json" in response.headers.get("Content-Type"):
            logging.info('[ response json ] : %s' % response.json())
        else:
            logging.info('[ response text ] : %s' % response.text)
        logging.info("-" * 100)

        return response

    def params_splicing_url(api, payload):
        """
        主要用于将post请求的参数拼接为URL
        :param api: API接口
        :param payload: 传参（dict）
        :return: URL
        """
        params = []
        for key in payload.keys():
            value = payload[key]
            param = key + '=' + str(value)
            params.append(param)
        url = api + '?' + '&'.join(params)
        return url

    def set_url(self, Interface):
        """
        主要用于将请求拼接为URL
        set url
        :param: interface url
        :return:
        """
        self.host = self.conf.http_type_release + '://' + self.conf.host_release + ':' + self.conf.port_release
        self.url = self.host + '/' + Interface
        return self.url


if __name__ == '__main__':
   HTTP2= Request().set_url('LOGIN')
   print(HTTP2)


