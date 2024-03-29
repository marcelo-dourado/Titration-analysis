# Titration analysis

## Introdução
Esta ferramenta foi desenvolvida para facilitar a extração dos resultados da titulação conduzida no Metrohm Titrino 848. O programa lê os arquivos .txt gerado pelo titulador, extrai os dados de múltiplos arquivos de titulação e compila os resultados em uma planilha Excel estruturada.

## Instalação
- Clone ou baixe o repositório contendo o arquivo executável.

## Como Usar
1. Clique no arquivo executável "Titration analysis".
2. A janela da interface gráfica (GUI) aparecerá com o título "Titration analysis".
3. Clique no botão "Escolher um diretório".
4. Uma janela de diálogo de arquivo será aberta. Navegue até a pasta contendo os arquivos de titulação que deseja analisar e selecione-a.
5. A ferramenta processará os dados do diretório selecionado.
6. Uma vez concluído o processo, uma mensagem aparecerá indicando que a análise está completa e os resultados serão salvos na pasta de saída.
7. Navegue até a pasta de saída para encontrar a planilha Excel gerada chamada "Resultado da titulação - [NomeDaPasta].xlsx", onde [NomeDaPasta] é o nome do diretório selecionado na etapa 4.

## Entendendo os Resultados
A planilha Excel gerada contém duas abas:
1. **Dados**:
Esta aba contém os dados brutos extraídos dos arquivos de titulação. Cada linha representa uma análise de titulação e as colunas incluem:
- Análise: Nome da análise
- Amostra: Nome da amostra
- Volume amostra (mL): Volume da amostra
- Volume EP (mL): Volume do ponto equivalente
- Concentração: Concentração
- Unidade: Unidade (se disponível)

2. **Estatísticas**:
   Esta aba contém informações estatísticas calculadas a partir dos dados brutos. Inclui a média, desvio padrão (SD) e coeficiente de variação (% CV) para cada amostra.

## Observações
- Certifique-se de que os arquivos de titulação estejam armazenados em um único diretório.
- A ferramenta ignora qualquer arquivo com a extensão ".ini".
- Verifique se os arquivos de titulação estão formatados corretamente para uma extração precisa de dados.

## Créditos
- Desenvolvido por Marcelo De Luccas Dourado.

Para quaisquer dúvidas ou problemas, entre em contato com o desenvolvedor via marcelodourado.eq@gmail.com.

