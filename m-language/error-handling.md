---
title: "Error handling | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "index-page "
ms.assetid: defd5222-fb73-4ce7-b6d4-d2c72d0c2967
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Error handling
[!INCLUDE[mIntroText](../includes/mintrotext-md.md)]  
  
## <a name="__toc360789892"></a>Error  
  
|Function|Description|  
|------------|---------------|  
|[Diagnostics.ActivityId](diagnostics-activityid.md)|Returns an opaque identifier for the currently-running evaluation.|
|[Diagnostics.Trace](diagnostics-trace.md)|Writes a trace message, if tracing is enabled, and returns value.|  
|[Error.Record](error-record.md)|Returns a record containing fields “Reason”, “Message”, and “Detail” set to the provided values. The record can be used to raise or throw an error.|  
|[TraceLevel.Critical](tracelevel-critical.md)|Returns 1, the value for Critical trace level.|  
|[TraceLevel.Error](tracelevel-error.md)|Returns 2, the value for Error trace level.|
|[TraceLevel.Information](tracelevel-information.md)|Returns 4, the value for Information trace level.|
|[TraceLevel.Verbose](tracelevel-verbose.md)|Returns 5, the value for Verbose trace level.|
|[TraceLevel.Warning](tracelevel-warning.md)|Returns 3, the value for Warning trace level.|