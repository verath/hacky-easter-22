# Bucket Egg

> My Irish friend told me about his new web site. He told me it was in a bucket named `egg-in-a-bucket`. No clue what that is...

Buckets probably references the AWS S3 service.

From AWS documentation we find:

> Amazon S3 virtual-hosted-style URLs use the following format.
>
> ```
> https://bucket-name.s3.Region.amazonaws.com/key-name
> ```

The Irish AWS region is "eu-west-1".

Accessing https://egg-in-a-bucket.s3.eu-west-1.amazonaws.com
gives us an error. But if we specify the file we are looking for (index.html,
probably) then it works:

https://egg-in-a-bucket.s3.eu-west-1.amazonaws.com/index.html

We get an image of a QR code egg, which we can scan to get the flag:
`he2022{th1s_3gg_1s_1n_4_buck3t}`
