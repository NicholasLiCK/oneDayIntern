# oneDayIntern

ADL
https://docs.microsoft.com/zh-tw/azure/storage/blobs/data-lake-storage-introduction

using console for fast development

主要的目標：
Parse the required PTT data and display the articles. The attached file ptt_dump_20210218_1141.json is an example. You need to use the raw data on Azure Data Lake Storage(ADLS).
Definition of the columns can be found in the attached image definition.png.
Please reference here and the attached file credentials.txt to get some useful tools. (Storage Explorer, CLI, etc.)
 

Design a user interface to show parsed results.
 

Filter the articles with the keyword “愛莉莎莎” and “天竺鼠車車” if they are in one of the 3 columns: “article_title”, “content”, and “messages”.
(We are big fans of Alisasa, and we really want to know what is Pui Pui!!)
 

Dump the contents into folder structure. Either graphical, text-like or any other representations are fine.
