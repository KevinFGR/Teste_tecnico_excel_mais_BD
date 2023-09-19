# Teste_tecnico_excel_mais_BD

<h2>Questões</h2>
<b>Questão 1 – Contingência, processamento manual de dados</b>
<p>Cenário hipotético: Um de nossos fornecedores enviam dados em lote por meio de API (Web Services). Periodicamente, é necessário o consumo desta API para que os dados sejam atualizados, garantindo assim a continuidade dos serviços da Infocar. O fornecedor entrou em contato com os representantes da Infocar para sinalizar que o lote em específico deverá ser processado manualmente com transferência de arquivo em Excel (teste-ti-processamento_fornecedor_fora_do_ar.xlsx) já que a API está fora e sem previsão.
Na sequência, você como responsável de processamento, recebeu esta notícia através do seu e-mail para que o processo manual seja executado.
Com base no cenário hipotético acima, resolva:</p>

<ol type="a">
<li>Antes de “sair fazendo” “go horse”. Quais são os passos imediatos a serem tomados em um melhor fluxo o possível de trabalho e ágil?</li>
  <p>
	Resposta: Com base na situação descrita, levaria em consideração uma metodologia ágil básica em cascata para a resolução. Os passos seriam: Análise da situação, planejamento, implementação, testes e manutenção.
  </p>
	<p>
    A análise da situação se dá a partir do enunciado (Um imprevisto no fluxo padrão de funcionamento da recepção de dados que acarretará na criação de um script para remediá-la). Inclusive, por conta de ser um imprevisto não usarei metodologias muito complexas que demandam mais tempo.	
  </p>
  <p>
	O planejamento é o momento se pensar no que vou fazer para resolver o problema e como vou executar isso e, caso houvesse mais pessoas envolvidas, delegar quem faria cada atividade. Portanto, uma vez que o enunciado menciona a necessidade dessa atividade para o bom funcionamento dos serviços da Infocar, escolhi a linguagem Python para essa tarefa, pois, já tenho experiências pessoais voltadas a manipulação de arquivos de planilhas com ela e pela sua sintaxe fácil, rápida de programar que tem chance menor de erros.
  </p>
  <p>
	A implementação será a “mão na massa”, a hora em que criarei o código e para os testes usarei os comandos try e except do python para melhor depuração e tratamento de erros.
  </p>
  <p>
	Por fim, a manutenção será feita a partir dos erros encontrados na fase de testes.
  </p>
 
<li>   Escreva um código que faça a leitura do arquivo com armazenamento dos dados em banco para que o processamento seja executado com sucesso.</li>
<p>
	Vídeo mostrando a execução:	https://drive.google.com/file/d/1EpPF6TuKOkzv2h1JcjXg7QeUR0rgckN9/view?usp=sharing
<p>
	<label>tecnologias necessárias:</label>
  <ul>
<li>Python</li>
<li>MYSQL / MariaDB
<li>Servidor localhost</li>
</ul>
	<label>Bibliotecas necessárias:</label>
 <ul>
<li>openpyxl => pip install openpyxl</li>
<li>mysql.connector => pip install mysql-connector-python</li>
 </ul>
 <p>
	O repositório está salvo no Google Drive e no GitHub. Caso seja necessário, a pasta no Drive está com a virtualenvi (venv) que usei para desenvolver:
 </p>
 <ul>
 	<li>Google Drive: https://drive.google.com/drive/folders/1ZQrJTlPYSA-mfDPivre9EK9ouWU1z-gT?usp=sharing</li>
	<li>Github: https://github.com/KevinFGR/Teste_tecnico_excel_mais_BD</li>
	
	
 </ol>
<b>Questão 2 –Processamento em grande escala</b>
<p>
Cenário hipotético: Tem uma tabela em banco de dados que possui 30 milhões de registros. Estes dados devem ser tratados e exportados em formato de arquivo. São 10 colunas e todas elas estão com definidas como VARCHAR(MAX).
</p>
<ol>
<li>Você trataria estes dados diretamente no banco? Justifique sua resposta</li>
	Resposta: Não, fazer tais modificações em um banco de dados em produção não é uma boa prática uma vez que há riscos de perder ou modificar dados importantes para o funcionamento da empresa. o único comando que eu realizaria no banco é um SELECT para obter os dados e as modificações seriam feitas no script sem alteração no banco.	
<li>Monte um algoritmo que processaria a exportação para CSV, onde todos os registros teriam no máximo 30 dígitos cada coluna.</li>
  <p>
	Vídeo mostrando a execução:	https://drive.google.com/file/d/1ExBJUOKbBI4EUPG0lylPaZnj_nzFBT3R/view?usp=sharing
  </p>
	<label>tecnologias necessárias:</label>
  <ul>
<li>Python</li>
<li>MYSQL / MariaDB
<li>Servidor localhost</li>
</ul>
	<label>Bibliotecas necessárias:</label>
 <ul>
<li>openpyxl => pip install openpyxl</li>
<li>mysql.connector => pip install mysql-connector-python</li>
 </ul>
 <p>
	O repositório está salvo no Google Drive e no GitHub. Caso seja necessário, a pasta no Drive está com a virtualenvi (venv) que usei para desenvolver:
 </p>
 <ul>
 	<li>Google Drive: https://drive.google.com/drive/folders/1ZQrJTlPYSA-mfDPivre9EK9ouWU1z-gT?usp=sharing</li>
	<li>Github: https://github.com/KevinFGR/Teste_tecnico_excel_mais_BD</li>
