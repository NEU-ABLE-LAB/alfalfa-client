import os
import datetime
import pytest
import tempfile
import zipfile
from unittest import TestCase
from time import sleep
from alfalfa_client.alfalfa_client import AlfalfaClient


# Consider factoring this out of the test file
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def create_zip(model_dir):
    osw_dir_path = os.path.join(os.path.dirname(__file__), 'test_idfs', model_dir)
    zip_file_fd, zip_file_path = tempfile.mkstemp(suffix='.zip')

    zipf = zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED)
    zipdir(osw_dir_path, zipf)
    zipf.close()
    return zip_file_path


if __name__ == "__main__":
    ## Setting up the test path
    #zip_file_path = create_zip('refrig_case_osw')   ## Example from Alfalfa as is
    #zip_file_path = create_zip('refrig_case_osw_weather')   ## Weather file changed --> weather_data.csv is required
    zip_file_path = create_zip('refrig_case_osw_idf')   ## IDF file changed -->

    #zip_file_path = create_zip('train_resstock')
    #zip_file_path = create_zip('refrig_case_osw3')


    ## Setting the Alfalfa client (docker container)
    alfalfa = AlfalfaClient(url='http://172.23.32.1')


    ## Submit the idf file (zipped)
    model_id = alfalfa.submit(zip_file_path)

    alfalfa.wait(model_id, "Stopped")
    alfalfa.start(
        model_id,
        external_clock="false",
        start_datetime=datetime.datetime(2019, 1, 2, 0, 0, 0),
        end_datetime=datetime.datetime(2019, 1, 3, 0, 0, 0),
        timescale=5
    )

    alfalfa.wait(model_id, "Running")
    alfalfa.stop(model_id)
    alfalfa.wait(model_id, "Stopped")