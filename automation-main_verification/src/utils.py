import pandas as pd
from src.config import Config


class Utils:
    def read_excel(self):
        """read excel file for ration card
        """
        result = pd.read_excel(Config.EXCEL_FILE_PATH, sheet_name=Config.SHEET_NAME, header=0).to_dict(orient="records")
        return result
