![RAM Use](TRS80Pyramid.jpg)

# RAM Use

| | | |
| --- | --- | --- |
| 44A1      | isLoneObject          | 1 if a lone object was given last input      |
| 45A8      | nounDataSize          | Number of bytes in noun's data area          |
| 45A9      | someDecoded           | 1 if something was decoded from input        |
| 45AA:45AB | nounDataPtr           | Pointer to noun data                         |
| 465A:467A | inputBuffer           | User's input                                 |
| 467B      | inputNoun             | The user input noun                          |
| 467C      | inputVerb             | The user input verb                          |
| 467D      | verbGrammar           | The phrase's grammar type                    |
| 467E      | nextErrorNum          | Which general error to print next (0-3)      |
| 46FB      | nounMsgPunc           | Punctuation char for printed unknown noun    |
| 46D3:46FC | unknownNoun           | Copy of user's unknown noun text             |
| 46FD:4724 | unknownVerb           | Copy of user's unknwon verb text             |
| 4774      | keyWaitCount          | Rapidly bumped waiting on a key (random)     |
| 4779:477A | currentParsePtr       | Pointer to word table entry while parsing    |
| 477B:477C | inputWordPtr          | Pointer to word being tokenized              |
| 477D      | numCharsTest          | Number of chars in test word (tokenizing)    |
| 477E      | testWord              | First byte of word data (tokenizing)         |
| 481A      | shiftCount            | Count of shifts during the unpack algorithm  |
| 4884      | unpackNumWords        | Number of words to unpack (2-byte words)     |
| 4885:4886 | valueOfForty          | Used in dividing by 40 in unpack             |
| 4887      | unpackToScreen        | 1 to print to screen, 0 to given buffer      |
| 503F      | currentRoom           | (saved) The room the player is in            |
| 5040      | bcdTurnCountLSB       | (saved) Number of turns LSB                  |
| 5041      | bcdTurnCountMSB       | (saved) Number of turns MSB                  |
| 5042:5043 | lampOnTurnCount       | (saved) Number of turns the lamp has burned  |
| 5044      | lastRoom              | (saved) Last room the player was in          |
| 5045      | numObjInPack          | (saved) Number of objects in the pack        |
| 5046      | numResurrected        | (saved) Number of times player resurrected   |
| 54C5:54C6 | nextResurrectMsg      | Next resurrection message                    |
| 55B2      | scoreTempLSB          | Used in calculating/printing score           |
| 55B3      | scoreTempMSB          | Used in calculating/printing score           |
| 55BF      | scoreSign             | Sign char in print message                   |
| 55C0:55C3 | scoreMsg              | Where the score goes in the print message    |
| 55E3:55E6 | turnMsg               | Where the turn goes in the pring message     |

Stack initialized to 47BF
