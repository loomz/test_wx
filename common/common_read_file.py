import xlrd
import json
import csv
import yaml


class CommonReadFile(object):

    def get_data_excel(self, filename, sheet):
        wb = xlrd.open_workbook(filename)
        # wb.sheet_by_index(0) 通过索引获得工作薄
        sheet = wb.sheet_by_index(sheet)
        rows = sheet.nrows  # 获取总行数
        cols = sheet.ncols  # 获取总列数
        lit = []
        for row in range(rows):  # 遍历行
            row_arr = []
            for col in range(cols):  # 遍历列
                col_data = sheet.cell_value(row, col)  # 获取单元格的值
                col_type = sheet.cell_type(row, col)  # 数据类型
                print("col_value=%s, col_type=%s" % (col_data, col_type))
                row_arr.append(col_data)
            lit.append(row_arr)

        print(lit)
        return lit

    def get_data_json(self, file_json):
        with open(file_json, encoding="utf-8") as f:
            lit = []
            keys = json.load(f)
            for key in keys:
                if len(key.values()) == 1:
                    lit.extend(key.values())
                else:
                    lit.append(tuple(key.values()))
            return lit

    def get_data_yaml(self, file_name):
        data = []
        with open(file_name, encoding="utf-8") as f:
            dict_data = yaml.safe_load(f.read())
            for i in dict_data:
                data.append(tuple(dict_data[i].values()))
        return data

    def get_data_csv(self, file_csv):
        # with opn 打开某文件 定义别名 f
        with open(file_csv, encoding="utf-8") as f:
            # 读取里面值
            lst = csv.reader(f)
            my_data = []
            for row in lst:
                if len(row) == 1:
                    my_data.extend(row)
                else:
                    my_data.append(row)
            return my_data