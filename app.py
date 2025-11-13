import os  # F401: 未使用 import
import sys
import json  # 這三個都沒用到 → 觸發 F401

# E501: 行太長（超過 88 字元）
very_long_variable_name_that_will_definitely_exceed_the_max_line_length_set_by_black_and_flake8 = "This is a super long string to trigger line too long error in flake8"

def hello_world():
print("Hello, DevSecOps!" * 5)  # E111: 縮排錯誤（少了 4 個空格） + E225: 缺少空格

# W291: 行尾有多餘空白  
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]   