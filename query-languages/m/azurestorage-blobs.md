---
title: "AzureStorage.Blobs | Microsoft Docs"
ms.date: 10/10/2019
ms.service: powerquery
ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo
---
# AzureStorage.Blobs

## Syntax

<pre>
AzureStorage.Blobs(<b>account</b> as text, optional <b>options</b> as nullable record) as table
</pre>
  
## About  

Returns a navigational table containing a row for each container found at the account URL, <code>account</code>, from an Azure storage vault. Each row contains a link to the container blobs. <code>options</code> may be specified to control the following options: <ul> <li><code>BlockSize</code> : The number of bytes to read before waiting on the data consumer. The default value is 4 MB.</li> <li><code>RequestSize</code> : The number of bytes to try to read in a single HTTP request to the server. The default value is 4 MB.</li> <li><code>ConcurrentRequests</code> : The ConcurrentRequests option supports faster download of data by specifying the number of requests to be made in parallel, at the cost of memory utilization. The memory required is (ConcurrentRequest * RequestSize). The default value is 16.</li> </ul> 
  
