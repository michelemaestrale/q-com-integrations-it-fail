import json
import os
import sys
from typing import Dict

from app.utils.slack import slack_alert

from config_sm import Config, ConfigBuilder

#arn = "arn:aws:secretsmanager:eu-west-1:330652100360:secret:techops_automation"
#secrets_arns: Dict[str, str] = {
#    "supply_ops_italy": f"{arn}/supply_ops_italy-xtDpnF",
#}
#cb: ConfigBuilder = ConfigBuilder()
#for name, arn in secrets_arns.items():
#    cb.add_parameter(name, sm=arn)
#config: Config = cb.build()

#secrets: dict = json.loads(config.get_value("supply_ops_italy"))
#for secret_name, secret_value in secrets.items():
#    os.environ[secret_name] = secret_value

failure = os.system(sys.argv[1])
if failure:
    print('Execution of "%s" failed!\n' % sys.argv[1])
    slack_alert(f"Failed {sys.argv[1]}")
    sys.exit(1)
