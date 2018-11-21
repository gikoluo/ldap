# ldap

== 0. Init k8s env 

CLUSTER_NAME=cloud-cluster

gcloud container clusters create $CLUSTER_NAME


gcloud container clusters get-credentials $CLUSTER_NAME



== 1. Create namespace

kubectl create ns auth

```shell
DOMAIN=
./gencert.sh

kubectl create secret tls login.k8s.luochunhui.com.tls --cert=ssl/cert.pem --key=ssl/key.pem -n auth

