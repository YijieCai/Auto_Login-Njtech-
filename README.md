## Auto_Login (windows) 流程
    |---安装python(推荐3.10，因为我用的是3.10)和必要的python库

        |---python3.10 (URL:https://www.python.org/downloads/windows/)
    
        |---python library(库: ddddocr selenium requests time pillow subprocess )
    
    |---安装Chrome和ChromeDriver

        |---确定Chrome版本
    
        |---下载ChromeDriver(对应版本)
        
    |---Auto_Login_njtech.py

        |---01判断是否有网
        
        |---02如果无网络则尝试登录校园网
        
        |---03超过100次登录失败可能是没办法登录页面，重启
        
## 如何实现开机自动运行？

Win10系统的开机启动文件夹路径为：

【C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp】

任何放在这个文件夹中的程序快捷方式，都会在系统开机后自动启动。

将Auto_Login_njtech.py放入该文件夹，注意：开机有密码可以通过pyautogui实现，但是无法保证安全性。


## 如何安装ChromeDriver？
1、打开chrome浏览器

2、输入chrome://version 

3、得到版本号：Chrome_Version: 132.0.6834.84 (正式版本) （64 位） (cohort: Stable Installs & Version Pins) 

4、通过以下之一的方式下载chromedriver

[1]访问google的chromedriver官方下载站：

https://chromedriver.storage.googleapis.com

[2]或者打开下面网址，即可直接下载对应版本chromeDriver，在[Chrome_version]中输入版本号：

https://storage.googleapis.com/chrome-for-testing-public/[Chrome_version]/win64/chromedriver-win64.zip

例如：

https://storage.googleapis.com/chrome-for-testing-public/132.0.6834.84/win64/chromedriver-win64.zip

5、下载的压缩包中的chromedrvier文件放入python环境的Scripts文件夹中

参考路径：C:\Users\Administrator\AppData\Local\Programs\Python\Python310\Scripts

6、检测驱动是否安装成功

使用02Test Driver.py 顺利打开网页即为成功

参考

https://zhuanlan.zhihu.com/p/110274934

https://www.cnblogs.com/doudoua123/p/18513903

## ddddocr运行失败？

运行01OCR.py测试ddddocr是否正常运行

可能报错：ImportError: DLL load failed while importing onnxruntime_pybind11_state: 找不到指定的模块。

下载VC++ 2019解决该问题

参考:

https://blog.csdn.net/zhuchengchengct/article/details/124854199

https://www.bilibili.com/video/BV16K6aY8EW3/

## 不知道如何用代码定位'按钮'或'输入窗口'？

在想要定位的页面按下F12，逐行找到你想要确定的模块（鼠标停留在相应的代码块，页面会有颜色标记）

当颜色标记缩小到最小时，右键，找到Copy选项，Copy Xpath。

获得如下格式的信息：//*[@id="login-normal"]/div[2]/form/app-verification/nz-input-group/input

在单引号(必须是单引号，因为信息中存在双引号)中粘贴Xpath信息：Xpath：driver.find_element(By.XPATH,'')

如aim_block=driver.find_element(By.XPATH,'//*[@id="login-normal"]/div[2]/form/app-verification/nz-input-group/input')



