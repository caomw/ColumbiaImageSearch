import json

class Updater():
    """ This class enables updating the index of available images, 
    getting new images from an ingester and pushing them to an indexer.
    """

    def __init__(self,global_conf_file):
        """ Creates an `Updater` based on the values in the json file `global_conf_file`.

        :param global_conf_file: path to json file with parameters configuration.
        """
        self.ingester = None
        self.indexer = None
        self.global_conf_file = global_conf_file
        self.global_conf = json.load(open(self.global_conf_file,'rt'))
        self.init_ingester()
        self.init_indexer()

    def init_ingester(self):
        """ Initialize `ingester` from `global_conf['ingester']` value.

        Currently supported ingester types are:
        - mysql_ingester
        - cdr_ingester
        """
        field = 'UP_ingester'
        if field not in self.global_conf:
            raise ValueError("[Updater: error] "+field+" is not defined in configuration file.")
        if self.global_conf[field]=="mysql_ingester":
            from ..ingester.mysql_ingester import MySQLIngester
            self.ingester = MySQLIngester(self.global_conf_file)
        elif self.global_conf[field]=="cdr_ingester":
            from ..ingester.cdr_ingester import CDRIngester
            self.ingester = CDRIngester(self.global_conf_file)
        else:
            raise ValueError("[Updater: error] unkown 'ingester' {}.".format(self.global_conf[field]))

    def init_indexer(self):
        """ Initialize `indexer` from `global_conf['indexer']` value.

        Currently supported indexer types are:
        - local_indexer
        - hbase_indexer
        """
        field = 'UP_indexer'
        if field not in self.global_conf:
            raise ValueError("[Updater: error] "+field+" is not defined in configuration file.")
        if self.global_conf[field]=="local_indexer":
            from ..indexer.local_indexer import LocalIndexer
            self.indexer = LocalIndexer(self.global_conf_file)
        elif self.global_conf[field]=="hbase_indexer":
            from ..indexer.hbase_indexer import HBaseIndexer
            self.indexer = HBaseIndexer(self.global_conf_file)
        else:
            raise ValueError("[Updater: error] unkown 'indexer' {}.".format(self.global_conf[field]))

    def run_udpate(self):
        """ Runs an update.
        """
        try:
            start = self.indexer.get_next_batch_start()
            self.ingester.set_start(start)
            batch = self.ingester.get_batch()
            self.indexer.index_batch(batch)
        except Exception as inst:
            print "[Updater.run_udpate: error] {}".format(inst)
