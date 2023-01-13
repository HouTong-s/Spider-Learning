import yagmail 
yag = yagmail.SMTP(user='ht1291227829@163.com',           #用户名
                            password='VPSFMOHBWISASQFY',                  #密码
                            host='smtp.163.com',               #主机
                            port='465')                          #端口
message = "亲，抢票成功，请在半个小时之内前往支付！"
#发送邮件
yag.send(to="1291227829@qq.com",
                                #目标邮箱地址（从buy_tickets.txt中获取）
        subject='12306购票成功通知',                   #邮件标题
        contents=message)                             #邮件内容