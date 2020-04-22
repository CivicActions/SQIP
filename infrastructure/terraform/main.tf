




resource "aws_qldb_ledger" "test-ledger" {
  name = "test-ledger"
}

data "helm_repository" "bitnami" {
  name = "bitnami"
  url  = "https://charts.bitnami.com/bitnami"
}

resource "helm_release" "my_cache" {
  name       = "my-cache"
  repository = data.helm_repository.incubator.metadata[0].name
  chart      = "redis-cache"
}
