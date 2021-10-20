
import os

folder_path = "C:/Users/jst75/Desktop/새 폴더"

folder_list = os.listdir(folder_path)                                               # 각 폴더 이름 (hood_T/hong_T/...)
#folder_list = ["hood_T", "long_T"]
for folder_name in folder_list :                                                    # 각 폴더 이름(hood_T)의 파일이름 얻기
    file_path = folder_path + "\\" + folder_name                                    # file_path : D:\\python_D\\fashion_data\\original\\hood_T
    
    file_list = os.listdir(file_path)                                               # file_list[0] : D:\\python_D\\fashion_data\\original\\hood_T\\hood_T_1.jpg
    #file_list.sort()

    print("-------------------------------------------------")
    print(folder_name + " have " + str(len(file_list)) + " files.")
    print("file_path : " + file_path)
    
    # (hood_T_1(2).jpg -> 1.jpg) 이미 이름이 있는 파일이면 오류가 나기에 먼저 숫자로된 아무 이름으로 만들고, 다시 이름을 지정합니다.
    count = 1
    for file_name in file_list :
        old_name = file_path + "\\" + file_name                                     # old_name = D:\\python_D\\fashion_data\\original\\hood_T\\hood_T_1 (2).jpg
        new_name = file_path + "\\" + str(count) + ".xlsx"                           # new_name = D:\\python_D\\fashion_data\\original\\hood_T\\1.jpg

        try:
            os.rename(old_name, new_name)
            print("success : " + file_name + " -> " + str(count) + ".xls")
        except:
            print("fail : " + file_name + " -> " + str(count) + ".xls")
            print("=========files already renamed original(abcde.jpg) to number(1.jpg)===========")
            
        count = count + 1
        print("="*50)
        print("1.xls생성 완료")
        print("="*50)


    # # (1.jpg -> hood_T_1.jpg) : count 값을 다시 지정해 이름을 지정함.
    # file_list = os.listdir(file_path)                                               # 1.jpg 로 바뀐 이름을 가져와야 되기 때문에 다시 로드
    # count = 1
    # for file_name in file_list :
    #     old_name = file_path + "\\" + file_name                                     # old_name = 1.jpg
    #     new_name = file_path + "\\" + folder_name + "_" + str(count) + ".jpg"       # new_name = hood_T_1.jpg

    #     try:
    #         os.rename(old_name, new_name)
    #         print("success : " + file_name + " -> " + folder_name + "_" + str(count) + ".jpg")
    #     except:
    #         print("fail : " + file_name + " -> " + folder_name + "_" + str(count) + ".jpg")
    #         print("=========files already renamed number(1.jpg) to new_name(hood_T_1.jpg)===========")
    #         break
    #     count = count + 1