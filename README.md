# Lambda MapProxy

A basic [Serverless](https://serverless.com) setup to run MapProxy as an Amazon Web Service Lambda Function.

You will need to have an Amazon IAM user set up with valid credentials in your environment. Instructions for this can be found [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html).

You will need to create an s3 bucket (this is where the cached tiles are stored). In the serverless.yml file, you will need to change line 16 from "mapproxy-lambda-demo" to your bucket name.

Likewise you will need to change the bucket_name on line 53 in mapproxy.yaml.

Currently mapproxy.yaml is configured to hit the OSM tile server, you can configure the services, layers, caches, grids, and sources as per the documentation at (https://mapproxy.org). Note that this lambda is really only set up to use the S3 cache.

To get started, you must have npm already installed on your system along with a couple plugins:
```sh
npm install -g serverless
serverless plugin install -n serverless-apigw-binary
serverless plugin install -n serverless-wsgi
```

From here, you can deploy using serverless:
```sh
serverless deploy
```

This command line will return information about what has been deployed. The most important bit here is the endpoints which will return a link like:
 ```
 endpoints:
    GET - https://nobqrkpnhl.execute-api.us-west-1.amazonaws.com/dev/{proxy+}
```
Going to the link provided minus the {proxy+} will take you to the MapProxy Root (https://nobqrkpnhl.execute-api.us-west-1.amazonaws.com/dev/ will remain up through FOSS4GNA as an example) 
