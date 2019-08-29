git clone https://github.com/guilhermewolf/docker-stack-python.git

Criar rede 'amadeu-net' com driver overlay

Buildar a imagem

Editar docker-compose.yml
- Adicionar 3 replicas do app
- App na porta 9000
- Hostname dos containers com nome do nó que ele esta (templates)
- DB em modo global

Levantar a stack com o nome amadeu

