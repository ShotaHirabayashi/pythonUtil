from oauth2client.service_account import ServiceAccountCredentials
import gspread


def set_date_spreadsheet():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('autohotelproject-e5248af20781.json', scope)
    gc = gspread.authorize(credentials)
    SPREADSHEET_KEY = "1L27sExDrHt9D4JHFu-qo_HZTXb6a3a2x5NoGwju6aD4"
    worksheet = gc.open_by_key(SPREADSHEET_KEY).worksheet("テスト")
    import_value = int(worksheet.acell('A1').value)
    # A1セルの値に100加算した値をB1セルに表示させる
    export_value = import_value + 100
    worksheet.update_cell(1, 2, export_value)
