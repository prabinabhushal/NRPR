# import sys
import logging
import argparse
from ETL_nrpr import ExtractTransferLoad

def main ():
    #  zip_file = sys.argv[1]
    logging.basicConfig(filename='etl.log',
    level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger("getLogger")

    parser = argparse.ArgumentParser(description="folder path for etl process")
    parser.add_argument("--folder",help="Full path to the folder to process")

    args = parser.parse_args()
    etl = ExtractTransferLoad()
    etl.run(args,logger)
 
if __name__ == "__main__":
    main()
