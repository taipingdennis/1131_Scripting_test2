# 題目：簡易人事資料管理系統實作
# Main execution

def main(database: list):
    while True:
        import functions as f
        print(
"""
--- 人事資料管理系統 ---
1. 新增資料
2. 查詢資料
3. 修改資料
4. 刪除資料
5. 顯示所有資料
6. 退出系統
------------------------"""
        )
        option_dict = {
            '1': f.create_data,
            '2': f.read_data,
            '3': f.update_data,
            '4': f.delete_data,
            '5': f.output_database,
        }
        option = input("請選擇功能: ")

        # 退出系統
        if option == '6':
            print(f"系統已退出。")
            break

        # 確保輸入有效選項
        while option not in option_dict:
            option = input("輸入錯誤, 請重新選擇: ")

        # 執行選擇的功能 (根據函式是否需要參數來決定是否傳遞database)
        try:
            option_dict[option](database)
        except TypeError:
            option_dict[option]()

# 待處理: 退出系統後再重啟系統, 無法保留上次的資料庫紀錄
database = list()
main(database)
