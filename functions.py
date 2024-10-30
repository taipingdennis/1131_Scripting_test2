# 題目：簡易人事資料管理系統實作
# functions

# 1. 新增資料(已完善)
def create_data(database: list):
    # init power
    if_create = 'y'

    while if_create == 'y':
        # 將"年齡輸入格式確認"功能打包成函數, 盡量避免多層巢狀結構影響可讀性
        def age_input_check(age):
            while True:
                try:
                    float_age = float(age)
                    int_age = int(float_age)
                    if int_age == float_age and int_age > 0:
                        age = int_age
                        break
                    else:
                        age = input("年齡須為正整數, 請重新輸入: ")
                except Exception:
                    age = input("年齡須為正整數, 請重新輸入: ")

            return age

        # 定義資料格式
        department = str()
        name = str()
        age = str()
        phone = str()
        data_dict = {
            "部門": department,
            "姓名": name,
            "年齡": age,
            "手機號碼": phone
        }

        # 使用者輸入該筆資料內容
        key = list(data_dict.keys())
        for i in range(len(data_dict)):
            data_dict[key[i]] = input(f"請輸入{key[i]}: ")

            # 確保年齡輸入的格式正確
            if key[i] == "年齡":
                data_dict[key[i]] = age_input_check(data_dict[key[i]])

        # 將該筆資料加入資料庫
        database.append(data_dict)

        # 詢問使用者是否繼續新增資料
        if_create = input("是否繼續新增資料? (y/n): ")

        if if_create == 'y':
            continue
        elif if_create == 'n':
            break

        while if_create not in ['y', 'n']:
            if_create = input("輸入格式錯誤, 是否繼續新增資料? (y/n): ")

# 2. 查詢資料(由於時間不足先ChatGPT生成, 方待日後重構)
def read_data(database: list):
    # 取得使用者輸入的查詢姓名
    query_name = input("請輸入要查詢的姓名: ")

    # 搜索資料庫
    found = False
    for entry in database:
        if entry['姓名'] == query_name:
            # 如果找到對應的姓名，則輸出查詢結果
            print("\n--- 查詢結果 ---")
            print(f"{'部門':<10}{'姓名':<10}{'年齡':<10}{'手機號碼':<15}")
            print(f"----------------------------------------")  # 分隔線
            print(f"{entry['部門']:<10}{entry['姓名']:<10}{entry['年齡']:<10}{entry['手機號碼']:<15}")
            found = True
            break

    # 如果沒找到，則提示查無此人
    if not found:
        print("查無此人。")

# 3. 修改資料(由於時間不足先ChatGPT生成, 方待日後重構)
def update_data(database: list):
    # 取得使用者輸入的姓名
    update_name = input("請輸入要修改的姓名: ")

    # 搜索資料庫
    for entry in database:
        if entry['姓名'] == update_name:
            # 找到對應的姓名，顯示當前資料
            print("當前資料:")
            print(f"{'部門':<10}{'姓名':<10}{'年齡':<10}{'手機號碼':<15}")
            print(f"----------------------------------------")  # 分隔線
            print(f"{entry['部門']:<10}{entry['姓名']:<10}{entry['年齡']:<10}{entry['手機號碼']:<15}")

            # 顯示可修改的選項
            print("\n1. 修改部門\n2. 修改姓名\n3. 修改年齡\n4. 修改手機")
            option = input("請選擇要修改的欄位: ")

            # 根據選擇的欄位進行修改
            if option == '1':
                entry['部門'] = input("請輸入新的部門: ")
            elif option == '2':
                entry['姓名'] = input("請輸入新的姓名: ")
            elif option == '3':
                # 確保年齡為正整數
                new_age = input("請輸入新的年齡: ")
                while not new_age.isdigit() or int(new_age) <= 0:
                    new_age = input("年齡須為正整數，請重新輸入: ")
                entry['年齡'] = int(new_age)
            elif option == '4':
                entry['手機號碼'] = input("請輸入新的手機號碼: ")
            else:
                print("無效的選項，未進行修改。")
                return

            # 顯示更新後的資料
            print("\n--- 更新後的資料 ---")
            print(f"{'部門':<10}{'姓名':<10}{'年齡':<10}{'手機號碼':<15}")
            print('-' * 45)
            print(f"{entry['部門']:<10}{entry['姓名']:<10}{entry['年齡']:<10}{entry['手機號碼']:<15}")
            break
    else:
        # 查無此人
        print("查無此人。")

# 4. 刪除資料(由於時間不足先ChatGPT生成, 方待日後重構)
def delete_data(database: list):
    # 取得使用者輸入的姓名
    delete_name = input("請輸入要刪除的姓名: ")

    # 搜尋資料庫
    for i, entry in enumerate(database):
        if entry['姓名'] == delete_name:
            # 找到對應的姓名，詢問是否確認刪除
            confirm = input(f"確定要刪除 {delete_name} 的資料嗎? (y/n): ").lower()
            if confirm == 'y':
                # 刪除資料
                database.pop(i)
                print(f"{delete_name} 的資料已刪除。")
            else:
                print(f"未刪除 {delete_name} 的資料。")
            break
    else:
        # 若查無此人
        print("查無此人。")

    # # 列出剩餘的所有資料
    # print("\n--- 剩餘的所有資料 ---")
    # print(f"{'部門':<10}{'姓名':<10}{'年齡':<10}{'手機號碼':<15}")
    # print(f"----------------------------------------")  # 分隔線
    # for entry in database:
    #     print(f"{entry['部門']:<10}{entry['姓名']:<10}{entry['年齡']:<10}{entry['手機號碼']:<15}")

# 5-1. 顯示一筆資料(由於時間不足, 方待日後構建)
def output_data():
    pass

# 5-2. 顯示所有資料(由於時間不足先ChatGPT生成, 方待日後重構)
def output_database(database: list):
    # 定義表頭和對齊格式
    header = f"{'部門':<10}{'姓名':<10}{'年齡':<10}{'手機':<15}"
    print(header)
    print(f"----------------------------------------")  # 分隔線

    # 逐行輸出每筆資料
    for entry in database:
        department = entry['部門']
        name = entry['姓名']
        age = entry['年齡']
        phone = entry['手機號碼']

        # 使用格式化來處理對齊
        print(f"{department:<10}{name:<10}{age:<10}{phone:<15}")
