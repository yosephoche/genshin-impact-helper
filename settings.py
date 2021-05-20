# settings
import logging
import json
import requests
import os
from requests.exceptions import HTTPError

# hard code your variables here if you are running the script from a private PC
USER_VARIABLES = {
    'USER_AGENT': '',  # google "what is my user agent", should begin with Mozilla/5.0
    'OS_COOKIE': '',  # your genshin/hoyolab login cookie (see below)
    'DISCORD_WEBHOOK': '',  # optional
}
# OS_COOKIE Value should look like: login_ticket=xxx; account_id=696969; cookie_token=xxxxx; ltoken=xxxx; ltuid=696969; mi18nLang=en-us; _MHYUUID=xxx
#         Separate cookies for multiple accounts with the hash symbol #
#         e.g. cookie1text#cookie2text

__all__ = ['log', 'CONFIG', 'req']

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S')

log = logger = logging

class _Config:
    GIH_VERSION = '1.7.0.210301-alpha'
    LOG_LEVEL = logging.INFO
    # LOG_LEVEL = logging.DEBUG
    OS_COOKIE = ''
    DISCORD_WEBHOOK = ''
    PUSH_CONFIG = '' #just leaving this here, no one actually uses this anyway

    # HoYoLAB
    LANG = 'en-us'
    OS_ACT_ID = 'e202102251931481'
    OS_REFERER_URL = 'https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id={}'.format(OS_ACT_ID)
    OS_REWARD_URL = 'https://hk4e-api-os.mihoyo.com/event/sol/home?lang={}&act_id={}'.format(LANG, OS_ACT_ID)
    # OS_ROLE_URL = 'https://api-os-takumi.mihoyo.com/auth/api/getUserAccountInfoByLToken?t={}&ltoken={}&uid={}'
    OS_INFO_URL = 'https://hk4e-api-os.mihoyo.com/event/sol/info?lang={}&act_id={}'.format(LANG, OS_ACT_ID)
    OS_SIGN_URL = 'https://hk4e-api-os.mihoyo.com/event/sol/sign?lang={}'.format(LANG)
    WB_USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E150'


class HttpRequest(object):
    @staticmethod
    def to_python(json_str: str):
        return json.loads(json_str)

    @staticmethod
    def to_json(obj):
        return json.dumps(obj, indent=4, ensure_ascii=False)

    def request(self, method, url, max_retry: int = 2,
            params=None, data=None, json=None, headers=None, **kwargs):
        for i in range(max_retry + 1):
            try:
                s = requests.Session()
                response = s.request(method, url, params=params,
                    data=data, json=json, headers=headers, **kwargs)
            except HTTPError as e:
                log.error(f'HTTP error:\n{e}')
                log.error(f'The NO.{i + 1} request failed, retrying...')
            except KeyError as e:
                log.error(f'Wrong response:\n{e}')
                log.error(f'The NO.{i + 1} request failed, retrying...')
            except Exception as e:
                log.error(f'Unknown error:\n{e}')
                log.error(f'The NO.{i + 1} request failed, retrying...')
            else:
                return response

        raise Exception(f'All {max_retry + 1} HTTP requests failed, die.')


req = HttpRequest()
CONFIG = _Config()
log.basicConfig(level=CONFIG.LOG_LEVEL)
if USER_VARIABLES['OS_COOKIE']:
    CONFIG.OS_COOKIE = USER_VARIABLES['OS_COOKIE']
elif os.environ['OS_COOKIE']:
    CONFIG.OS_COOKIE = os.environ['OS_COOKIE']
if not CONFIG.OS_COOKIE:
    raise Exception("no OS_COOKIE configured")
if USER_VARIABLES['USER_AGENT']:
    CONFIG.WB_USER_AGENT = USER_VARIABLES['USER_AGENT']
elif os.environ['USER_AGENT']:
    CONFIG.WB_USER_AGENT = os.environ['USER_AGENT']
if USER_VARIABLES['DISCORD_WEBHOOK']:
    CONFIG.DISCORD_WEBHOOK = USER_VARIABLES['DISCORD_WEBHOOK']
elif os.environ['DISCORD_WEBHOOK']:
    CONFIG.DISCORD_WEBHOOK = os.environ['DISCORD_WEBHOOK']

MESSAGE_TEMPLATE = '''
    {today:#^28}
    [UID:{region_name}]{uid}
    Today's rewards: {award_name} × {award_cnt}
    Monthly Check-In count: {total_sign_day} days
    Check-in result: {status}
    {end:#^28}'''

CONFIG.MESSAGE_TEMPLATE = MESSAGE_TEMPLATE
