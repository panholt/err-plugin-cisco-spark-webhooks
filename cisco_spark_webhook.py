# -*- coding: utf-8 -*-
from errbot import BotPlugin, webhook, botcmd


class SparkWebhook(BotPlugin):
    '''
    Webhook Receiver for Spark Backend
    '''

    @webhook('/incoming')
    def incoming(self, request):
        self.log.debug('Got Request: %s', request)
        self._bot.spark_webhook_callback(request)
        return "OK"

    @botcmd
    def webhook_stats(self, msg, *args):
        return 'Stats and stuff'

    def process_stats(self, request):
        try:
            data = request['data']
        except KeyError:
            self.log.warning('Invalid data received on webhook')
        if data['resource'] == 'messages':
            pass
        elif data['resource'] == 'memberships':
            pass
        elif data['resource'] == 'rooms':
            pass
        elif data['resource'] == 'teams':
            pass
        else:
            self.log.warning('Unknown resource: %s', data['resource'])
