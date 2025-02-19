#!/bin/bash

echo -e "\e[1;32m[+] Iniciando requisição com curl...\e[0m"
curl -u natas4:QryZXc2e0zahULdHrtHxzyYkj59kUxLQ -H "Referer: http://natas5.natas.labs.overthewire.org/" http://natas4.natas.labs.overthewire.org/ 2> /dev/null | \
  grep --color=always -E "Access|Error|Forbidden|Disallowed|You|page" || echo -e "\e[1;31m[-] Algo deu errado. Verifique a requisição!\e[0m"

echo -e "\e[1;34m[+] Requisição finalizada com sucesso!\e[0m"

