from json import loads

from requests import post

from .api_forms.repositories import list_repositories
from .authentication import load_api_key
from .common.InvalidAPIKeyException import InvalidAPIKeyException
from .logger import logger


class GithubController:
    # TODO: Implement print function

    __slots__ = 'api_key', 'args'
    api_endpoint = 'https://api.github.com/graphql'

    def __init__(self, args):
        self.api_key = None
        self.args = args

    def __call__(self, *args, **kwargs):
        self.obtain_api_key()
        self.process_args()

    def obtain_api_key(self):
        """
        Method reads API key from 'api_key' file in the project root and saves it into class attribute

        :return: None, API key is saved into class attribute api_key
        :raise: FileNotFoundError in case the 'api_key' file is missing completely
        :raise: InvalidAPIKeyException in case the 'api_key' file exist, but is either missing the API key
        or the API key is malformed
        """
        try:
            self.api_key = load_api_key()
        except FileNotFoundError:
            logger.warning("'api_key' file missing in project root. Please, create the file and add your API key to it")
            return False
        except InvalidAPIKeyException:
            logger.warning("'api_key' file present, but it's either missing the key or the key is malformed")
            return False

    def process_args(self):
        """

        :return:
        """
        actions_dict = {'list-my-repositories': self.list_my_repositories}
        for arg in self.args.action:
            # TODO: Investigate
            if arg in actions_dict.keys():
                actions_dict[arg]()

    # Repositories operations

    def list_my_repositories(self) -> [(str, str, str)]:
        """
        List all repositories of the current user (authenticated by API key)

        :return: list of tuples (name, sshUrl, url)
        """
        with post(self.api_endpoint, json=list_repositories,
                  headers={"Authorization": "bearer {}".format(self.api_key)}) as response:
            if response.ok:
                total_number_of_repositories = loads(response.text)['data']['viewer']['repositories']['totalCount']
                logger.debug("Total number of repositories obtainable: {}".format(total_number_of_repositories))
                repositories_dict = loads(response.text)['data']['viewer']['repositories']['edges']
                return [
                    (
                        repositories_dict[i]['node']['name'],
                        repositories_dict[i]['node']['sshUrl'],
                        repositories_dict[i]['node']['url'])
                    for i in range(total_number_of_repositories)
                ]

