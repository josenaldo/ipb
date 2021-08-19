import os
import subprocess
import re

from datetime import datetime

import urllib.request


class HerokuPGBackupDownloader():

    HEROKU_PATH = os.environ.get('HEROKU_PATH', 'heroku')

    def run(self, app, local_directory):
        """Download a backup for an app to the local disk"""

        print(f'Running backup script for {app}...')

        # Create a new backup
        new_backup_id = self.capture(app)

        print(f'New backup id: {new_backup_id}')

        # And finally download a local copy of that backup
        new_backup_url = self.get_url(app, new_backup_id)

        self.download(app, new_backup_url, local_directory)

        print('Done')

    def capture(self, app):
        """Create a new backup and return the backup id"""

        print('Capturing a new backup...')
        subprocess.run(f'{self.HEROKU_PATH} pg:backups capture --app {app}')

        info_out = subprocess.run(f'{self.HEROKU_PATH} pg:backups:info --app {app}', capture_output=True, text=True)
        info = info_out.stdout

        # Extract the backup id
        backup_id_regex = r'(?<====\sBackup\s)b(.+)(?=\n)'


        # backup_match = backup_id_regex.match(info)

        backup_match = re.search(backup_id_regex, info)

        # Return the new backup id
        # backup_match.captures.first

        return backup_match.group()

    def get_url(self, app, backup_id):
        """Returns the URL for an app's backup"""
        out = subprocess.run(f'{self.HEROKU_PATH} pg:backups public-url {backup_id} --app {app}', capture_output=True, text=True)

        # There's a new line character at the end we need to remove
        raw = out.stdout.rstrip()

        return raw

    def download(self, app, backup_url, local_destination_directory):
        """Download a backup given its URL"""

        print('  Downloading new backup...')

        dateTimeObj = datetime.now()
        timestampStr = dateTimeObj.strftime("%Y%m%d_%H%M%S")


        local_destination_filename = f'{app}-{timestampStr}.dump'
        local_destination_path = f'{local_destination_directory}/{local_destination_filename}'

        urllib.request.urlretrieve(backup_url, local_destination_path)
        # subprocess.run(f'curl --silent --output \'{local_destination_path}\' --location \'{backup_url}\'')
        # subprocess.run(f'curl \'{local_destination_path}\' --location \'{backup_url}\'')


import sys
if __name__ == "__main__":

    for arg in sys.argv:
        print(arg)

    if len(sys.argv) == 3:
        runner = HerokuPGBackupDownloader()
        runner.run(sys.argv[1], sys.argv[2])
    else:
        raise ValueError('This script expects two arguments: the app name and the local directory to download the backup')

