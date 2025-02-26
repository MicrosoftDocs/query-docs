---
description: "Learn more about: AzureStorage.DataLakeContents"
title: "AzureStorage.DataLakeContents"
ms.subservice: m-source
---
# AzureStorage.DataLakeContents

## Syntax

<pre>
AzureStorage.DataLakeContents(<b>url</b> as text, optional <b>options</b> as nullable record) as binary
</pre>

## About

Returns the content of the file at the URL, `url`, from an Azure Data Lake Storage filesystem. `options` may be specified to control the following options:

* `BlockSize`: The number of bytes to read before waiting on the data consumer. The default value is 4 MB.
* `RequestSize`: The number of bytes to try to read in a single HTTP request to the server. The default value is 4 MB.
* `ConcurrentRequests`: The ConcurrentRequests option supports faster download of data by specifying the number of requests to be made in parallel, at the cost of memory utilization. The memory required is (ConcurrentRequest * RequestSize). The default value is 16.
