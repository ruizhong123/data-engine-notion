# 資料工程筆記
   資料工程是軟體開發中一項重要工程，主要處理客戶資料或其他資訊轉換上道傳軟體介面方便使用以及提供資料科學家和資料分析師方便分析使用，
為了更加方便理解資料工程整個轉換過程，主要會介紹五項應用軟體在資料轉換的過程，分別是docker、SQL、EL(Extract、Load)、DBT(Transformation)
、Airflow 以及 Airbyte，來做為資料工程中主要的工具。

## Docker (容器化)
docker 是軟體開發中一個包裝工具，docker在程式的運行中主要有映像以及容器，映像主要是以文件檔，以dockerfile、docker-compose 呈現，
而容器視為程式正在運行時的文件檔，主要是可以模擬當程式運行在雲端機台是否會有bug錯誤，而為什麼 docker 作為資料工程最重要的一項技能之一，
是因為 docker 可以模擬機台運行程式時在自動爬取資料的情形，而 docker 在 data engine中主要會常用到host(主機端)、port(端口)、network(網路連接)
、environment(環境)、volume(容器)、depend_on(相依)、image(映像)、build(創建)以及 dockerfile 等語言指令。

### &nbsp;&nbsp;&nbsp;host(主機端口):模擬整個環境系統，可以模擬執行檔在環境運作的過程以及資料庫在環境中處理的情況，並且在語法中主要是包含整個docker中所有指令(除了server最大之外)。

### &nbsp;&nbsp;&nbsp;映像檔(image): 以dockerfile為基礎，可建立資料庫以及提供執行檔運行環境  






