# 💲 ETL + Dashboard de Taxas de Câmbio
Dashboard **Power BI** sobre taxas de câmbio com base no real brasileiro com dados provenientes da Frankfurt API. Todos os dias às 20h é executado um script Python responsável por extrair os dados da API e armazená-los no banco de dados **MySQL**. Em seguida as **Views** são atualizadas e expostas no Dashboard.

<img width="1299" height="731" alt="image" src="https://github.com/user-attachments/assets/33587b83-d915-413f-930a-988934554634" />

## Modelagem dos Dados
Há duas tabelas: "currencies" e "rates". A primeira armazena informações das moedas: nome, símbolo, sigla e um ID particular. A segunda armazena um ID particular, a taxa de câmbio, sua data e a chave estrangeira da moeda.

## Extração dos Dados
O script responsável pela população da tabela "currencies" se chama `currency_loader.py`.
<img width="1484" height="616" alt="{0BEA09D2-D4D8-4A3A-8B09-52764F08327C}" src="https://github.com/user-attachments/assets/0b5923bb-372e-4ba0-97cf-c95ecae8ad51" />

O script responsável pela extração das taxas de câmbio anteriores se chama `get_past_rate.py`
<img width="1509" height="673" alt="{657A418E-6384-4E18-9815-3982893F57DF}" src="https://github.com/user-attachments/assets/e336ae52-f34c-4d2c-a9cc-0f43a55c707b" />

O script responsável pela extração diária das novas taxas se chama `get_yesterdays_rate.py`
<img width="1539" height="882" alt="{AE0321C9-E3F2-491B-8222-F9ED99426F85}" src="https://github.com/user-attachments/assets/bbb1cd4a-e88c-4977-ba6a-e25240975d0f" />

## Análise dos Dados
A inserção de novos dados no banco faz com que as **Views** sejam atualizadas. Há 4 views: extremos cambiais; variação cambial (até 2 dias); variação cambial até 15 dias; variação cambial histórica (até Setembro/2026).

<img width="1203" height="509" alt="{88B91B19-E1A3-476D-8DC1-353E5C983C4D}" src="https://github.com/user-attachments/assets/b6c67e53-c17d-4c2a-9246-725e4dc28044" />

## Dashboard Power BI
Com novos dados, basta atualizar o Dashboard para visualizá-los. Observe a comparação entre dois dias diferentes:

<img width="1217" height="685" alt="image" src="https://github.com/user-attachments/assets/8a9b1865-2970-4036-99eb-31330a3bb9e2" />
<img width="1300" height="731" alt="{514F6F55-5049-44E0-B44B-DA604B491BD8}" src="https://github.com/user-attachments/assets/6a54965f-b71c-463b-accc-63434619eef8" />

### Evolução por Moeda
Este gráfico permite visualizar a evolução cambial de uma moeda específica.
<img width="617" height="265" alt="{B187EAB3-E024-492C-8667-0714EB821B99}" src="https://github.com/user-attachments/assets/3d33a777-9de3-4272-9137-e9611e1573de" />
<img width="734" height="298" alt="{3BD5AF01-F937-46E1-98DE-68F94F7F4967}" src="https://github.com/user-attachments/assets/ba119b4d-1bb8-45fb-ad54-632898e3f1c6" />

### Maior e Menor Taxa de Câmbio de Hoje
Exibe os extremos cambiais, a moeda na qual o real vale menos e a moeda na qual o real vale mais. No exemplo, 1 real valem 347.353 mil riais iranianos e 0,0047 onças troy.
<img width="612" height="172" alt="{FD852E74-16EC-4845-B6FE-CEA32FF5E4F4}" src="https://github.com/user-attachments/assets/9a77acf8-f34d-4647-b22d-62891c441784" />

### Maior Valorização e Desvalorização dos Últimos 2 dias
O primeiro gráfico mostra quais moedas quais moedas o real obteve poder de compra maior, e no segundo gráfico, poder de compra menor, na janela de 2 dias.
<img width="564" height="195" alt="{3050CA55-FED3-4B20-9E7D-170B1AA4C9E7}" src="https://github.com/user-attachments/assets/8972a464-db09-4575-ba98-73b66f468f42" />

### Maior Valorização e Desvalorização dos Últimos 15 dias
O primeiro gráfico mostra quais moedas quais moedas o real obteve poder de compra maior, e no segundo gráfico, poder de compra menor, na janela de 15 dias.
<img width="571" height="201" alt="{2E51E890-2A74-4518-A132-6D165DE51F2C}" src="https://github.com/user-attachments/assets/3c56cb41-4c42-4c3a-9646-e507004a8808" />


### Maior Valorização e Desvalorização desde Setembro
O primeiro gráfico mostra quais moedas quais moedas o real obteve poder de compra maior, e no segundo gráfico, poder de compra menor, desde Setembro.
<img width="565" height="196" alt="{7D95E668-8822-4E40-BA5B-EFC19E9D8ACB}" src="https://github.com/user-attachments/assets/db846481-65b8-41dc-93ee-c588ae61e058" />

### Tooltip: Nome da Moeda
É possível visualizar o nome completo da moeda a partir de sua sigla.
<img width="607" height="711" alt="{765B63EE-731D-48EF-AFB5-6B5AE7BAA6A1}" src="https://github.com/user-attachments/assets/23d6f79f-9efb-4dbd-bdb4-ee3c69cab006" />
