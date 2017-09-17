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
