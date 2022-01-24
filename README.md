# TelloWithLabVIEW
Using Tello with LabVIEW Tutorial

https://docs.google.com/document/d/1MxncDF8ot3yZ3Vr71-20pyanfowkeBq7ZZbCbNtm6GM/


# Using Tello with LabVIEW Tutorial 


此 Tutorial 的目的是希望藉由圖形化的 NI LabVIEW 來快速完成對 Tello SDK 命令的發送和接收，透過 LabVIEW Python node 取得 Tello 前鏡頭串流的畫面，甚至更進一步以 LabVIEW Vision Developement Module 完成更簡單上手的影像處理。 



# 一、安裝合適版本的 LabVIEW

LabVIEW 2018 (含以後) 的版本才支援 Python node，2018 支援 Python 2.7 和 3.6，2021 則支援 3.6 ~ 3.9 各版本 (不再支援 2.7)，使用 64 或 32 位元的 LabVIEW，就必需安裝對應位元版本的 Python。

按：我做 Term Project 的時候是使用了 LabVIEW 2021 64 bit 搭配 Python 3.9.9 64 bit，但經測試 LabVIEW 2018 32 bit 搭配 Python 3.6 32bit 也可以，推測 64 bit 應該也沒問題。



1. 到 NI LabVIEW 的下載頁面 
[LabVIEW Download - NI](https://www.ni.com/zh-tw/support/downloads/software-products/download.labview.html#) 

2. 下載 Windows 版本的 LabVIEW 2021 64bit 主程式 (不含驅動程式) 
(Install offline可以直接下載iso)    

3. 掛接該 iso 並執行 Install 安裝程式 

4. 按照預設的勾項一路裝到底就可以 


裝完要重新開機

5. 想用 LabVIEW 來處理影像的話，要再下載 [機器視覺開發 (Vision Development) 模組](https://www.ni.com/zh-tw/support/downloads/software-products/download.vision-development-module.html#) (VDM)，如果只是要顯示 Python + OpenCV 處理過的畫面可以不裝。 


裝完一樣要重開機 



6. 要用 LabVIEW 來擷取 USB 攝影機影像的話，還要再裝 [Vision Acquisition Software](https://www.ni.com/zh-tw/support/downloads/drivers/download.vision-acquisition-software.html#) (VAS)，跟 5. 的 VDM 一樣，它會自動選擇要安裝的版本。 \
 
裝完一樣要重開機


# 二、安裝合適版本的 Python

[Download Python | Python.org](https://www.python.org/downloads/)


LabVIEW 聲明不支援的版本，有時候也可能是可以用的，像是現在最新的3.10.2，不在官方宣稱的 3.6 ~ 3.9 但是我實測也是可以使用的，不過安裝的位元版本一定要和 LabVIEW 相同。



1. 下載與 LabVIEW 相同位元版本之 Python 並安裝
2. 先更新 pip，才不會在安裝 OpenCV 時發生奇怪的錯誤
 $python -m pip install –upgrade pip 
   
3. 再安裝相對應的 OpenCV  
$pip install opencv-python 



# 三、範例說明

 
打開從 Github 上下載的 LabVIEW 2018 範例 [TelloWithLabVIEW2018](https://github.com/JohnGDR08g/TelloWithLabVIEW) 點開 TelloVision_2018 資料夾，打開 TelloVisionTutorial 


 
可以看到專案視窗如下： 



1. UDPSingleCommandSender.vi 

    在本機電腦連上 Tello 的 WiFi 後，搭配 [Tello SDK 2.0](https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello_SDK_2.0_使用说明.pdf) 可以對 Tello 發送已輸入或未輸入但有列在 Tello SDK 2.0 裡的命令 (非 EDU 版只能使用 [Tello SDK](https://dl-cdn.ryzerobotics.com/downloads/tello/20180910/Tello%20SDK%20Documentation%20EN_1.3.pdf) 1.3) 
 
    Tello IP 的內容可以直接輸入更改，或是編輯 TelloIP.ctl 變更預設值
    Command 也是一樣，直接在空白處輸入命令，或是點擊下拉選擇預先輸入的命令，再按 Send 即可發送各種 SDK 命令給 Tello，收到回覆會顯示在 Return 顯示元件裡

2. UDPStateReceiver.vi


    執行 StateReceiver 可以收到 Tello的狀態，可參閱 SDK 裡 「Tello State」說明

  

3. PythonNodeForTelloVisionTester.vi


    先在 CommandSender 裡送出「command」、「streamon」後，就可以執行這個 vi 透過 Python Node 呼叫 OpenCV 得到 Tello 的串流畫面 (需安裝 VDM)。

    也可以透過修改資料夾內的 videoOnly.py 來修改擷取串流的功能，像是 IP、更改傳送的影像大小、是不是要先做處理…等等，要做YOLO之類的應該也是沒有問題。

    特別要注意的是綠色框裡的路徑要是 videoOnly.py 的絕對路徑，粉色框裡寫的.py 是要呼叫的 Python 檔名，3.6 是安裝的 Python 版本， startcap 跟 stopcap 是寫在 .py 內的 function name ，若要使用 class ，請參考 NI 官網說明  
[使用LabVIEW Python Node呼叫Python Class Methods - NI](https://knowledge.ni.com/KnowledgeArticleDetails?id=kA00Z0000019UFmSAM&l=zh-TW)



4. TelloDemoExample.vi

    就是我們 DEMO 的程式，沒有特別整理，但是有一些組合上面範例的參考，也有用到 keyboardTester.vi 來讓 Tello 可以被鍵盤操控飛行，不一定要提供給同學。 

