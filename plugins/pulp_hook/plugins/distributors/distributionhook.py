"""This plugin executes a user script at /usr/share/foreman/config/hooks/pulp/after_sync.sh"""

from subprocess import call
from pulp.plugins.distributor import Distributor
from pulp.plugins.types.database import all_type_ids

def entry_point():
    """default entry point to initialize the DistributionHook class"""
    return distributionhook

class distributionhook(Distributor):
    """This class defines the DistributionHook which inherits Distributor per the documenentation
       at https://docs.pulpproject.org/dev-guide/newtypesupport/plugin/example.html"""

    @classmethod
    def metadata(cls):
        return {
            'id' : 'distribution_hook',
            'display_name' : 'Distribution Hook',
            'types' : all_type_ids(),
        }

    def validate_config(self, repo, config, related_repos):
        return True, None

    def publish_repo(self, repo, publish_conduit, config):
        call("/usr/share/foreman/config/hooks/pulp/after_sync.sh", shell=True)
