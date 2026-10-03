#Script bash da questão 2 da Prova 1

#Comando que mostra a pasta/diretório no qual me encontro
echo 'Você se encontra neste diretório: '
pwd
echo '___________________________________'

#Comando que gere uma lista com detalhes do conteúdo da pasta HOME e redirecione essa lista para o arquivo: lista_HOME.txt
echo 'Redirecionando ao diretório HOME....'
cd ~/ 
echo 'Lendo diretórios e arquivos presentes em HOME'
ls > lista_HOME.txt

#Mostrar conteúdo armazenado no .txt
echo 'O conteúdo presente no diretório HOME é: '
cat lista_HOME.txt
echo '_________________________________'

#Mostrar a data atual
echo 'A última data de execução deste script foi: '
date
echo '______________FIM DO SCRIPT_______________'
