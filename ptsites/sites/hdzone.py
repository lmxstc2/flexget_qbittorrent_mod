from flexget import plugin

from ptsites.executor import Executor

# auto_sign_in
URL = 'http://hdzone.me/attendance.php'
SUCCEED_REGEX = '这是您的第 \\d+ 次签到，已连续签到 \\d+ 天，本次签到获得 \\d+ 个魔力值。|您今天已经签到过了，请勿重复刷新。'


class MainClass(Executor):
    @staticmethod
    def build_sign_in_entry(entry, site_name, config):
        site_config = entry['site_config']
        if not isinstance(site_config, str):
            raise plugin.PluginError('{} site_config is not a String'.format(site_name))
        entry['url'] = URL
        entry['succeed_regex'] = SUCCEED_REGEX
        headers = {
            'cookie': site_config,
            'user-agent': config.get('user-agent'),
            'referer': URL
        }
        entry['headers'] = headers