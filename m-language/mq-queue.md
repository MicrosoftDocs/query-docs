---
title: "MQ.Queue | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 9c5b8ef0-7387-4d08-9e0d-8912c4d9d8c2
caps.latest.revision: 3
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# MQ.Queue
<code>MQ.Queue(**server** as text, **queuemanager** as text, **channel** as text, **queue** as text, optional **options** as nullable record) as table</code>

## About
Returns a table that defines the IBM WebSphere MQ Server information required for reading and writing messages. It requires the following parameters: 

- <code>Server</code> name or address with an optional port number, separated by a colon, <code>server</code> (port 1414 will be used by default).
- The name of the <code>queue manager</code>, <code>queuemanager</code> on the MQ server.
- The name of the <code>channel</code>, <code>channel</code> for the queue manager on the MQ server.
- The name of the <code>queue</code>, <code>queue</code> to be accessed.

When this function is enumerated it returns a table containing messages in the queue via a non-destructive read. An optional record parameter, <code>options</code>, may be specified to control the following options: 

* <code>BinaryDisplayEncoding</code> : The binary value will be returned as text with the specified encoding. Affects the following columns in the output: MessageId, CorrelationId, AccountingToken, GroupId, and MsgToken. If it's not specified, the value will be returned as a binary value. The following values may be used: 
	* <code>BinaryEncoding.Base64</code>
	* <code>BinaryEncoding.Hex</code>
	* <code>TextEncoding.Utf16</code>
	* <code>TextEncoding.Unicode</code>
	* <code>TextEncoding.BigEndianUnicode</code>
	* <code>TextEncoding.Windows</code>
	* <code>TextEncoding.Ascii</code>
	* <code>TextEncoding.Utf8</code>
   
* <code>MessageDataDisplayEncoding</code> : Message Data is returned as a UTF8 representation of the underlying binary value by default. Supports the same values as the <code>BinaryDisplayEncoding</code> option. Also supports <code>type binary</code> to retrieve the message data as a binary value.
* <code>Timeout</code> : If a message is not in the queue, wait this amount of time for a message to appear. The default value is zero. Specified as a duration.

The record parameter is specified as [option1 = value1, option2 = value2...] or [BinaryDisplayEncoding = BinaryEncoding.Hex] for example. <code>Table.SelectRows</code> may be used to filter the messages to be retrieved from the queue. The following columns will be folded into the query: 
* <code>MessageId</code> : The message identifier of the MQ message to be retrieved. This can be a text or binary value.
* <code>CorrelationId</code> : The correlation identifier of the MQ message to be retrieved. This can be a text or binary value.
* <code>MessageToken</code> : The message token of the MQ message to be retrieved. This can be a text or binary value.
* <code>GroupId</code> : The group identifier of the MQ message to be retrieved. This can be a text or binary value.
* <code>Offset</code> : The offset of the MQ message to be retrieved. This is an integer value. (Not available on MQ z/OS).
* <code>LogicalSequenceNumber</code> : The logical sequence number of the MQ message to be retrieved. This is an integer value.

Note: When these columns are combined with other non-foldable columns the query might not be folded. <code>Table.FirstN</code> may be used to limit the number of messages retrieved from the queue. When not specified, only the first 500 messages will be retrieved. <code>Table.SelectColumns</code> may be used to restrict the columns returned by the function. <code>TableAction.DeleteRows</code> may be used to destructively get messages from the queue. <code>TableAction.InsertRows</code> may be used to send messages to the queue. The following message properties are writable: 
   
* <code>MessageData</code> : Message data. This is the only required column. Can be a text or binary value.
* <code>CorrelationId</code> : The correlation identifier of the MQ message to be sent. This can be a text or binary value.
* <code>Ccsid</code> : The character set for the message. By default, the character set on the MQ Server will be used.
* <code>MessageId</code> : The message identifier of the MQ message to be sent. This can be a text or binary value.
* <code>MessageType</code> : Valid message types are "Datagram", "Reply", or "Request". The default value is "Datagram".
* <code>Offset</code> : Message offset. The default is 0. <code>ReplyToQueue</code> : If the message type is "Request", then the Reply to Queue can be specified. The default is to use the queue as defined in <code>MQ.Queue</code>.
* <code>ReplyToQueueManager</code> : Name of the Queue Manager for the ReplyToQueue. The default is to use the queue manager as defined in <code>MQ.Queue</code>.

  
