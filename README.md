# viaChallenge
Via challenge assignment

This is the service repo. The serialized model from the viaChallengeModel repo was uploaded and run.

Flask was used to expose the service. 
Tensorflow and Keras were adopted to process predictions

to call the service: 
http:\<hostadress\>/predict/\<sepallength\>/\<sepalwidth\>/\<petallength\>/\<petalwidth\>

replace arguments with respective values

return value is the name of the specie: setosa, versicolor or virginica

> Attempt to upload to Azure failed due to debug mode option - turn it to false did not work

