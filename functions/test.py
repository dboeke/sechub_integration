import filter_function

event = {
    "Records": [
        {
            "messageId": "1f6fd4df-5b11-4d11-acf6-957b6e99fa6e",
            "receiptHandle": "AQEBfcsRZ9mv0NoPLwd2Jdhtok3Kf1Dae0jzYo9k1lu0wRlZUZJ7siZt6ffv3/+xA5gH70/8GvOzYLHwNtbmPdt5mcT/mXIXvb2rAH1AYZAIfkI0iVEfGHEOxhaxHhbKNQk2KBHY1cJNojTzhMJi5DDiY0twE3/1cN+tOJZr0OKl2Ai8Hw51UzmV4cWrGqI1Hijsuz05rTfOGWUY4IN8Olw9WI44Nu/qeNrNJHwJlbGV6AKv55/JzDDUxkiCuXEZSPVnSVvWFJZnDpkwudvMC6gJ80G6DCJfOIU4QiqwootN1C0tvvqslO0yhr9BdXzxzZlyMpSbq33ObJLqFR2pKbDw/ftZAkPsRQlXtXXI+EapImMA494WIkYM4467dPIZInfXmaZnloTQNBhZuejqGazRB8fskGU5ynRsi5o8Zvsla08=",
            "body": "{\n  \"Type\" : \"Notification\",\n  \"MessageId\" : \"cb145d6d-93e3-55d0-943a-05f3edaeaa77\",\n  \"TopicArn\" : \"arn:aws:sns:us-east-2:133534076130:turbot-firehose-user-sns-topic\",\n  \"Subject\" : \"[punisher-turbot] Control Approved updated by Turbot Identity\",\n  \"Message\" : \"{\\\"notificationType\\\":\\\"control_updated\\\",\\\"actor\\\":{\\\"identity\\\":{\\\"picture\\\":\\\"https://www.gravatar.com/avatar/cb9ff8606c24daf9cda1d82615bd7a8e\\\",\\\"turbot\\\":{\\\"title\\\":\\\"Turbot Identity\\\",\\\"id\\\":\\\"173249891011852\\\"}}},\\\"turbot\\\":{\\\"type\\\":null,\\\"controlId\\\":\\\"1000000\\\",\\\"controlOldVersionId\\\":\\\"216036333047576\\\",\\\"controlNewVersionId\\\":\\\"216036336629722\\\",\\\"createTimestamp\\\":\\\"2021-02-11T00:36:24.987Z\\\"},\\\"control\\\":{\\\"state\\\":\\\"alarm\\\",\\\"reason\\\":\\\"Approved\\\",\\\"details\\\":[{\\\"key\\\":\\\"Usage\\\",\\\"value\\\":\\\"Approved\\\"},{\\\"key\\\":\\\"Regions\\\",\\\"value\\\":\\\"Approved\\\"},{\\\"key\\\":\\\"Budget\\\",\\\"value\\\":\\\"Skipped\\\"},{\\\"key\\\":\\\"RESULT\\\",\\\"value\\\":\\\"Approved\\\"}],\\\"type\\\":{\\\"trunk\\\":{\\\"title\\\":\\\"AWS > S3 > Bucket > Approved\\\"}},\\\"turbot\\\":{\\\"id\\\":\\\"1\\\"},\\\"resource\\\":{\\\"akas\\\":[\\\"arn:aws:s3:::raj-switch-role-bucket\\\"],\\\"metadata\\\":{\\\"aws\\\":{\\\"accountId\\\":\\\"688720832404\\\",\\\"partition\\\":\\\"aws\\\",\\\"regionName\\\":\\\"us-east-2\\\"},\\\"createTimestamp\\\":\\\"2021-01-18T16:35:52.000Z\\\"},\\\"title\\\":null,\\\"turbot\\\":{\\\"id\\\":\\\"213971924734526\\\"}}},\\\"oldControl\\\":{\\\"state\\\":\\\"alarm\\\",\\\"turbot\\\":{\\\"id\\\":\\\"1000000\\\"}}}\",\n  \"Timestamp\" : \"2021-02-11T00:36:29.844Z\",\n  \"SignatureVersion\" : \"1\",\n  \"Signature\" : \"tXPOjoPlElJtiKWX5EIXMwLs7JRXKnj+xj1n4KL19w2tbgqbzmvV+ncRAogYoxdhI72oFvo1vaz2edOBB8O/9l9+8TvlLwx3MXw3fJidwOA6cXJMpux9ah+Fs/D137ebg7W24ibChWb+4CLDDAIyQUn5b1dtwdkN9ayein6uwIF7Bxr+N9M35homuEkDAZyVjvAPGd5TIn/EB+5WdLxa9UxpVHaTvJDXMvfjopdV37YzYgjYqupIhGmjRfE7JjXPqgnrONdoVQdbPxulQTKe1L4B0DsH1xORMSl+ZjLa2WacMLRIMJfFxM5qRcK/QJ6uhLpt+XUuDdqZSqirq4/0WQ==\",\n  \"SigningCertURL\" : \"https://sns.us-east-2.amazonaws.com/SimpleNotificationService-010a507c1833636cd94bdb98bd93083a.pem\",\n  \"UnsubscribeURL\" : \"https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-2:133534076130:turbot-firehose-user-sns-topic:a036479e-e982-4824-ad26-96f36636a384\"\n}",
            "attributes": {
                "ApproximateReceiveCount": "1",
                "SentTimestamp": "1613003789875",
                "SenderId": "AIDAIVEA3AGEU7NF6DRAG",
                "ApproximateFirstReceiveTimestamp": "1613003789876"
            },
            "messageAttributes": {},
            "md5OfMessageAttributes": None,
            "md5OfBody": "2e8279f5dd14f0c58de655e94a1ab551",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:us-east-2:133534076130:morales_firehose_raw_alarms_queue",
            "awsRegion": "us-east-2"
        }
    ]
}

event = {
    "Records": [
        {
            "messageId": "1133f0ec-930f-436c-a1e9-5c09a1065451",
            "receiptHandle": "AQEBF+mBLg8hOskFKl+QPWymSdTsOhlAj0kZf+oZ5LqEMMqauCoIXd2Nx1XNArFAgfoddVLyn7OHOelHa365d+Qj5IMeqxbpptsfBI3dfhSm/+G3fMRpDbJfl8jjhHoBKUnTsrgxxtfrvb8PigShxUJB1Zm2Bk7hH6P0RKz1MBAz0DUUJFS04GcyQxip9x/KqksYX4bv5SxOqaIbzT7D5JohhhrHCvJSdrH3WfXfJunckiJOjchkMkGqJbvlvIiPGg1naehgI5pREhAnP6z4SYjgbo2Oyqzr7sOjo2eB9UwPGv731rSgcW73chFIkNjUr4D2wglwB19fawtXd3is7m+CL+30F30p7XZ5a8xMZKwdRqAqT2lTxEUdZ8nQ9aHsyN2m+7JRMEdCwLc7Y7I9l8G7S9Tdx6qNr5AvfKLu9kaOO94=",
            "body": '{\n'
                       '  "Type" : "Notification",\n'
                       '  "MessageId" :  "790ec497-645c-5a09-a3e1-9f984caf944f",\n'
                       '  "TopicArn" :  "arn:aws:sns:us-east-2:133534076130:morales_firehose_raw_alarms",\n'
                       '  "Subject" : "[morales-turbot] Control Encryption at Rest updated by Turbot Identity",\n'
                       '  "Message" : "{\\"notificationType\\":\\"control_updated\\",\\"actor\\":{\\"alternatePersona\\":null,\\"identity\\":{\\"title\\":\\"Turbot Identity\\",\\"picture\\":\\"https://www.gravatar.com/avatar/cb9ff8606c24daf9cda1d82615bd7a8e\\",\\"turbot\\":{\\"title\\":\\"Turbot Identity\\",\\"id\\":\\"165643662385311\\"}}},\\"turbot\\":{\\"type\\":null,\\"controlId\\":\\"257954811436181\\",\\"controlOldVersionId\\":\\"257956495414019\\",\\"controlNewVersionId\\":\\"257956994434036\\",\\"createTimestamp\\":\\"2022-05-30T20:18:47.375Z\\"},\\"control\\":{\\"state\\":\\"alarm\\",\\"reason\\":\\"Default Encryption at Rest and Encryption at Rest is set as per policy\\",\\"details\\":null,\\"type\\":{\\"trunk\\":{\\"title\\":\\"AWS > S3 > Bucket > Encryption at Rest\\"}},\\"turbot\\":{\\"id\\":\\"257954811436181\\"},\\"resource\\":{\\"title\\":null,\\"metadata\\":{\\"aws\\":{\\"accountId\\":\\"133534076130\\",\\"partition\\":\\"aws\\",\\"regionName\\":\\"us-east-2\\"},\\"createTimestamp\\":\\"2022-05-30T19:43:10.000Z\\"},\\"turbot\\":{\\"title\\":\\"sh-firehose-test-bucket-001\\",\\"tags\\":{},\\"id\\":\\"257954811181128\\"}}},\\"oldControl\\":{\\"state\\":\\"ok\\",\\"turbot\\":{\\"id\\":\\"257954811436181\\"}}}",\n'
                       '  "Timestamp" : "2022-05-30T20:18:59.534Z",\n'
                       '  "SignatureVersion" : "1",\n'
                       '  "Signature" : "Q0sDLN/3OhuKVX61bvw5ISuZb0gAZLscsZsMQaludpeRkRkm/DOtr1PWrNMjDwjewJZbmSORgLWW71tKFWoypxnNMprBe/jKdkciKvyXbkuAkvdqd1nmNm3m3HlS4Ay+jPr9uMU+IV0NNOv6+WH6OUG+/VgTr36+rT/nbSVAH/Xj9X55vtwxzf3LKFH21uCaQc48oQ3v0NKGWZz5Fjj8PIH52KXm/t0KyhUiwtokJmgeIuq4xYILxOdWdIDHslS8Sjql2mBzv3IqxEn3DsOaAJ3EvGYRGaGogHeySlrbE9cEwP5ZcMpHIrmTzN7pO2aSCnmjkUj3UEu6hGdq1FQ0hw==",\n'
                       '  "SigningCertURL" : "https://sns.us-east-2.amazonaws.com/SimpleNotificationService-7ff5318490ec183fbaddaa2a969abfda.pem",\n'
                       '  "UnsubscribeURL" : "https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-2:133534076130:morales_firehose_raw_alarms:824101b1-216c-4535-9dc6-c036a2f6d6fd"\n}',
            "attributes": {
                "ApproximateReceiveCount": "1",
                "SentTimestamp": "1613003789875",
                "SenderId": "AIDAIVEA3AGEU7NF6DRAG",
                "ApproximateFirstReceiveTimestamp": "1613003789876"
            },
            "messageAttributes": {},
            "md5OfMessageAttributes": None,
            "md5OfBody": "ddbe69aecbde55b39c9087060b71d7da",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:us-east-2:133534076130:morales_firehose_raw_alarms_queue",
            "awsRegion": "us-east-2"
        }
    ]
}

# event = {
#     "Records": [
#         {
#             "messageId": "7df58378-3163-4b8b-b077-3de9131349ed",
#             "receiptHandle": "AQEBukY2yqFumYbmEAqev46naZH819Xr2SJY0+Ne+Umh1KIXAjavY5Mbe9i4f9DNjB69HpMpnxLxFIkSjZGhQwnM2nIIXiC4reyJdxpo/HmvkXO9LhS4orX5o+XbaSRLmuTij693/finqbP1na9qvvaS4vsifEetRsKykbReSEhD/O3Cn/gxOe2CofBHEkgWX9+0jh4omEXoIhwZNmAtyCjSRfHM+0bycXnJhjyBA8re3lywt+ZRs4G3sHdm6vAVwgLDujUC8Lr8jZJw7HzWP7E3PXruO+XBeW6+5UCAmbNYneWjk+CKe9mFfo9nNa7V8rQ+O8OyqgmQ/ybsJJ3cdiMknm4vIHAdVmYhT4GdMnFUxIj5KB0+5Z/Vyq+zYnpn+DW+epc3JkVfPyIO/0fBaOMt+1a5UtfzkOJ/ydqqQSeUeMU=",
#             "body": "{\n  \"Type\" : \"Notification\",\n  \"MessageId\" : \"9b2c3e73-ac08-569b-83ed-66edd243057e\",\n  \"TopicArn\" : \"arn:aws:sns:us-east-2:133534076130:turbot-firehose-user-sns-topic\",\n  \"Subject\" : \"[punisher-turbot] Control Approved updated by Turbot Identity\",\n  \"Message\" : \"{\\\"notificationType\\\":\\\"control_updated\\\",\\\"actor\\\":{\\\"identity\\\":{\\\"picture\\\":\\\"https://www.gravatar.com/avatar/cb9ff8606c24daf9cda1d82615bd7a8e\\\",\\\"turbot\\\":{\\\"title\\\":\\\"Turbot Identity\\\",\\\"id\\\":\\\"173249891011852\\\"}}},\\\"turbot\\\":{\\\"type\\\":null,\\\"controlId\\\":\\\"21212\\\",\\\"controlOldVersionId\\\":\\\"216036328690947\\\",\\\"controlNewVersionId\\\":\\\"216036333047576\\\",\\\"createTimestamp\\\":\\\"2021-02-11T00:36:21.489Z\\\"},\\\"control\\\":{\\\"state\\\":\\\"alarm\\\",\\\"reason\\\":\\\"Not approved\\\",\\\"details\\\":[{\\\"key\\\":\\\"Usage\\\",\\\"value\\\":\\\"Not approved\\\"},{\\\"key\\\":\\\"Regions\\\",\\\"value\\\":\\\"Approved\\\"},{\\\"key\\\":\\\"Budget\\\",\\\"value\\\":\\\"Skipped\\\"},{\\\"key\\\":\\\"RESULT\\\",\\\"value\\\":\\\"Not approved\\\"}],\\\"type\\\":{\\\"trunk\\\":{\\\"title\\\":\\\"AWS > S3 > Bucket > Approved\\\"}},\\\"turbot\\\":{\\\"id\\\":\\\"12121212\\\"},\\\"resource\\\":{\\\"akas\\\":[\\\"arn:aws:s3:::raj-switch-role-bucket\\\"],\\\"metadata\\\":{\\\"aws\\\":{\\\"accountId\\\":\\\"133534076130\\\",\\\"partition\\\":\\\"aws\\\",\\\"regionName\\\":\\\"us-east-2\\\"},\\\"createTimestamp\\\":\\\"2021-01-18T16:35:52.000Z\\\"},\\\"title\\\":null,\\\"turbot\\\":{\\\"id\\\":\\\"213971924734526\\\"}}},\\\"oldControl\\\":{\\\"state\\\":\\\"ok\\\",\\\"turbot\\\":{\\\"id\\\":\\\"213971925119603\\\"}}}\",\n  \"Timestamp\" : \"2021-02-11T00:36:27.806Z\",\n  \"SignatureVersion\" : \"1\",\n  \"Signature\" : \"jltPaywEJtOXY3DFqyZc5I4Xud2sSUbaRlzmDtw/VoO0lFOtyJpPFICOjkZ1diEhByS0cFXToMELtQ9JUGdzcPqATkWbouVA5CtldP1uqBctRpI6UhWkwq33LEmkP798j6IfwPevNa7r5EiITPlBogkbtung5OYOSMKGgQtsW713mBDgMkKXDypb75y/teYBIjiNRjcnodb2TLYFz2aaOjm7yGQgGiRq8hQPTjxSeR1k3KwinH+a6+rhFx/rTymCLeY8CCqidgjiFP61FOv7l4SOIbaqj1HbaiTWk1rl1exIYMtSpGLQz00lA1HwGiE2mG7iPEBTDvIbv5p7IqMRCw==\",\n  \"SigningCertURL\" : \"https://sns.us-east-2.amazonaws.com/SimpleNotificationService-010a507c1833636cd94bdb98bd93083a.pem\",\n  \"UnsubscribeURL\" : \"https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-2:133534076130:turbot-firehose-user-sns-topic:a036479e-e982-4824-ad26-96f36636a384\"\n}",
#             "attributes": {
#                 "ApproximateReceiveCount": "1",
#                 "SentTimestamp": "1613003787831",
#                 "SenderId": "AIDAIVEA3AGEU7NF6DRAG",
#                 "ApproximateFirstReceiveTimestamp": "1613003787832"
#             },
#             "messageAttributes": {},
#             "md5OfMessageAttributes": None,
#             "md5OfBody": "497fbcfef2d2b1aa318975f4d5d6628c",
#             "eventSource": "aws:sqs",
#             "eventSourceARN": "arn:aws:sqs:us-east-2:133534076130:morales_firehose_raw_alarms_queue",
#             "awsRegion": "us-east-2"
#         },
#         {
#             "messageId": "a93fef48-d66b-443c-bb03-6a01032258fa",
#             "receiptHandle": "AQEBh8u2Gu6qE/2GQA2NiDIPLgKvbPoTtfOU429sFRm/wODF+8ZEb8QR3Cl86l2SD66wdTXHewS8N7TTwU0uKLo3aXEHdlGQrV68x0C88PVQZ0eunaEsBrjxYqe2fN5uPsxuwFXvF8Kw05mehePKu5Z9e/vYiTWUEsAGMZ7OCQ1ZiEUKUHLLKOX4tpX5mXxTaJsau+BQLxNz2wA50taYuBPm8UxbPo8kjSiKuAKDJ5SRY0DudJZjtsJP+Dh05+IpptNXC1ZVuDBScO5G+b/O3MRo4b1qYF9iLT4YFXY9LZExc7xbF7FC1lQ2E+5aZ/7eL7ZBK/pkQ1NFVADNXYc2opgjnWQqw/zr8W6vkXM/Pr0A+lMQ2vbf7L3oCNLuPMsMmYegdR2rYAUNoytBUg9PzFjsz6HqLlcP3CxPc68OcAM/+9s=",
#             "body": "{\n  \"Type\" : \"Notification\",\n  \"MessageId\" : \"0363b33e-e862-5424-bb9a-eba0962e6f00\",\n  \"TopicArn\" : \"arn:aws:sns:us-east-2:133534076130:turbot-firehose-user-sns-topic\",\n  \"Subject\" : \"[punisher-turbot] Control Approved updated by Turbot Identity\",\n  \"Message\" : \"{\\\"notificationType\\\":\\\"control_updated\\\",\\\"actor\\\":{\\\"identity\\\":{\\\"picture\\\":\\\"https://www.gravatar.com/avatar/cb9ff8606c24daf9cda1d82615bd7a8e\\\",\\\"turbot\\\":{\\\"title\\\":\\\"Turbot Identity\\\",\\\"id\\\":\\\"173249891011852\\\"}}},\\\"turbot\\\":{\\\"type\\\":null,\\\"controlId\\\":\\\"21214\\\",\\\"controlOldVersionId\\\":\\\"216036317180248\\\",\\\"controlNewVersionId\\\":\\\"216036328690947\\\",\\\"createTimestamp\\\":\\\"2021-02-11T00:36:17.236Z\\\"},\\\"control\\\":{\\\"state\\\":\\\"ok\\\",\\\"reason\\\":\\\"Approved\\\",\\\"details\\\":[{\\\"key\\\":\\\"Usage\\\",\\\"value\\\":\\\"Approved\\\"},{\\\"key\\\":\\\"Regions\\\",\\\"value\\\":\\\"Approved\\\"},{\\\"key\\\":\\\"Budget\\\",\\\"value\\\":\\\"Skipped\\\"},{\\\"key\\\":\\\"RESULT\\\",\\\"value\\\":\\\"Approved\\\"}],\\\"type\\\":{\\\"trunk\\\":{\\\"title\\\":\\\"AWS > S3 > Bucket > Approved\\\"}},\\\"turbot\\\":{\\\"id\\\":\\\"213971925119603\\\"},\\\"resource\\\":{\\\"akas\\\":[\\\"arn:aws:s3:::raj-switch-role-bucket\\\"],\\\"metadata\\\":{\\\"aws\\\":{\\\"accountId\\\":\\\"133534076130\\\",\\\"partition\\\":\\\"aws\\\",\\\"regionName\\\":\\\"us-east-2\\\"},\\\"createTimestamp\\\":\\\"2021-01-18T16:35:52.000Z\\\"},\\\"title\\\":null,\\\"turbot\\\":{\\\"id\\\":\\\"213971924734526\\\"}}},\\\"oldControl\\\":{\\\"state\\\":\\\"alarm\\\",\\\"turbot\\\":{\\\"id\\\":\\\"213971925119603\\\"}}}\",\n  \"Timestamp\" : \"2021-02-11T00:36:28.017Z\",\n  \"SignatureVersion\" : \"1\",\n  \"Signature\" : \"rqLLoN4vVAbX5XCz2YOxKVIx8HUBZJDFcs3zHHE+kDtKlA2jpPo87swuUgn8d2s2JBgnwRDAzjjWCFtHUtvW0uIHHmEFGchM0f4c3nN+5DBYs9axrpTmX/WRd3klr5ejOQKGyFfR85qj+BfWeMPtIjx0AEhaL06T+Mvhs6ASXuihcqgUbXiT280Xmd6K5POYq6oZ2dLk2H7Gwf8XvRl3gRgA0ETTjiDsPDIgCWixbHyVJQfyOa0KyeRtvBdZhTf4beblo6SYkKC4KVGqYMvlgZz1l4VYxH+GqcXA52zstXW0RTb4+TKsu+E4VB4MHpHOlmG4SNKq4QHUexDdOrjDWg==\",\n  \"SigningCertURL\" : \"https://sns.us-east-2.amazonaws.com/SimpleNotificationService-010a507c1833636cd94bdb98bd93083a.pem\",\n  \"UnsubscribeURL\" : \"https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-2:133534076130:turbot-firehose-user-sns-topic:a036479e-e982-4824-ad26-96f36636a384\"\n}",
#             "attributes": {
#                 "ApproximateReceiveCount": "1",
#                 "SentTimestamp": "1613003788047",
#                 "SenderId": "AIDAIVEA3AGEU7NF6DRAG",
#                 "ApproximateFirstReceiveTimestamp": "1613003788048"
#             },
#             "messageAttributes": {},
#             "md5OfMessageAttributes": None,
#             "md5OfBody": "f6a2486aaa3b534c1b2602c595e3e02d",
#             "eventSource": "aws:sqs",
#             "eventSourceARN": "arn:aws:sqs:us-east-2:133534076130:morales_firehose_raw_alarms_queue",
#             "awsRegion": "us-east-2"
#         },
#         {
#             "messageId": "8ea8ffb7-aaae-429f-96f8-ea1851a6e913",
#             "receiptHandle": "AQEBcmDgMgSuhmp0ZOopycdusSdBtMjW/Y0wzDLSSfunnFpGQ4qVOrv9twvW6hjwpikfaSsAigdMfGxkLYmHxTvCkePH55ct8nSFa/Y/ARabd81MX63Zz7CrB0F/aigxDMr04/fYOPLGOTU6ikJgfxGqPq7LykoSWE5uzU5Yn4YgfWv+ODOgH8kF/jaYRXROF1HvwUwijNv7bQbqg53J6f1rewahEEI90DvUSwF7TYjFbgR644qMQCQJmYHpI8mFKe5hsNlpQwtxE3dgVlevwPlNQfxcGic0JA/iIsu3Zgr6ywJoy56rXoQO+APlgfU55o91T9+6mHUxOctsDAbEFCjZqoAjOX/AQnPmpm4QnfXVM/BW3qu1LAZ4b+enVvfwoNBNxHmcGgjK5GMXVdjXdUazvTfd4CHjBrgIu+ECF81h6A8=",
#             "body": "{\n  \"Type\" : \"Notification\",\n  \"MessageId\" : \"bd8b6d21-6b79-57b3-a66b-35bf153581b7\",\n  \"TopicArn\" : \"arn:aws:sns:us-east-2:133534076130:turbot-firehose-user-sns-topic\",\n  \"Subject\" : \"[punisher-turbot] Control Approved updated by Turbot Identity\",\n  \"Message\" : \"{\\\"notificationType\\\":\\\"control_updated\\\",\\\"actor\\\":{\\\"identity\\\":{\\\"picture\\\":\\\"https://www.gravatar.com/avatar/cb9ff8606c24daf9cda1d82615bd7a8e\\\",\\\"turbot\\\":{\\\"title\\\":\\\"Turbot Identity\\\",\\\"id\\\":\\\"173249891011852\\\"}}},\\\"turbot\\\":{\\\"type\\\":null,\\\"controlId\\\":\\\"21397\\\",\\\"controlOldVersionId\\\":\\\"216036328690947\\\",\\\"controlNewVersionId\\\":\\\"216036333047576\\\",\\\"createTimestamp\\\":\\\"2021-02-11T00:36:21.489Z\\\"},\\\"control\\\":{\\\"state\\\":\\\"alarm\\\",\\\"reason\\\":\\\"Not approved\\\",\\\"details\\\":[{\\\"key\\\":\\\"Usage\\\",\\\"value\\\":\\\"Not approved\\\"},{\\\"key\\\":\\\"Regions\\\",\\\"value\\\":\\\"Approved\\\"},{\\\"key\\\":\\\"Budget\\\",\\\"value\\\":\\\"Skipped\\\"},{\\\"key\\\":\\\"RESULT\\\",\\\"value\\\":\\\"Not approved\\\"}],\\\"type\\\":{\\\"trunk\\\":{\\\"title\\\":\\\"AWS > S3 > Bucket > Approved\\\"}},\\\"turbot\\\":{\\\"id\\\":\\\"213971925119603\\\"},\\\"resource\\\":{\\\"akas\\\":[\\\"arn:aws:s3:::raj-switch-role-bucket\\\"],\\\"metadata\\\":{\\\"aws\\\":{\\\"accountId\\\":\\\"133534076130\\\",\\\"partition\\\":\\\"aws\\\",\\\"regionName\\\":\\\"us-east-2\\\"},\\\"createTimestamp\\\":\\\"2021-01-18T16:35:52.000Z\\\"},\\\"title\\\":null,\\\"turbot\\\":{\\\"id\\\":\\\"213971924734526\\\"}}},\\\"oldControl\\\":{\\\"state\\\":\\\"ok\\\",\\\"turbot\\\":{\\\"id\\\":\\\"213971925119603\\\"}}}\",\n  \"Timestamp\" : \"2021-02-11T00:36:28.808Z\",\n  \"SignatureVersion\" : \"1\",\n  \"Signature\" : \"sjqj3IEDmz2UYnJr92fsurNTttLO1LEl1tqqeb40CbiN+L0D4Ft60Bz4J2GO1NGWu6nexBTsPs0PA9x7EVZTucZjkDcDR8gRrLJ1Jwkv86ojp0n5Ruu5zg+a4pVNZan6vrbAuUUtz48hh2YAGxSWKtAglT+3waBB+QvuYYRwrFvwPCkCrx7amfFPmCsKYdnUMBgYVG6bdxGwKGlhPfgOh5fOxn4POfQLX1YdDNcYSuOqq3xMn1GaZ8uoIPIi8e1R9tlXCCjvx0bB6/VlWWfe0supG62Hj9O/qy/IARfj4Ae5/FM/0BEYFUKUg43uevOtWPlsh3KxixoOhrsfvh6n4Q==\",\n  \"SigningCertURL\" : \"https://sns.us-east-2.amazonaws.com/SimpleNotificationService-010a507c1833636cd94bdb98bd93083a.pem\",\n  \"UnsubscribeURL\" : \"https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-2:133534076130:turbot-firehose-user-sns-topic:a036479e-e982-4824-ad26-96f36636a384\"\n}",
#             "attributes": {
#                 "ApproximateReceiveCount": "1",
#                 "SentTimestamp": "1613003788832",
#                 "SenderId": "AIDAIVEA3AGEU7NF6DRAG",
#                 "ApproximateFirstReceiveTimestamp": "1613003788833"
#             },
#             "messageAttributes": {},
#             "md5OfMessageAttributes": None,
#             "md5OfBody": "ec171637d6f30f8a7da63afabec428fa",
#             "eventSource": "aws:sqs",
#             "eventSourceARN": "arn:aws:sqs:us-east-2:133534076130:morales_firehose_raw_alarms_queue",
#             "awsRegion": "us-east-2"
#         },
#         {
#             "messageId": "5f6ed1c4-8d50-47f7-802c-994d52f82550",
#             "receiptHandle": "AQEBsUVoPOzW5KaHW1k9vLppGaJ0HcXjDro5QHeHij6fOxilvbGYok3a+3BcrhOlgDuRzYplNZcj3sy8zZPvUNwT5/Gr5gNa3YGi1Dl8l6di+3HU9u9FX8lrlZ7I1EEc+lIOUuE6o5cbgqlR2mYW0UAQooWs/YqKZorsECHzSTS2Jve+d5WQs1mQAgQEpzU+lx8sLzWnKnl60GvCSGeixywv+w9ddJvHHyCcG+j4rAG3rmAcCoeXb5FgE54xa5EwHLQuU5WcWHUPM0NNlXuH3uJOBBozA3Kk/NQQzJE6hiX+6gLKJB3xx8cdHnecPclFQK9wiDqgS9pFZ1wDxzTc6hy7i15uYlDZYZNeMTqklZMBtaWPb5hugOjy4gjdh4m/rlj5ATfi2scKGu2cB8Xfw0ezDHzjjwlp+71EtVmLJ+vcJEY=",
#             "body": "{\n  \"Type\" : \"Notification\",\n  \"MessageId\" : \"1c700edf-e1cf-5381-a621-56419f828b41\",\n  \"TopicArn\" : \"arn:aws:sns:us-east-2:133534076130:turbot-firehose-user-sns-topic\",\n  \"Subject\" : \"[punisher-turbot] Control Approved updated by Turbot Identity\",\n  \"Message\" : \"{\\\"notificationType\\\":\\\"control_updated\\\",\\\"actor\\\":{\\\"identity\\\":{\\\"picture\\\":\\\"https://www.gravatar.com/avatar/cb9ff8606c24daf9cda1d82615bd7a8e\\\",\\\"turbot\\\":{\\\"title\\\":\\\"Turbot Identity\\\",\\\"id\\\":\\\"173249891011852\\\"}}},\\\"turbot\\\":{\\\"type\\\":null,\\\"controlId\\\":\\\"213971925119603\\\",\\\"controlOldVersionId\\\":\\\"216036333047576\\\",\\\"controlNewVersionId\\\":\\\"216036336629722\\\",\\\"createTimestamp\\\":\\\"2021-02-11T00:36:24.987Z\\\"},\\\"control\\\":{\\\"state\\\":\\\"ok\\\",\\\"reason\\\":\\\"Approved\\\",\\\"details\\\":[{\\\"key\\\":\\\"Usage\\\",\\\"value\\\":\\\"Approved\\\"},{\\\"key\\\":\\\"Regions\\\",\\\"value\\\":\\\"Approved\\\"},{\\\"key\\\":\\\"Budget\\\",\\\"value\\\":\\\"Skipped\\\"},{\\\"key\\\":\\\"RESULT\\\",\\\"value\\\":\\\"Approved\\\"}],\\\"type\\\":{\\\"trunk\\\":{\\\"title\\\":\\\"AWS > S3 > Bucket > Approved\\\"}},\\\"turbot\\\":{\\\"id\\\":\\\"213971925119603\\\"},\\\"resource\\\":{\\\"akas\\\":[\\\"arn:aws:s3:::raj-switch-role-bucket\\\"],\\\"metadata\\\":{\\\"aws\\\":{\\\"accountId\\\":\\\"133534076130\\\",\\\"partition\\\":\\\"aws\\\",\\\"regionName\\\":\\\"us-east-2\\\"},\\\"createTimestamp\\\":\\\"2021-01-18T16:35:52.000Z\\\"},\\\"title\\\":null,\\\"turbot\\\":{\\\"id\\\":\\\"213971924734526\\\"}}},\\\"oldControl\\\":{\\\"state\\\":\\\"alarm\\\",\\\"turbot\\\":{\\\"id\\\":\\\"213971925119603\\\"}}}\",\n  \"Timestamp\" : \"2021-02-11T00:36:29.800Z\",\n  \"SignatureVersion\" : \"1\",\n  \"Signature\" : \"jwL93HhFs8S8tP+NAS61W2bkH2HVerh71gXCPVvTfb5WA55GnL6n1xVXg2Yu3vS9Eh6l+c1fuMvGkc0bmJcw4/XFoSQAx8BtbtCPGX+qiu9bawJu01Pdpvd9T7BYBXOEF2OeVHDz1ulL+tpI5/LIv/TGieZNgLcFZJBsiOkaDyQptFPPnBKXRQnLIy7sBSdlNQBgYTOFcORZth8lKZYlNPXS/ciSeh85QEQWhkWQzcI4u4p+2Z7OA3dyDAO1+MoRljKV5Y7wVCm0MsYlrPfJghFjoDsOLtZfvo0CO+ewLJLknQ4y4tjzqJ4yTyIJhAWwCcP3zAbC8NA87FEgn4KrTQ==\",\n  \"SigningCertURL\" : \"https://sns.us-east-2.amazonaws.com/SimpleNotificationService-010a507c1833636cd94bdb98bd93083a.pem\",\n  \"UnsubscribeURL\" : \"https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-2:133534076130:turbot-firehose-user-sns-topic:a036479e-e982-4824-ad26-96f36636a384\"\n}",
#             "attributes": {
#                 "ApproximateReceiveCount": "1",
#                 "SentTimestamp": "1613003789825",
#                 "SenderId": "AIDAIVEA3AGEU7NF6DRAG",
#                 "ApproximateFirstReceiveTimestamp": "1613003789826"
#             },
#             "messageAttributes": {},
#             "md5OfMessageAttributes": None,
#             "md5OfBody": "221ce000191dd0d02c15917f65cedccc",
#             "eventSource": "aws:sqs",
#             "eventSourceARN": "arn:aws:sqs:us-east-2:133534076130:morales_firehose_raw_alarms_queue",
#             "awsRegion": "us-east-2"
#         },
#         {
#             "messageId": "1f6fd4df-5b11-4d11-acf6-957b6e99fa6e",
#             "receiptHandle": "AQEBfcsRZ9mv0NoPLwd2Jdhtok3Kf1Dae0jzYo9k1lu0wRlZUZJ7siZt6ffv3/+xA5gH70/8GvOzYLHwNtbmPdt5mcT/mXIXvb2rAH1AYZAIfkI0iVEfGHEOxhaxHhbKNQk2KBHY1cJNojTzhMJi5DDiY0twE3/1cN+tOJZr0OKl2Ai8Hw51UzmV4cWrGqI1Hijsuz05rTfOGWUY4IN8Olw9WI44Nu/qeNrNJHwJlbGV6AKv55/JzDDUxkiCuXEZSPVnSVvWFJZnDpkwudvMC6gJ80G6DCJfOIU4QiqwootN1C0tvvqslO0yhr9BdXzxzZlyMpSbq33ObJLqFR2pKbDw/ftZAkPsRQlXtXXI+EapImMA494WIkYM4467dPIZInfXmaZnloTQNBhZuejqGazRB8fskGU5ynRsi5o8Zvsla08=",
#             "body": "{\n  \"Type\" : \"Notification\",\n  \"MessageId\" : \"cb145d6d-93e3-55d0-943a-05f3edaeaa77\",\n  \"TopicArn\" : \"arn:aws:sns:us-east-2:133534076130:turbot-firehose-user-sns-topic\",\n  \"Subject\" : \"[punisher-turbot] Control Approved updated by Turbot Identity\",\n  \"Message\" : \"{\\\"notificationType\\\":\\\"control_updated\\\",\\\"actor\\\":{\\\"identity\\\":{\\\"picture\\\":\\\"https://www.gravatar.com/avatar/cb9ff8606c24daf9cda1d82615bd7a8e\\\",\\\"turbot\\\":{\\\"title\\\":\\\"Turbot Identity\\\",\\\"id\\\":\\\"173249891011852\\\"}}},\\\"turbot\\\":{\\\"type\\\":null,\\\"controlId\\\":\\\"213971925119603\\\",\\\"controlOldVersionId\\\":\\\"216036333047576\\\",\\\"controlNewVersionId\\\":\\\"216036336629722\\\",\\\"createTimestamp\\\":\\\"2021-02-11T00:36:24.987Z\\\"},\\\"control\\\":{\\\"state\\\":\\\"ok\\\",\\\"reason\\\":\\\"Approved\\\",\\\"details\\\":[{\\\"key\\\":\\\"Usage\\\",\\\"value\\\":\\\"Approved\\\"},{\\\"key\\\":\\\"Regions\\\",\\\"value\\\":\\\"Approved\\\"},{\\\"key\\\":\\\"Budget\\\",\\\"value\\\":\\\"Skipped\\\"},{\\\"key\\\":\\\"RESULT\\\",\\\"value\\\":\\\"Approved\\\"}],\\\"type\\\":{\\\"trunk\\\":{\\\"title\\\":\\\"AWS > S3 > Bucket > Approved\\\"}},\\\"turbot\\\":{\\\"id\\\":\\\"213971925119603\\\"},\\\"resource\\\":{\\\"akas\\\":[\\\"arn:aws:s3:::raj-switch-role-bucket\\\"],\\\"metadata\\\":{\\\"aws\\\":{\\\"accountId\\\":\\\"133534076130\\\",\\\"partition\\\":\\\"aws\\\",\\\"regionName\\\":\\\"us-east-2\\\"},\\\"createTimestamp\\\":\\\"2021-01-18T16:35:52.000Z\\\"},\\\"title\\\":null,\\\"turbot\\\":{\\\"id\\\":\\\"213971924734526\\\"}}},\\\"oldControl\\\":{\\\"state\\\":\\\"alarm\\\",\\\"turbot\\\":{\\\"id\\\":\\\"213971925119603\\\"}}}\",\n  \"Timestamp\" : \"2021-02-11T00:36:29.844Z\",\n  \"SignatureVersion\" : \"1\",\n  \"Signature\" : \"tXPOjoPlElJtiKWX5EIXMwLs7JRXKnj+xj1n4KL19w2tbgqbzmvV+ncRAogYoxdhI72oFvo1vaz2edOBB8O/9l9+8TvlLwx3MXw3fJidwOA6cXJMpux9ah+Fs/D137ebg7W24ibChWb+4CLDDAIyQUn5b1dtwdkN9ayein6uwIF7Bxr+N9M35homuEkDAZyVjvAPGd5TIn/EB+5WdLxa9UxpVHaTvJDXMvfjopdV37YzYgjYqupIhGmjRfE7JjXPqgnrONdoVQdbPxulQTKe1L4B0DsH1xORMSl+ZjLa2WacMLRIMJfFxM5qRcK/QJ6uhLpt+XUuDdqZSqirq4/0WQ==\",\n  \"SigningCertURL\" : \"https://sns.us-east-2.amazonaws.com/SimpleNotificationService-010a507c1833636cd94bdb98bd93083a.pem\",\n  \"UnsubscribeURL\" : \"https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-2:133534076130:turbot-firehose-user-sns-topic:a036479e-e982-4824-ad26-96f36636a384\"\n}",
#             "attributes": {
#                 "ApproximateReceiveCount": "1",
#                 "SentTimestamp": "1613003789875",
#                 "SenderId": "AIDAIVEA3AGEU7NF6DRAG",
#                 "ApproximateFirstReceiveTimestamp": "1613003789876"
#             },
#             "messageAttributes": {},
#             "md5OfMessageAttributes": None,
#             "md5OfBody": "2e8279f5dd14f0c58de655e94a1ab551",
#             "eventSource": "aws:sqs",
#             "eventSourceARN": "arn:aws:sqs:us-east-2:133534076130:morales_firehose_raw_alarms_queue",
#             "awsRegion": "us-east-2"
#         }
#     ]


# }


class Context:
    def __init__(self) -> None:
        self.invoked_function_arn = "arn:aws:lambda:us-east-2:133534076130:function:TurbotFirehoseFilterFunction"
        pass

context = Context()

filter_function.lambda_handler(event, context)