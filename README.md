# 資料工程筆記
   資料工程是軟體開發中一項重要工程，主要處理客戶資料或其他資訊轉換上道傳軟體介面方便使用以及提供資料科學家和資料分析師方便分析使用，
為了更加方便理解資料工程整個轉換過程，主要會介紹五項應用軟體在資料轉換的過程，分別是docker、SQL、EL(Extract、Load)、DBT(Transformation)
、cron(執行時間)、Airflow 以及 Airbyte，來做為資料工程中主要的工具。

## Docker (容器化)
docker 是軟體開發中一個包裝工具，docker在程式的運行中主要有映像以及容器，映像主要是以文件檔，以dockerfile、docker-compose 呈現，
而容器視為程式正在運行時的文件檔，主要是可以模擬當程式運行在雲端機台是否會有bug錯誤，而為什麼 docker 作為資料工程最重要的一項技能之一，
是因為 docker 可以模擬機台運行程式時在自動爬取資料的情形，而 docker 在 data engine中主要會常用到host(主機端)、port(端口)、network(網路連接)
、environment(環境)、volume(容器)、depend_on(相依)、image(映像)、build(創建)以及 dockerfile 等語言指令。

#### &nbsp;&nbsp;&nbsp;host(主機)
 &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;模擬整個環境系統，可以模擬執行檔在環境運作的過程以及資料庫在環境中處理的情況，並且在語法中主要是包含整個docker中所有指令  
 &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;(除了server最大之外)。

#### &nbsp;&nbsp;&nbsp;image(映像檔): 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 以dockerfile為基礎，可建立資料庫以及提供執行檔運行環境  

#### &nbsp;&nbsp;&nbsp; port(端口)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;想像為主機台相應的房號，若沒有指定的房號，資料在傳送的過程中會錯亂，主要的語法呈現為  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"主機端數字:docker-compose端口"

#### &nbsp;&nbsp;&nbsp; environment(環境)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;透過環境設置找到主要的資料庫，主要的語法有 POSTGRES_DB(資料庫名稱)、POSTGRES_USER(資料庫使用著)以及
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;POSTGRES_PASSWORD(資料庫密碼)

#### &nbsp;&nbsp;&nbsp; network(網路連接)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;決定容器之間資料傳送的方式  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - host(主機共享):容器跟主機共享一個端口  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - brdige(橋梁):容器之間有各自的端口且隔絕，可相互傳送  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - null(無):容器之間無任何橋梁且完全隔絕

#### &nbsp;&nbsp;&nbsp; volume(容器)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;連接資料庫來源，語法為 "./source_database/init.sql:/docker-entrypoint-initdb.d/init.sql"

## DBT(Data Build Transformation)
DBT 資料轉換套件包，為資料流主要處理文件檔，內建 model(資料場)、macro(內建函式套件包)、analyses(分析資料檔)、dbt_package(執行dbt套件包)、
log(偵測dbt的bug)、seeds(儲存小型csv檔資料)、snapshots(追蹤資料變化) 、target(資料轉換後的快取檔)、test(存放制定的資料品質測試，
如果有新模型的話可通過test進行測試)以及 main_project.yml(策畫整體資料轉換架構)

## CRON(排列指定的時間爬取資料)


## Airflow(自動排程)
設定 airflow 可以掌控 python 執行檔以及 docker 檔
-  設定 port(端口ui) 可以看到airflow 網站
-  Dag(安排時間爬取資料)
- 


## SQL(資料庫)
#### &nbsp;&nbsp; 合併資料
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SELECT f.film_id,f.title,a.actor_name  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FROM films f  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;INNER  JOIN  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;film_actors fa ON f.film_id = fa.film_id  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;INNER JOIN  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;actors a ON fa.actor_id = a.actor_id  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ORDER BY f.film_id;



































