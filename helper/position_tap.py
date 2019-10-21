def target_click(self, x1, y1):  # x1,y1为你编写脚本时适用设备的实际坐标
    wd = self.wd
    x_1 = x1 / 375  # 计算坐标在横坐标上的比例，其中375为iphone6s的宽
    y_1 = y1 / 667  # 计算坐标在纵坐标667为iphone6s的高
    x = wd.get_window_size()['width']  # 获取设备的屏幕宽度
    y = wd.get_window_size()['height']  # 获取设备屏幕的高度
    print
    x_1 * x, y_1 * y  # 打印出点击的坐标点
    wd.tap([(x_1 * x, y_1 * y)], 500)  # 模拟单手点击操作