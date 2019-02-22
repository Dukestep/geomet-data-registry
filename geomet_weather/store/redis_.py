###############################################################################
#
# Copyright (C) 2019 Tom Kralidis
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

import logging
from urllib.parse import urlparse

import redis

from geomet_weather.store.base import BaseStore

LOGGER = logging.getLogger(__name__)


class RedisStore(BaseStore):
    """Redis key-value store implementation"""

    def __init__(self, provider, url):
        """
        Initialize object

        :param provider: provider type
        :param url: url/path of tile index

        :returns: `geomet_weather.store.redis_.RedisStore`
        """

        BaseStore.__init__(self, provider, url)

        self.url_parsed = urlparse(self.url)

        self.redis = redis.StrictRedis(host=self.url_parsed.hostname,
                                       port=self.url_parsed.port)

    def increment(self, group, layer):
        """
        Increment group/layer/count

        :param group: group name
        :param layer: layer name

        :returns: boolean of process status
        """

        raise NotImplementedError()

    def count(self, group, layer):
        """
        Get file count of a given group/layer

        :param group: group name
        :param layer: layer name

        :returns: boolean of process status
        """

        raise NotImplementedError()

    def reset(self, group, layer):
        """
        Reset group/layer count

        :param group: group name
        :param layer: layer name

        :returns: boolean of process status
        """

        raise NotImplementedError()

    def __repr__(self):
        return '<RedisStore> {}'.format(self.type)


class StoreError(Exception):
    """setup error"""
    pass
