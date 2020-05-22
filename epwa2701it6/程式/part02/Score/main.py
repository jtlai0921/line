# 載入scoprocess套件中的模組，並且指定簡稱
import scoprocess.scocheck as sc
import scoprocess.scosort as ss

# 建立一個成績資料組
scores = [80, 95, 70, 40, 65, 55, 75, 50, 90]

# 呼叫scocheck模組中的函式處理成績資料組，並且顯示結果
print('最高分：', sc.highest(scores))
print('最低分：', sc.lowest(scores))
print('平均分數：', sc.average(scores))
print('及格：', list(sc.get_pass_scores(scores)))
print('不及格：', list(sc.get_fail_scores(scores)))

# 呼叫scosort模組中的函式對成績資料組進行排序，並且顯示結果
print('由低到高排序：', list(ss.sort_low_to_hight(scores)))
print('由高到低排序：', list(ss.sort_high_to_low(scores)))