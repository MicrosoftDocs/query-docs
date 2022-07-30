---
description: "Learn more about: AzureStorage.DataLakeContents"
title: "AzureStorage.DataLakeContents"
ms.date: 10/10/2019
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo
---
# AzureStorage.DataLakeContents

## Syntax

<pre>  
AzureStorage.DataLakeContents(<b>url</b> as text, optional <b>options</b> as nullable record) as binary
</pre>

## About  

Returns the content of the file at the URL, <code>url</code>, from an Azure Data Lake Storage filesystem. <code>options</code> may be specified to control the following options: <ul> <li><code>BlockSize</code> : The number of bytes to read before waiting on the data consumer. The default value is 4 MB.</li> <li><code>RequestSize</code> : The number of bytes to try to read in a single HTTP request to the server. The default value is 4 MB.</li> <li><code>ConcurrentRequests</code> : The ConcurrentRequests option supports faster download of data by specifying the number of requests to be made in parallel, at the cost of memory utilization. The memory required is (ConcurrentRequest * RequestSize). The default value is 16.</li> </ul> 
  
  
  
