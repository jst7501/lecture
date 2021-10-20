from openpyxl import load_workbook
import re
import sys
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from io import StringIO 
import datetime

date_handler = lambda obj: (
    obj.isoformat()
    if isinstance(obj, (datetime.datetime, datetime.date))
    else None
)
json.dumps(datetime.datetime.now(), default=date_handler)
print("시트에 작업을 시작합니다.")
def Excel():
    wb = load_workbook('C:/Users/jst75/Desktop/새 폴더/준식/1.xlsx')
 
    # 현재 Active Sheet 얻기
    ws = wb.active
    #ws = wb.get_sheet_by_name("Sheet1") 엑셀에서 sheet를 선택
    chk="0123456789"
    #sys.stdout = open('output.txt','w') 결과를 텍스트 파일로 저장 / '쓰기'가능
    pre = ws.rows
    #print(pre)
    #for r in ws.rows:
    #    print(r)
    for r in ws.rows: # 엑셀에서 각 행과 열로 순회하기 위함
        ty = r[2].value # 첫째 열의 값 : 그룹
        data = r[1].value # 둘째 열의 값 : 주소
        vs = r[3].value
        vf = r[4].value
        vt = r[5].value
        vr = r[6].value
        vy = r[7].value
        vh = r[8].value
        ve = r[9].value
         

        #if pre != ty:
            #pre =ty
            #print("그룹 : ",ty)
            #print('----------------------------------',end='\n')
       
        #print(r)
        scope = ['https://spreadsheets.google.com/feeds']
        json_file_name = 'sekiro-329602-fa52ecc5078d.json'
        credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
        gc = gspread.authorize(credentials)
        spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1ZT2dIXr4H2UgwvgJvsn8-8lK-2DvOES9M97Va1XAElU/edit#gid=0'
        # 문서 불러오기
        doc = gc.open_by_url(spreadsheet_url)
        # a 시트 불러오기
        worksheet = doc.worksheet('시트1')
        date_handler = lambda obj: (
        obj.isoformat()
        if isinstance(obj, (datetime.datetime, datetime.date))
        else None
        )
        json.dumps(datetime.datetime.now(), default=date_handler)
 
        # range_list = worksheet.range('A1:D3')
        # for cell in range_list:
        #     print(cell.value)
        print("데이터를 올리고 있습니다.")
        worksheet.append_row([data,ty,vs,vf,vt,vr,vy,vh,ve])
        print("성공")
if __name__ == "__main__":
    Excel()