import logging
from ops.framework import Object

logger = logging.getLogger(__name__)

DEFAULT_RELATION_NAME = "gateway"


class GatewayProvider(Object):
    def __init__(self, charm, relation_name=DEFAULT_RELATION_NAME):
        super().__init__(charm, relation_name)

    def send_gateway_relation_data(self, app, gateway_name, gateway_namespace):
        logger.info("Executing send_gateway_relation_data")
        relations = self.model.relations["gateway"]
        logger.info(f"found {len(relations)} relations: {relations}")
        for relation in relations:
            relation.data[app].update(
                {
                    "gateway_name": gateway_name,
                    "gateway_namespace": gateway_namespace,
                }
            )
