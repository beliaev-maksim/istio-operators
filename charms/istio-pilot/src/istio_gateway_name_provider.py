import logging
from ops.framework import Object

logger = logging.getLogger(__name__)

DEFAULT_RELATION_NAME = "gateway"


class GatewayProvider(Object):
    def __init__(self, charm, relation_name=DEFAULT_RELATION_NAME):
        super().__init__(charm, relation_name)

    def send_gateway_relation_data(self, charm, gateway_name, gateway_namespace):
        relations = self.model.relations["gateway"]
        if not relations:
            self.logger.debug("No relations, this line should have not run")
            return
        for relation in relations:
            relation.data[charm].update(
                {
                    "gateway_name": gateway_name,
                    "gateway_namespace": gateway_namespace,
                }
            )
